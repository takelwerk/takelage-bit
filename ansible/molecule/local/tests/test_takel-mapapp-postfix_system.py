import datetime
import email
import imaplib
import time

import pytest


def _create_mail_command_(takel_postfix_host, takel_postfix_domain,
                          mail_recipient):
    now = datetime.datetime.utcnow()
    mail_time = now.strftime('%Y-%m-%d_%H-%M-%S')
    mail_command = f"mail -s 'test:test_takel_postfix_system_sendmail " \
                   f"host:{takel_postfix_host}.{takel_postfix_domain} " \
                   f"time:{mail_time}' {mail_recipient} < /dev/null"
    return mail_command


def _classify_mails_(mails,
                     takel_postfix_from,
                     takel_postfix_host,
                     takel_postfix_domain,
                     mail_valid_till_minutes,
                     mail_expires_after_minutes):
    new_mail = {'received': False,
                'from': False,
                'return-path': False}
    mailids_expired = []
    for mailid, mail in mails.items():
        try:
            subject_dict = dict(
                keyvalue.split(':') for keyvalue in mail['subject'].split(' '))

            if subject_dict['test'] != 'test_takel_postfix_system_sendmail':
                continue

            expected_mail_subject_host = \
                f"{takel_postfix_host}.{takel_postfix_domain}"
            if subject_dict['host'] != expected_mail_subject_host:
                continue

            now = datetime.datetime.utcnow()
            mail_time = datetime.datetime.strptime(subject_dict['time'],
                                                   '%Y-%m-%d_%H-%M-%S')
            # a message from the future?
            if mail_time > now:
                continue

            # a message which is old enough to be deleted?
            if mail_time < now - datetime.timedelta(
                    minutes=mail_expires_after_minutes):
                mailids_expired.append(mailid)
                continue

            # a message too old for this test?
            if mail_time < now - datetime.timedelta(
                    minutes=mail_valid_till_minutes):
                continue

            # expected_mail_from = \
            #     f"{takel_postfix_host}.{takel_postfix_domain} " \
            #     f"<{takel_postfix_from}>"
            expected_mail_from = 'root <noreply@geospin.de>'
            if mail['From'] == expected_mail_from:
                new_mail['from'] = True

            expected_mail_return_path = f"<{takel_postfix_from}>"
            if mail['Return-Path'] == expected_mail_return_path:
                new_mail['return-path'] = True

            # a valid mail!
            new_mail['received'] = True
            mailids_expired.append(mailid)

        except:  # noqa: E722
            pass

    return new_mail, mailids_expired


def _new_test_mail_(takel_postfix_from,
                    takel_postfix_host,
                    takel_postfix_domain,
                    mail_username,
                    mail_password,
                    mail_server,
                    mail_valid_till_minutes,
                    mail_expires_after_minutes):
    mails = {}

    # login to recipient mail account
    connection = imaplib.IMAP4_SSL(mail_server)
    connection.login(mail_username, mail_password)

    # select inbox of recipient mail account
    connection.select()

    # loop over mails in inbox of recipient mail account
    typ, data = connection.search(None, 'ALL')
    for num in data[0].split():
        typ, data = connection.fetch(num, '(RFC822)')
        mails[num] = email.message_from_bytes(data[0][1])

    # classify mails
    new_mail, mailids_expired = _classify_mails_(mails,
                                                 takel_postfix_from,
                                                 takel_postfix_host,
                                                 takel_postfix_domain,
                                                 mail_valid_till_minutes,
                                                 mail_expires_after_minutes)

    # flag expired mails
    for mailid in mailids_expired:
        connection.store(mailid, '+FLAGS', '\\Deleted')

    # delete expired mails
    connection.expunge()

    # close connection to recipient mail account
    connection.close()
    connection.logout()

    return new_mail


# todo: fix mail configuration in mapapp
@pytest.mark.xfail
def test_takel_mapapp_postfix_system_sendmail(host, testvars, testpass):
    # get postfix vars
    takel_postfix_from = 'noreply@geospin.de'
    takel_postfix_domain = 'geospin.ai'
    takel_postfix_host = 'portal'
    mail_recipient = \
        testpass('geospin/devops/secrets/mail/geospinde_testinfra_login')

    # get mail credentials
    mail_username = \
        testpass('geospin/devops/secrets/mail/geospinde_testinfra_login')
    mail_password = \
        testpass('geospin/devops/secrets/mail/geospinde_testinfra_password')
    mail_server = \
        testpass('geospin/devops/secrets/mail/geospinde_testinfra_server')

    # get retention times
    mail_valid_till_minutes = \
        int(testpass('geospin/devops/secrets/mail/'
                     'geospinde_testinfra_valid_till_minutes'))
    mail_expires_after_minutes = \
        int(testpass('geospin/devops/secrets/mail/'
                     'geospinde_testinfra_expires_after_hours'))
    get_mail_retry_sleep = 5

    # send test mail
    mail_command = _create_mail_command_(
        takel_postfix_host,
        takel_postfix_domain,
        mail_recipient)
    host.run(mail_command)

    for attempt in range(0, 20):
        new_mail = _new_test_mail_(
            takel_postfix_from,
            takel_postfix_host,
            takel_postfix_domain,
            mail_username,
            mail_password,
            mail_server,
            mail_valid_till_minutes,
            mail_expires_after_minutes)
        if new_mail['received']:
            break
        time.sleep(get_mail_retry_sleep)

    assert new_mail['received']
    assert new_mail['from']
    assert new_mail['return-path']

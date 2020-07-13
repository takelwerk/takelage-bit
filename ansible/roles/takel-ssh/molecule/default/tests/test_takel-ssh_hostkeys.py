import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_ssh_hostkeys_private_ecdsa_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_ecdsa_key' in testvars:
        takel_ssh_host_ecdsa_key = \
            testvars['takel_ssh_host_ecdsa_key']

        ssh_host_ecdsa_key_file = \
            host.file('/etc/ssh/ssh_host_ecdsa_key')
        ssh_host_ecdsa_key = \
            ssh_host_ecdsa_key_file.content_string.strip()

        assert takel_ssh_host_ecdsa_key == ssh_host_ecdsa_key


def test_takel_ssh_hostkeys_public_ecdsa_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_ecdsa_key_pub' in testvars:
        takel_ssh_host_ecdsa_key_pub = \
            testvars['takel_ssh_host_ecdsa_key_pub']

        ssh_host_ecdsa_key_pub_file = \
            host.file('/etc/ssh/ssh_host_ecdsa_key.pub')
        ssh_host_ecdsa_key_pub = \
            ssh_host_ecdsa_key_pub_file.content_string.strip()

        assert takel_ssh_host_ecdsa_key_pub == ssh_host_ecdsa_key_pub


def test_takel_ssh_hostkeys_private_ed25519_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_ed25519_key' in testvars:
        takel_ssh_host_ed25519_key = \
            testvars['takel_ssh_host_ed25519_key']

        ssh_host_ed25519_key_file = \
            host.file('/etc/ssh/ssh_host_ed25519_key')
        ssh_host_ed25519_key = \
            ssh_host_ed25519_key_file.content_string.strip()

        assert takel_ssh_host_ed25519_key == ssh_host_ed25519_key


def test_takel_ssh_hostkeys_public_ed25519_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_ed25519_key_pub' in testvars:
        takel_ssh_host_ed25519_key_pub = \
            testvars['takel_ssh_host_ed25519_key_pub']

        ssh_host_ed25519_key_pub_file = \
            host.file('/etc/ssh/ssh_host_ed25519_key.pub')
        ssh_host_ed25519_key_pub = \
            ssh_host_ed25519_key_pub_file.content_string.strip()

        assert takel_ssh_host_ed25519_key_pub == ssh_host_ed25519_key_pub


def test_takel_ssh_hostkeys_private_rsa_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_rsa_key' in testvars:
        takel_ssh_host_rsa_key = \
            testvars['takel_ssh_host_rsa_key']

        ssh_host_rsa_key_file = \
            host.file('/etc/ssh/ssh_host_rsa_key')
        ssh_host_rsa_key = \
            ssh_host_rsa_key_file.content_string.strip()

        assert takel_ssh_host_rsa_key == ssh_host_rsa_key


def test_takel_ssh_hostkeys_public_rsa_sshd_hostkey(host, testvars):
    if 'takel_ssh_host_rsa_key_pub' in testvars:
        takel_ssh_host_rsa_key_pub = \
            testvars['takel_ssh_host_rsa_key_pub']

        ssh_host_rsa_key_pub_file = \
            host.file('/etc/ssh/ssh_host_rsa_key.pub')
        ssh_host_rsa_key_pub = \
            ssh_host_rsa_key_pub_file.content_string.strip()

        assert takel_ssh_host_rsa_key_pub == ssh_host_rsa_key_pub

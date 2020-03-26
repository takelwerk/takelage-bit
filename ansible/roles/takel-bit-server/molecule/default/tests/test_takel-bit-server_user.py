import testaid

testinfra_hosts = testaid.hosts()


def test_takel_bit_server_user(host, testvars):
    bit_username = testvars['takel_bit_server_bit_user']
    authorized_keys_file = '/home/' + bit_username + '/.ssh/authorized_keys'
    for key in testvars['takel_bit_server_sshpubkeys_custom']:
        assert key in host.file(authorized_keys_file).content_string

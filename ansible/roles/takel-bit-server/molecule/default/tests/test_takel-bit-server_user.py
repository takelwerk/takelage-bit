import testaid

testinfra_hosts = testaid.hosts()


def test_takel_bit_server_group(host, testvars):
    bit_group_name = testvars['takel_bit_server_bit_group']
    bit_group_gid = testvars['takel_bit_server_bit_gid']
    bit_group = host.group(bit_group_name)

    assert bit_group.exists
    assert bit_group.gid == bit_group_gid


def test_takel_bit_server_ssh(host, testvars):
    bit_username = testvars['takel_bit_server_bit_user']
    authorized_keys_file = '/home/' + bit_username + '/.ssh/authorized_keys'

    for key in testvars['takel_bit_server_sshpubkeys_custom']:
        assert key in host.file(authorized_keys_file).content_string

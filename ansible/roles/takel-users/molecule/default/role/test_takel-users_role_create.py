import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_users_role_create_password(host):
    command = 'echo "myuserpassword" | sudo -S whoami'
    result = host.check_output(command)

    assert result == 'root'

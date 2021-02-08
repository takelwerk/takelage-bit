import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_users_role_root_password(host):
    inner_command = 'echo "myrootpassword" | su -c whoami'
    command = f"su myuser -c '{inner_command}'"
    result = host.check_output(command)

    assert result == 'root'

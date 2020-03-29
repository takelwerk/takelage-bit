import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_ssh_system_port_open(host, testvars):
    port = testvars['takel_ssh_Port']
    ip = host.check_output('hostname -I').strip()
    molecule_server = host.addr(ip)

    # needs the ping command line tool
    assert molecule_server.is_reachable
    assert not molecule_server.port(21).is_reachable
    assert molecule_server.port(port).is_reachable


def test_takel_ssh_system_key_scan(host, testvars):
    port = testvars['takel_ssh_Port']
    ip = host.check_output('hostname -I').strip()
    keys = host.check_output('ssh-keyscan -p {} {}'.format(port, ip))

    assert 'ssh-ed25519' in keys

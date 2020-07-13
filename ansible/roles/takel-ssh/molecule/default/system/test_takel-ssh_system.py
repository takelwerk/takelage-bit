import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_ssh_system_port_open(host, testvars):
    port = testvars['takel_ssh_Port']
    molecule_server = host.addr(testvars['inventory_hostname'])

    # needs the ping command line tool
    assert molecule_server.is_reachable
    assert not molecule_server.port(21).is_reachable
    assert molecule_server.port(port).is_reachable


def test_takel_ssh_system_key_scan(host, testvars):
    port = testvars['takel_ssh_Port']
    ip = testvars['ansible_hostname']
    keys = host.check_output(f'ssh-keyscan -p {port} {ip}')

    assert 'ssh-ed25519' in keys
    assert 'ssh-rsa' in keys

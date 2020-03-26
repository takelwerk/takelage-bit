import testaid

testinfra_hosts = testaid.hosts()


def test_takel_bit_server_configure(host, testvars):
    repo_dir = testvars['takel_bit_server_repo_dir']

    assert host.file(repo_dir).is_directory

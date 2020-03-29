import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_bit_server_configure(host, testvars):
    if 'takel_gcsfuse_gcs_bucket_key' not in testvars:
        repo_dir = testvars['takel_bit_server_repo_dir']
        dir = host.file(repo_dir)
        assert dir.exists
        assert dir.is_directory
        assert dir.user == testvars['takel_bit_server_bit_user']
        assert dir.group == testvars['takel_bit_server_bit_group']
        assert dir.mode == 0o755

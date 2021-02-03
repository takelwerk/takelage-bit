import takeltest
from pathlib import Path

testinfra_hosts = takeltest.hosts()


def test_takel_gcsfs_system_bin_path(host, testvars):
    # https://github.com/GoogleCloudPlatform
    # /gcsfuse/blob/master/tools/mount_gcsfuse/find.go
    # HACK(jacobsa): Since mount(8) appears to call its helpers with $PATH
    # unset, I can find no better way to do this than searching a hard-coded
    # list of candidates. However, include as a candidate the $PATH-relative
    # version in case we are being called in a context with $PATH set,
    # such as a test.
    if 'takel_gcsfuse_gcs_bucket_key' in testvars:
        valid_bin_paths = [Path('/usr/bin'), Path('/usr/local/bin')]
        bin_path = host.check_output('which gcsfuse')

        assert Path(bin_path).parents[0] in valid_bin_paths


def test_takel_gcsfs_system_called_by_mount(host, testvars):
    if 'takel_gcsfuse_gcs_bucket_key' in testvars:
        result = host.run('mount -a')

        assert "findGcsfuse: Can't find a usable executable." not in result.stderr

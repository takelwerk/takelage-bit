import pytest
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_gcsfuse_install_deb_packages_installed(host, testvars):
    if 'takel_gcsfuse_gcs_bucket_key' not in testvars:
        pytest.skip('takel_gcsfuse_gcs_bucket_key')

    install_packages = testvars['takel_gcsfuse_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed

import testaid

testinfra_hosts = testaid.hosts()


def test_takel_bit_client_install_packages_installed(host, testvars):
    takel_gpg_install_packages = \
        testvars['takel_bit_client_deb_install_packages']

    for package in takel_gpg_install_packages:
        rpm = host.package(package)

        assert rpm.is_installed


def test_takel_bit_client_install_bit_installed(host, testvars):
    takel_bit_client_bin = testvars['takel_bit_client_bin']

    assert host.file(takel_bit_client_bin).is_file

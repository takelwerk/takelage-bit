import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_users_create_user(host, testvars):
    takel_users_userdata = testvars['takel_users_userdata']
    takel_users_users = testvars['takel_users_users']

    for takel_users_user in takel_users_users:
        userdata = takel_users_userdata[takel_users_user]
        user = host.user(takel_users_user)

        assert takel_users_user == user.group
        if 'id' in userdata.keys():
            assert userdata['id'] == user.uid
            assert userdata['id'] == user.uid
        if 'password' in userdata.keys():
            assert userdata['password'] == user.password
        if 'comment' in userdata.keys():
            assert userdata['comment'] == user.gecos
        if 'groups' in userdata.keys():
            user_groups = user.groups
            user_groups.sort()
            userdata_groups = [takel_users_user] + userdata['groups']
            userdata_groups.sort()
            assert userdata_groups == user_groups

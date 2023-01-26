import pytest

from Task_1.script_1 import Member, Moderator, Admin
import Task_1.script_2 as sc_2

params_me = {
        "name": "Alex",
        "surname": "Member",
        "age": "29",
        "join_date": "2023:01:01",
    }

params_mo = {
        "name": "Adam",
        "surname": "Member",
        "age": "29",
        "join_date": "2023:02:01",
        "badge": "star",
    }

changed = {
    "newname": "Newname",
    "newsurname": "Newchanged",
    "newage": "99",
    "newlevel": "3",
    "newbadge": "glow"
}

perm_data = {
        "member": "Member",
        "moderator": "Moderator",
        "admin": "Admin",
        "post_data": "post_data",
        "article_id": "44",
        "update_data": "update_data",
        "group_id": "55",
        "level1": 1,
        "level3": 3,
    }


def test_create_member():
    member = Member(**params_me)
    assert member.name == params_me['name']
    assert member.surname == params_me['surname']
    assert member.age == params_me['age']
    assert member.get_join_date() == params_me['join_date']
    assert isinstance(member.get_user_id(), int)
    assert member.full_name == f"{params_me['name']} {params_me['surname']}"


def test_create_moderator():
    moderator = Moderator(**params_mo)
    assert moderator.name == params_mo['name']
    assert moderator.surname == params_mo['surname']
    assert moderator.age == params_mo['age']
    assert moderator.get_join_date() == params_mo['join_date']
    assert moderator.badge == params_mo["badge"]
    assert isinstance(moderator.get_user_id(), int)
    assert moderator.full_name == f"{params_mo['name']} {params_mo['surname']}"


def test_create_admin():
    admin = Admin(**params_mo)
    admin2 = Admin(**params_mo)
    assert admin.name == params_mo['name']
    assert admin.surname == params_mo['surname']
    assert admin.age == params_mo['age']
    assert admin.get_join_date() == params_mo['join_date']
    assert admin.badge == params_mo["badge"]
    assert admin.level == 1
    assert isinstance(admin.get_user_id(), int)
    assert admin.full_name == f"{params_mo['name']} {params_mo['surname']}"
    assert admin.get_user_id() != admin2.get_user_id()


def test_change_atr_me():
    member = Member(**params_me)
    member.set_name(changed["newname"])
    assert member.name == changed["newname"]
    member.set_surname(changed["newsurname"])
    assert member.surname == changed["newsurname"]
    member.set_age(changed["newage"])
    assert member.age == changed["newage"]

    moderator = Moderator(**params_mo)
    moderator.set_name(changed["newname"])
    assert moderator.name == changed["newname"]
    moderator.set_surname(changed["newsurname"])
    assert moderator.surname == changed["newsurname"]
    moderator.set_age(changed["newage"])
    assert moderator.age == changed["newage"]
    moderator.set_badge(changed['newbadge'])
    assert moderator.badge == changed['newbadge']

    admin = Admin(**params_mo)
    admin.set_name(changed["newname"])
    assert admin.name == changed["newname"]
    admin.set_surname(changed["newsurname"])
    assert admin.surname == changed["newsurname"]
    admin.set_age(changed["newage"])
    assert admin.age == changed["newage"]
    admin.set_badge(changed['newbadge'])
    assert admin.badge == changed['newbadge']
    admin.set_level(changed['newlevel'])
    assert admin.level == changed['newlevel']


def test_permission():
    assert sc_2.set_like_to_article(perm_data['member'], perm_data['post_data']) is True
    assert sc_2.share_article(perm_data['member'], perm_data['article_id']) is True
    with pytest.raises(sc_2.NoAccess):
        sc_2.update_article(perm_data['member'], perm_data['update_data'])
    with pytest.raises(sc_2.NoAccess):
        sc_2.create_article(perm_data['member'], perm_data['post_data'])
    with pytest.raises(sc_2.NoAccess):
        sc_2.delete_article(perm_data['member'], perm_data['article_id'])
    with pytest.raises(sc_2.NoAccess):
        sc_2.delete_group(perm_data['member'], perm_data['group_id'], perm_data['level3'])

    assert sc_2.set_like_to_article(perm_data['moderator'], perm_data['post_data']) is True
    assert sc_2.share_article(perm_data['moderator'], perm_data['article_id']) is True
    assert sc_2.update_article(perm_data['moderator'], perm_data['update_data']) is True
    assert sc_2.create_article(perm_data['moderator'], perm_data['post_data']) is True
    with pytest.raises(sc_2.NoAccess):
        sc_2.delete_article(perm_data['moderator'], perm_data['article_id'])
    with pytest.raises(sc_2.NoAccess):
        sc_2.delete_group(perm_data['moderator'], perm_data['group_id'], perm_data['level3'])

    assert sc_2.set_like_to_article(perm_data['admin'], perm_data['post_data']) is True
    assert sc_2.share_article(perm_data['admin'], perm_data['article_id']) is True
    assert sc_2.update_article(perm_data['admin'], perm_data['update_data']) is True
    assert sc_2.create_article(perm_data['admin'], perm_data['post_data']) is True
    assert sc_2.delete_article(perm_data['admin'], perm_data['article_id']) is True
    assert sc_2.delete_group(perm_data['admin'], perm_data['group_id'], perm_data['level3']) is True
    with pytest.raises(sc_2.NoAccess):
        sc_2.delete_group(perm_data['moderator'], perm_data['group_id'], perm_data['level1'])

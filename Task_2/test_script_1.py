from unittest import TestCase

import Task_1.script_1 as sc_1
import Task_1.script_2 as sc_2


class TestCreateUser(TestCase):
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

    def setUp(self) -> None:
        self.member_1 = sc_1.Member(**self.params_me)
        self.moderator_1 = sc_1.Moderator(**self.params_mo)
        self.admin_1 = sc_1.Admin(**self.params_mo)

    def test_create_member(self):
        self.assertEqual(self.member_1.name, self.params_me["name"])
        self.assertEqual(self.member_1.surname, self.params_me["surname"])
        self.assertEqual(self.member_1.age, self.params_me["age"])
        self.assertEqual(self.member_1.get_join_date(), self.params_me["join_date"])
        self.assertIsInstance(self.member_1.get_user_id(), int)
        self.assertEqual(self.member_1.full_name, f"{self.params_me['name']} {self.params_me['surname']}")

    def test_create_moderator(self):
        self.assertEqual(self.moderator_1.name, self.params_mo["name"])
        self.assertEqual(self.moderator_1.surname, self.params_mo["surname"])
        self.assertEqual(self.moderator_1.age, self.params_mo["age"])
        self.assertEqual(self.moderator_1.get_join_date(), self.params_mo["join_date"])
        self.assertEqual(self.moderator_1.badge, self.params_mo["badge"])
        self.assertIsInstance(self.moderator_1.get_user_id(), int)
        self.assertEqual(self.moderator_1.full_name, f"{self.params_mo['name']} {self.params_mo['surname']}")

    def test_create_admin(self):
        self.assertEqual(self.admin_1.name, self.params_mo["name"])
        self.assertEqual(self.admin_1.surname, self.params_mo["surname"])
        self.assertEqual(self.admin_1.age, self.params_mo["age"])
        self.assertEqual(self.admin_1.get_join_date(), self.params_mo["join_date"])
        self.assertEqual(self.admin_1.badge, self.params_mo["badge"])
        self.assertEqual(self.admin_1.level, 1)
        self.assertIsInstance(self.admin_1.get_user_id(), int)
        self.assertEqual(self.admin_1.full_name, f"{self.params_mo['name']} {self.params_mo['surname']}")
        admin_2 = sc_1.Admin(**self.params_mo)
        admin_3 = sc_1.Admin(**self.params_mo)
        self.assertIsInstance(admin_2.get_user_id(), int)
        self.assertIsInstance(admin_3.get_user_id(), int)
        self.assertNotEqual(admin_2.get_user_id(), admin_3.get_user_id())

    def test_change_atr_me(self):
        self.member_1.set_name(self.changed["newname"])
        self.assertEqual(self.member_1.name, self.changed["newname"])
        self.member_1.set_surname(self.changed["newsurname"])
        self.assertEqual(self.member_1.surname, self.changed["newsurname"])
        self.member_1.set_age(self.changed['newage'])
        self.assertEqual(self.member_1.age, self.changed['newage'])

        self.moderator_1.set_name(self.changed["newname"])
        self.assertEqual(self.moderator_1.name, self.changed["newname"])
        self.moderator_1.set_surname(self.changed["newsurname"])
        self.assertEqual(self.moderator_1.surname, self.changed["newsurname"])
        self.moderator_1.set_age(self.changed['newage'])
        self.assertEqual(self.moderator_1.age, self.changed['newage'])
        self.moderator_1.set_badge(self.changed['newbadge'])
        self.assertEqual(self.moderator_1.badge, self.changed['newbadge'])

        self.admin_1.set_name(self.changed["newname"])
        self.assertEqual(self.admin_1.name, self.changed["newname"])
        self.admin_1.set_surname(self.changed["newsurname"])
        self.assertEqual(self.admin_1.surname, self.changed["newsurname"])
        self.admin_1.set_age(self.changed['newage'])
        self.assertEqual(self.admin_1.age, self.changed['newage'])
        self.admin_1.set_badge(self.changed['newbadge'])
        self.assertEqual(self.admin_1.badge, self.changed['newbadge'])
        self.admin_1.set_level(self.changed['newlevel'])
        self.assertEqual(self.admin_1.level, self.changed['newlevel'])

    def test_permission(self):
        self.assertTrue(sc_2.set_like_to_article(self.member_1, self.perm_data['post_data']))
        self.assertTrue(sc_2.share_article(self.member_1, self.perm_data['article_id']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.update_article(self.member_1, self.perm_data['update_data']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.create_article(self.member_1, self.perm_data['post_data']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.delete_article(self.member_1, self.perm_data['article_id']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.delete_group(self.member_1, self.perm_data['group_id'],
                                              self.perm_data['level3']))

        self.assertTrue(sc_2.set_like_to_article(self.moderator_1, self.perm_data['post_data']))
        self.assertTrue(sc_2.share_article(self.moderator_1, self.perm_data['article_id']))
        self.assertTrue(sc_2.update_article(self.moderator_1, self.perm_data['update_data']))
        self.assertTrue(sc_2.create_article(self.moderator_1, self.perm_data['post_data']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.delete_article(self.moderator_1, self.perm_data['article_id']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.delete_group(self.moderator_1, self.perm_data['group_id'],
                                              self.perm_data['level3']))

        self.assertTrue(sc_2.set_like_to_article(self.admin_1, self.perm_data['post_data']))
        self.assertTrue(sc_2.share_article(self.admin_1, self.perm_data['article_id']))
        self.assertTrue(sc_2.update_article(self.admin_1, self.perm_data['update_data']))
        self.assertTrue(sc_2.create_article(self.admin_1, self.perm_data['post_data']))
        self.assertTrue(sc_2.delete_article(self.admin_1, self.perm_data['article_id']))
        self.assertTrue(sc_2.delete_group(self.admin_1, self.perm_data['group_id'],
                                          self.perm_data['level3']))
        with self.assertRaises(sc_2.NoAccess):
            self.assertTrue(sc_2.delete_group(self.perm_data['admin'], self.perm_data['group_id'],
                                              self.perm_data['level1']))

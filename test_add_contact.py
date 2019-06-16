# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact_hanna(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Hanna", lastname="Semerenko", nickname="magika", company="test", email="anna.semerenko@djangostars.com", bday="13", bmonth="April", byear="1979"))
        self.app.logout()

    def test_add_contact_masha(self):
        self.app.login(username="admin", password="secret")
        self.app.create_contact(Contact(firstname="Mary", lastname="Ilyina", nickname="masha", company="test", email="mary.ilyina@djangostars.com", bday="14", bmonth="July", byear="1998"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
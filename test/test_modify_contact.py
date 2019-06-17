# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Hanna1", lastname="Semerenko1", nickname="magika1", company="test1", email="anna.semerenko1@djangostars.com", bday="14", bmonth="May", byear="1978"))
    app.session.logout()
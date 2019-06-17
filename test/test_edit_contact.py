# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_hanna(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Hanna1", lastname="Semerenko1", nickname="magika1", company="test1", email="anna.semerenko1@djangostars.com", bday="14", bmonth="May", byear="1978"))
    app.session.logout()
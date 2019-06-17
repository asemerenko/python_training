# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Anna"))
    app.session.logout()

def test_modify_contact_bday(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(bday="31"))
    app.session.logout()
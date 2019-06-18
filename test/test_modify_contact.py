# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact_name(app):
    app.contact.modify_first_contact(Contact(firstname="Anna"))

def test_modify_contact_bday(app):
    app.contact.modify_first_contact(Contact(bday="31"))

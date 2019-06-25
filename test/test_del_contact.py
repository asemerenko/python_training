# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Hanna", lastname="Martynenko"))
    old_contacts = app.contact.add_contact_list()
    app.contact.delete_first_contact()
    assert len(old_contacts)-1 == app.contact.count()
    new_contacts = app.contact.add_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


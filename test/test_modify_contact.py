# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Hanna"))
    old_contacts = app.contact.add_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Anna")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.add_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_bday(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="Hanna"))
#    old_contacts = app.contact.add_contact_list()
#    app.contact.modify_first_contact(Contact(bday="31"))
#    new_contacts = app.contact.add_contact_list()
#    assert len(old_contacts) == len(new_contacts)



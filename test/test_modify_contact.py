# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_contact_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Hanna"))
    old_contacts = db.get_contact_list()
    contact_old_data = random.choice(old_contacts)
    old_contacts.remove(contact_old_data)
    contact_new_data = Contact(firstname="Anna13", id=contact_old_data.id)
    app.contact.modify_contact_by_id(contact_old_data.id, contact_new_data)
    old_contacts.append(contact_new_data)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())
        assert sorted(list(map(clean, new_contacts)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                       key=Contact.id_or_max)

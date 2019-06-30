# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact_hanna(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(
        firstname="Hanna",
        lastname="Semerenko",
        nickname="magika",
        company="test_company",
        homephone="4444444",
        mobilephone="0974472212",
        workphone="5555555",
        fax="0969986635",
        secondaryphone="3244225",
        email="anna.semerenko@djangostars.com",
        bday="13",
        bmonth="April",
        byear="1979"
    )
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact_masha(app):
#    old_contacts = app.contact.add_contact_list()
#    contact = Contact(
#        firstname="Mary",
#        lastname="Ilyina",
#        nickname="masha",
#        company="test",
#        email="mary.ilyina@djangostars.com",
#        bday="14",
#        bmonth="July",
#        byear="1998"
#    )
#    app.contact.create(contact)
#    new_contacts = app.contact.add_contact_list()
#    assert len(old_contacts)+1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

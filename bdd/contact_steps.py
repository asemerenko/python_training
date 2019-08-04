from pytest_bdd import given, when, then
from fixture.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname> and <address>')
def new_contact(firstname, lastname, address):
    return Contact(firstname=firstname, lastname=lastname, address=address)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())

        assert sorted(list(map(clean, new_contacts)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                       key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Hanna", lastname="Martynenko"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, app, non_empty_contact_list, random_contact, check_ui):
    old_contacts = non_empty_contact_list
    assert len(non_empty_contact_list) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())

        assert sorted(list(map(clean, new_contacts)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                       key=Contact.id_or_max)


@given('a modified contact with <firstname>, <lastname> and <address>')
def contact_for_modify(firstname, lastname, address, random_contact):
    return Contact(firstname=firstname, lastname=lastname, address=address, id=random_contact.id)


@when('I modify the contact in the list')
def modify_group(app, random_contact, contact_for_modify):
    app.contact.modify_contact_by_id(random_contact.id, contact_for_modify)


@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, random_contact, contact_for_modify, check_ui):
    old_contacts = non_empty_contact_list
    old_contacts.remove(random_contact)
    old_contacts.append(contact_for_modify)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact_cl):
            return Contact(id=contact_cl.id, firstname=contact_cl.firstname.strip())

        assert sorted(list(map(clean, new_contacts)), key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                                       key=Contact.id_or_max)

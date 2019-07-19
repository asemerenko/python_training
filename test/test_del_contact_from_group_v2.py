from model.group import Group
from model.contact import Contact
import random


def test_del_contact_from_group(app, db, orm):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="New_group_for_test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Firstname_test"))
    id_group_list_with_contacts = db.get_group_list_with_contacts()
    if len(id_group_list_with_contacts) == 0:
        id_contact = random.choice(db.get_contact_list()).id
        id_group = random.choice(db.get_group_list()).id
        app.contact.add_contact_in_group(id_group, id_contact)
        id_group_list_with_contacts.append(id_group)
    id_group = random.choice(id_group_list_with_contacts)
    id_contact = random.choice(orm.get_contacts_in_group(Group(id=id_group))).id
    app.contact.dell_contact_from_group(id_group, id_contact)
    assert db.get_contact_by_id(id_contact) not in orm.get_contacts_in_group(Group(id=id_group))

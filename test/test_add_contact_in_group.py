from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random


dbORM = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_test"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Firstname_test"))
    groups_list = db.get_group_list()
    id_group = random.choice(groups_list).id
    contacts_list = db.get_contact_list()
    id_contact = random.choice(contacts_list).id
    app.contact.add_contact_in_group(id_group, id_contact)
    assert db.get_contact_by_id(id_contact) in dbORM.get_contacts_in_group(Group(id=id_group))

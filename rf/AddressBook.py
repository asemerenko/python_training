from fixture.application import Application
import json
import os.path
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'],
                                   user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def new_group_for_modify(self, name, header, footer, id):
        return Group(name=name, header=header, footer=footer, id=id)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def get_group_id(self, group):
        return group.id

    def get_contact_id(self, contact):
        return contact.id

    def modify_group(self, group1, group2):
        self.fixture.group.modify_group_by_id(group1.id, group2)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def verify_group_list_is_not_empty(self, list1):
        if len(list1) == 0:
            self.fixture.group.create(Group(name="New_group"))

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self, firstname, lastname, address):
        return Contact(firstname=firstname, lastname=lastname, address=address)

    def new_contact_for_modify(self, firstname, lastname, address, id):
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def verify_contact_list_is_not_empty(self, list1):
        if len(list1) == 0:
            self.fixture.contact.create(Contact(firstname="firstname4", lastname="lastname4", address="adress4"))

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def modify_contact(self, contact1, contact2):
        self.fixture.contact.modify_contact_by_id(contact1.id, contact2)


import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_group_by_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_id='%s'"
                           % id_in)
            (id, name, header, footer) = cursor.fetchone()
            group_return = Group(id=str(id), name=name, header=header, footer=footer)
        finally:
            cursor.close()
        return group_return

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, middlename, nickname, company, "
                           "title, address FROM addressbook WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, middlename, nickname, company, title, address) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                    nickname=nickname, company=company, title=title, address=address))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, middlename, nickname, company, "
                           "title, address, email, email2, email3, home, mobile, work, phone2 "
                           "FROM addressbook WHERE deprecated='0000-00-00 00:00:00' and id='%s'" % id_in)
            (id, firstname, lastname, middlename, nickname, company, title,
             address, email, email2, email3, home, mobile, work, phone2) = cursor.fetchone()
            contact_return = Contact(id=str(id), firstname=firstname, lastname=lastname, middlename=middlename,
                                     nickname=nickname, company=company, title=title, address=address, email=email,
                                     email2=email2, email3=email3, homephone=home, mobilephone=mobile, workphone=work,
                                     secondaryphone=phone2)
        finally:
            cursor.close()
        return contact_return

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT DISTINCT group_id FROM address_in_groups")
            for row in cursor:
                (id,) = row
                list.append(str(id))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

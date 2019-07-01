from model.contact import Contact
from random import randrange
import re


def test_comparison_contact_on_home_and_edit_page(app):
    if app.contact.count() == 0:
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
            email="test1@djangostars.com",
            email2="test2@djangostars.com",
            email3="test3@djangostars.com",
            address="Address",
            bday="13",
            bmonth="April",
            byear="1979"
        )
        app.contact.create(contact)
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.secondaryphone]))))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

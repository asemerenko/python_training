from model.contact import Contact


def test_comparison_contact_on_home_page_and_in_db(app, db):
    if len(db.get_contact_list()) == 0:
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
    for contact in list_contacts:
        assert contact.firstname == db.get_contact_by_id(contact.id).firstname
        assert contact.lastname == db.get_contact_by_id(contact.id).lastname
        assert contact.address == db.get_contact_by_id(contact.id).address
        assert contact.all_emails_from_home_page == merge_emails(db.get_contact_by_id(contact.id))
        assert contact.all_phones_from_home_page == merge_phones(db.get_contact_by_id(contact.id))


def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                             contact.workphone, contact.secondaryphone])))

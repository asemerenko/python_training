# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_hanna(app):
    app.contact.create(Contact(firstname="Hanna", lastname="Semerenko", nickname="magika", company="test", email="anna.semerenko@djangostars.com", bday="13", bmonth="April", byear="1979"))


def test_add_contact_masha(app):
    app.contact.create(Contact(firstname="Mary", lastname="Ilyina", nickname="masha", company="test", email="mary.ilyina@djangostars.com", bday="14", bmonth="July", byear="1998"))

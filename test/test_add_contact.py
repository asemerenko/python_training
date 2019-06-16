# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact_hanna(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Hanna", lastname="Semerenko", nickname="magika", company="test", email="anna.semerenko@djangostars.com", bday="13", bmonth="April", byear="1979"))
    app.session.logout()

def test_add_contact_masha(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Mary", lastname="Ilyina", nickname="masha", company="test", email="mary.ilyina@djangostars.com", bday="14", bmonth="July", byear="1998"))
    app.session.logout()
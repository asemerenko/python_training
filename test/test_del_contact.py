# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_hanna(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()
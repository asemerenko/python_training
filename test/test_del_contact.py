# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact_hanna(app):
    app.contact.delete_first_contact()

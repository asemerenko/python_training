# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_delete"))
    app.group.delete_first_group()

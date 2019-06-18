# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_modify"))
    app.group.modify_first_group(Group(name="New group name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="New_group_for_modify"))
    app.group.modify_first_group(Group(header="New header"))

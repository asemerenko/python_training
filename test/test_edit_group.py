# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Group_name_Hanna", header="Group_header", footer="Group_footer"))
    app.session.logout()
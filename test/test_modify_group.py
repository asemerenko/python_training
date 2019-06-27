# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_modify"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="New_group_for_modify"))
#    old_groups = app.group.add_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.add_group_list()
#    assert len(old_groups) == len(new_groups)

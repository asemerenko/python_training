# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_modify"))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).id
    group_old_data = db.get_group_by_id(id)
    old_groups.remove(group_old_data)
    group_new_data = Group(name="New group name1", id=id)
    app.group.modify_group_by_id(id, group_new_data)
    old_groups.append(group_new_data)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group_cl):
            return Group(id=group_cl.id, name=group_cl.name.strip())

        assert sorted(list(map(clean, new_groups)), key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                                   key=Group.id_or_max)

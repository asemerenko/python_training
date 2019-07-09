# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


bday_list = list(map(lambda x: str(x), range(1, 31)))
bmonth_list = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
byear_list = list(map(lambda x: str(x), range(1900, 2019)))


testdata = [
    Contact(
        firstname="",
        lastname="",
        nickname="",
        company="",
        homephone="",
        mobilephone="",
        workphone="",
        fax="",
        secondaryphone="",
        email="",
        email2="",
        email3="",
        address="",
        bday=random.choice(bday_list),
        bmonth=random.choice(bmonth_list),
        byear=random.choice(byear_list))] + [
    Contact(
        firstname=random_string("firstname", 10),
        lastname=random_string("lastname", 20),
        nickname=random_string("nickname", 10),
        company=random_string("company", 10),
        homephone=random_string("homephone", 10),
        mobilephone=random_string("mobilephone", 10),
        workphone=random_string("workphone", 10),
        fax=random_string("fax", 10),
        secondaryphone=random_string("secondaryphone", 10),
        email=random_string("email", 10),
        email2=random_string("email2", 10),
        email3=random_string("email3", 10),
        address=random_string("address", 10),
        bday=random.choice(bday_list),
        bmonth=random.choice(bmonth_list),
        byear=random.choice(byear_list)
    )
    for i in range(5)
]

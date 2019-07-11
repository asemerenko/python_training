# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))

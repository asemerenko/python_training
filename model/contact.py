from sys import maxsize


class Contact:

    def __init__(self,
                 firstname=None,
                 lastname=None,
                 middlename=None,
                 nickname=None,
                 company=None,
                 title=None,
                 address=None,
                 all_emails_from_home_page=None,
                 all_phones_from_home_page=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 secondaryaddress=None,
                 secondaryphone=None,
                 notes=None,
                 id=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.middlename = middlename
        self.nickname = nickname
        self.company = company
        self.title = title
        self.address = address
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.secondaryaddress = secondaryaddress
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id

    def __eq__(self, other):
        return self.firstname == other.firstname and \
               (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and \
               (self.id is None or other.id is None or self.id == other.id)

    def __repr__(self):
        return "Contact(%s, %s, %s)" % (self.firstname, self.lastname, self.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

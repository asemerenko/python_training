from sys import maxsize


class Contact:

    def __init__(self,
                 firstname=None,
                 lastname=None,
                 nickname=None,
                 company=None,
                 email=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 id=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.email = email
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
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

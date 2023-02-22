from options import get_id_by_citizenship, get_id_family_member

MAX_WAITING_TIME = 10000

class UserConfig:
    def __init__(self, citizenship, number_applicants, family_member, family_citizenship):
        self.citizenship = citizenship
        self.citizenship_id = get_id_by_citizenship(citizenship)
        self.family_member = get_id_family_member(family_member)
        self.number_applicants = number_applicants
        self.family_citizenship = family_citizenship
        self.family_citizenship_id = get_id_by_citizenship(family_citizenship)
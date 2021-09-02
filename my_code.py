import datetime

from users.models import BaseUser
from users.models import Profile

users = BaseUser.objects.filter(profile=None)
for user in users:
    Profile.objects.create(user=user)


class Person:
    def __init__(self):
        self.name = 'Tony'
        self.age = 25
        self.is_work = True
        self.day_of_birth = datetime.date(14, 1, 1992)


obj = Person()
print(obj.age)

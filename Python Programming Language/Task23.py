# Task 23


class User:

    _password = "password"

    def get_password(self):
        return self._password

class ActiveUser(User):

    def get_password(self):
        return "********"

active =ActiveUser()
print(active.get_password())
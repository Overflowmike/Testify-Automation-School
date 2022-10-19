# Task 22

class Hunt:
    _weapon = "Assault Rifle"
    _assaultRifle = "Not Available"

    def get_weapon(self):
        return  self._assaultRifle

    def __int__(self):
        self._weapon

hunt = Hunt()
print(hunt.get_weapon())

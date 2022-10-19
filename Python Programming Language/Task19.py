# Task 19



class Human:
    group = "Mammal"
    leg_count = 4
    name = "Mike"
    can_walk = True
    get_description = "This is human"

    def _init_(self, get_description):
        self.get_description = "This is human"

    def set_leg_count(self, count):
         self.leg_count = count


male = Human()
print("Human:", male.get_description)


human = Human()
human.set_leg_count(4)
print("\nHuman:", human.name, human.leg_count)
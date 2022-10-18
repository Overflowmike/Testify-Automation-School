# Task 21


class Human:
    group = "Mammal"
    leg_count = 4
    can_walk = True
    get_gender = "Unknown"
    gender = "man"
    count = 4
    fe_gender = "woman"
    fe_count = 3


def print_human_info(self):
    print("\nHuman{", self.get_gender, ",", self.leg_count, self.fe_gender, self.fe_count + "}")


class Man(Human):

    def __int__(self, get_gender, leg_count, count="4", gender="Man", fe_gender="Female", fe_count=3):
        self.get_gender = gender
        self.leg_count = count

    def print_human_info(self):
        pass


class Woman(Human):

    def print_human_info(self):
        pass

    get_gender = "Female"
    fe_count = 3

human = Human()

man = Human()
print("\nMan:", human.gender)

woman = Human()
print("\nWoman:", human.fe_gender)

man = Man()
man.print_human_info()

woman = Woman()
woman.print_human_info()

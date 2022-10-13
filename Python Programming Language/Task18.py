# Task 18


class Human:

    group = "Male"
    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name

Michael = Human("Michael")
Festus = Human("Festus")

print(Michael.name)
print(Festus.name)

print(Michael.group)
print(Festus.group)
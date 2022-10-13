# Task 18

class Human:

    group = "Male"
    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name

Michael = Human("Michael")

print(Michael.name)
print(Michael.group)


print(Michael.leg_count)
print(Michael.can_walk)
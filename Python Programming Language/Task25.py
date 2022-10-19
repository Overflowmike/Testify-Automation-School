# Task 25


import print_name as print_name


class Utilities:

    @staticmethod
    def print_name(self):
        return "Electricity"

    @staticmethod
    def print_name2(self):
        return "Water Board"

    @staticmethod
    def print_name3(self):
        return "Gas"

printName = staticmethod(print_name)
print("Utility1 =", Utilities.print_name("Electricity"))
print("Utility2 =", Utilities.print_name2("Water Board"))
print("Utility3 =", Utilities.print_name3("Gas"))

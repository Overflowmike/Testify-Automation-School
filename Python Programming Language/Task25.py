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

    @staticmethod
    def print_name4(self):
        return "Heater"

printName = staticmethod(print_name)
print("Utility1 =", Utilities.print_name("Electricity"))
print("Utility2 =", Utilities.print_name2("Water Board"))
print("Utility3 =", Utilities.print_name3("Gas"))
print("Utility4 =", Utilities.print_name4("Heater"))

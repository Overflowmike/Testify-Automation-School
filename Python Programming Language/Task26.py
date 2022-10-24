# Task 26 A


class BoysHostel():
    boy1 = "Faraday"
    boy2 = "Lincoln"

    def boy_name(self):
        print("Faraday")

    def girl_name(self):
        print("Unknown")


class GirlsHostel():
    girl1 = "Kristal"
    girl2 = "Michelle"

    def girl_name(self):
        print("Kristal")

    def boy_name(self):
        print("None")

gender = BoysHostel()
gender.boy_name()

gender = GirlsHostel()
gender.girl_name()

print(gender.boy_name() == gender.girl_name())
print(gender.girl_name() != gender.boy_name())


# Task 26 B


num1 = 8

num2 = 19

print(num1 < num2)
print(num2 > num1)
print(num1 > num2)
print(num1 <= num2)
print(num2 >= num1)
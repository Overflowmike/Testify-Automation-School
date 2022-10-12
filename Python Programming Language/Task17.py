# Task 17


# class
class Human:
    name = "Michael"
    group = "Test Automation"
    level = "Level 3"

    def get_name_group_level(self):
        return self.name + ":" + self.group + ":" + self.level

# objects
Michael = Human()
print(Michael.name, Michael.group, Michael.level, Michael.get_name_group_level())
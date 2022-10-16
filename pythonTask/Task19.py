# Task 19
class Human:

    leg_count = 4
    can_walk = True
    def __init__(self, name):
        print('This is python')
        self.name = name

    # instance Method
    def get_description(self):
        print(self.name)


# create object using constructor
human = Human("leg_count")
human.get_description()
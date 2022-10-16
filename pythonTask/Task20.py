# Task 20

class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"


human = Human()
print(human.get_gender())


class Man(Human):
    pass


class Woman(Human):
    pass


man1 = Man()
woman1 = Woman()
print(man1.get_gender())
print(woman1.get_gender())

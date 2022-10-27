# Task 21

# Create a class called Human
# Add an attribute leg_count with the value of 4
# Add a method called get_gender() that returns "Unknown" in the Human class
# Create another class called Man that extends Human
# Create another class called Woman that extends Human
# In the class, Man create the method get_gender() which should return "man"
# In the class, Woman create the method get_gender() which should return "woman"
# Instantiate the Man and Woman classes
#Print out the value of get_gender() from the Man and Woman object instances

class Human:
    leg_count = 4

    def get_gender(self):
        return "Unknown"



class Man(Human):

    def get_gender(self):
        return "man"


class Woman(Human):

    def get_gender(self):
        return "Woman"

    def __int__(self, Man, Woman):
        self.Man = Man
        self.Woman = Woman


human = Human()
human.get_gender()

man1 = Man()
print(man1.get_gender())



woman1 = Woman()
print(woman1.get_gender())
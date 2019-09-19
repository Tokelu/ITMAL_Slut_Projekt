# Define a function
def world():
    print("Hello, World!")
# Define a variable
shark = "Sammy"
# Define a class
class Octopus:
    def __init__(self, name, color, age):
        self.color = color
        self.name = name
        self.age = age
		
    def tell_me_about_the_octopus(self):
        print("This octopus is " + self.color + ".") 
        print("This octopus is "+ str(self.age) + " old.")
        print(self.name + " is the octopus's name.")
		
    def __str__(self):
        return "person class"
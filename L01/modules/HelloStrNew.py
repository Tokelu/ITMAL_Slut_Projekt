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
		
    def tell_me_about_the_octopus():
        print("This octopus is " + self.color + ".")
        print(self.name + " is the octopus's name.")
		
	def __str__(self):
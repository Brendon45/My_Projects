#!/usr/bin/python3
# This is a simple Python class program demonstrating class and instance variables, methods, and class methods.

# Define a class named 'Robot'
class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name  # Initialize the instance variable 'name' with the value passed
        print("(Initializing {})".format(self.name))

        # When this robot is created, it adds to the population
        Robot.population += 1

    def die(self):
        """Simulates the robot being destroyed."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1  # Decrease the population count

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


# Create an instance of the 'Robot' class with the name 'R2-D2'
droid1 = Robot("R2-D2")
# Call the 'say_hi' method on the 'Robot' instance to print the greeting
droid1.say_hi()
# Call the class method 'how_many' to print the current population of robots
Robot.how_many()

# Create another instance of the 'Robot' class with the name 'C-3PO'
droid2 = Robot("C-3PO")
# Call the 'say_hi' method on the second 'Robot' instance to print the greeting
droid2.say_hi()
# Call the class method 'how_many' to print the updated population of robots
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
# Call the 'die' method on the first 'Robot' instance to simulate its destruction
droid1.die()
# Call the 'die' method on the second 'Robot' instance to simulate its destruction
droid2.die()

# Call the class method 'how_many' to print the final population of robots
Robot.how_many()
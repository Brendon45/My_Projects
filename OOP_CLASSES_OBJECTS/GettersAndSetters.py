#!/usr/bin/python3
"""The following example shows a class, which has internal attributes, which
can't be accessed from outside. These are the private attributes
self.__potential_physical and self.__potential_psychic. Furthermore, we show
that a property can be deduced from the values of more than one attribute.
The property "condition" of our example returns the condition of the robot in
a descriptive string. The condition depends on the sum of the values of the
psychic and physical conditions of the robot.
"""

class Robot:
    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        """Initializes the Robot with a name, build year, and initial potential
        values for physical and psychic conditions.
        """
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk  # Private attribute
        self.__potential_psychic = lp  # Private attribute

    @property
    def condition(self):
        """Calculates the condition of the robot based on the sum of its
        physical and psychic potentials.
        """
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

# Example usage:
if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)  # Creating a robot instance
    y = Robot("Caliban", 1993, -0.4, 0.3)  # Creating another robot instance

    # Accessing the condition property
    print(x.condition)  # Output: "Seems to be okay!"
    print(y.condition)  # Output: "I feel bad!"
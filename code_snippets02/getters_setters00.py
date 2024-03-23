#!/usr/bin/python3

class Person:
    def __init__(self, age):
        self.age = age  # Set the age using the property setter

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age
        else:
            self.__age = 0

# Create an instance of the Person class with age 10
my_obj = Person(10)

# Access the age attribute of the object using the property getter
print(my_obj.age)  # Output: 0 (since age 10 is less than 18, it's set to 0)

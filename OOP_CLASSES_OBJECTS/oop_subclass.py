#!/usr/bin/python3

# Define a base class named 'SchoolMember'
class SchoolMember:
    '''Represents any school member.'''
    
    def __init__(self, name, age):
        # Initialize the 'name' and 'age' attributes
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        # Print the name and age of the school member
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

# Define a derived class named 'Teacher' which inherits from 'SchoolMember'
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    
    def __init__(self, name, age, salary):
        # Initialize the base class (SchoolMember) part of the object
        SchoolMember.__init__(self, name, age)
        # Initialize the 'salary' attribute
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        # Call the tell method of the base class
        SchoolMember.tell(self)
        # Print the salary of the teacher
        print('Salary: "{:d}"'.format(self.salary))

# Define a derived class named 'Student' which inherits from 'SchoolMember'
class Student(SchoolMember):
    '''Represents a student.'''
    
    def __init__(self, name, age, marks):
        # Initialize the base class (SchoolMember) part of the object
        SchoolMember.__init__(self, name, age)
        # Initialize the 'marks' attribute
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        # Call the tell method of the base class
        SchoolMember.tell(self)
        # Print the marks of the student
        print('Marks: "{:d}"'.format(self.marks))

# Create an instance of the 'Teacher' class
t = Teacher('Mrs. Shoniwa', 40, 30000)
# Create an instance of the 'Student' class
s = Student('Amanda', 25, 75)

# prints a blank line
print()

# Create a list of school members
members = [t, s]
for member in members:
    # Call the tell method for each member in the list
    # This works for both Teachers and Students due to polymorphism
    member.tell()
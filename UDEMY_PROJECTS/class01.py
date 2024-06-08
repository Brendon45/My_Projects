#!/usr/bin/python3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Book: {self.title} by {self.author}"
    
my_book = Book(title="1984", author="George Orwell")  # Corrected author name
my_book2 = Book(title="The Code Book", author="Simon Singh")  # Corrected title capitalization

print(my_book.display_info())
print(my_book2.display_info())

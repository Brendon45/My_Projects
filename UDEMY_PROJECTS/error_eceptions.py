#!/usr/bin/python3

print("Give two numbers and l'll divide them")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0")

    except ValueError:
        print("use numbers only")
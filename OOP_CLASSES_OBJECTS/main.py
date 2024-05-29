#!/usr/bin/python3

from person import Person

def main():
    jane = Person("Jane Doe", 25)
    print(f"{jane}")
    print(repr(jane))

if __name__ == "__main__":
    main()

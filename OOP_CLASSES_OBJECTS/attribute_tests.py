class A:
    def __init__(self):
        self.__priv = "I am private"  # Private attribute
        self._prot = "I am protected"  # Protected attribute
        self.pub = "I am public"  # Public attribute

# Creating an instance of class A
a = A()

# Accessing public attribute
print(a.pub)  # Output: I am public

# Accessing protected attribute
print(a._prot)  # Output: I am protected (though it is not recommended to do so directly)

# Accessing private attribute (This will raise an AttributeError if uncommented)
# print(a.__priv)  # Uncommenting this line will cause an error

# Accessing private attribute using name mangling
print(a._A__priv)  # Output: I am private (accessing private attribute using name mangling)

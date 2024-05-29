#!/usr/bin/python3

from attribute_tests import A
x = A()
print(f'At first: {x.pub}')
x.pub = x.pub + " and my value can be changed"
print(f"Now: {x.pub}")
print(x._prot)
print(x._A__priv)  # Corrected line to access private attribute

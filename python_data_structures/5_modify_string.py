#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

def remove_char(some_string):
  new_string = ""
  removed = "Aa"

  for char in some_string:
    if char in removed:
      char = ""
    new_string += char
  return new_string

result = remove_char(string)
print(result)

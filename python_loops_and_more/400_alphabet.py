#!/usr/bin/python3

for i in range(97, 123):
  if chr(i) == "a" or chr(i) == "q":
    continue
  print(chr(i), end="")

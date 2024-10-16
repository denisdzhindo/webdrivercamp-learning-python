#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]
true_false = []

for number in my_list:
  if number % 2 == 0:
    true_false.append(True)
  else:
    true_false.append(False)
print(my_list)
print(tuple(true_false))

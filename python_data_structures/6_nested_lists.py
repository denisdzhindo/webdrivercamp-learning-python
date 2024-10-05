#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for list_ in matrix:
  for number in list_:
    print(number, end=" ")
  print("")


# unpacking list solution: 

'''for element in matrix:
  print(*element)'''

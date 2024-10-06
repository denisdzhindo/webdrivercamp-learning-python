#!/usr/bin/python3

print(*range(100), sep = ", ")

# solution 2 with var (for practice)
'''numbers = range(100)
result = ""

for index, number in enumerate(numbers):
  result += str(number)
  if index < len(numbers) - 1:
    result += ", "

print(result)'''




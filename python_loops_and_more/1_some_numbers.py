#!/usr/bin/python3

numbers = range(100)
result = ""

for index, number in enumerate(numbers):
  result += str(number)
  if index < len(numbers) - 1:
    result += ", "

print(result)

# solution 2
# print(*range(100), sep = ", ")

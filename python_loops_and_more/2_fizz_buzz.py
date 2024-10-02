#!/usr/bin/python3

def fizz_buzz(number):
  result = ""

  for num in range(1, number + 1):

    if num % 3 == 0 and num % 5 == 0:
      result = result + "FizzBuzz "
    elif num % 5 == 0:
      result += "Buzz "
    elif num % 3 == 0:
      result +="Fizz "
    else:
      result += str(num) +  " "

  return result

final = fizz_buzz(100)
print(final)

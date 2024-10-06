#!/usr/bin/python3

def tuple_addition(first_arg = None, second_arg = None):

  if first_arg == None:
    first_arg = (0, 0)
  if second_arg == None:
    second_arg = (0, 0)
  if first_arg == ():
    first_arg = (0, 0)
  if second_arg == ():
    second_arg = (0, 0)
  if len(first_arg) < 2:
    first_arg = (first_arg[0], 0)
  if len(second_arg) < 2:
    second_arg = (second_arg[0], 0)
  if len(first_arg) > 2:
    first_arg = (first_arg[0], first_arg[1])
  if len(second_arg) > 2:
    second_arg = (second_arg[0], second_arg[1])



  return (first_arg[0] + second_arg[0], first_arg[1] + second_arg[1])

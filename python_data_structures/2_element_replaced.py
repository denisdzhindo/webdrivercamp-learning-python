#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5

def replace(index):
  list_[index] = element_to_replace
  return list_

result = replace(index)
print(result)


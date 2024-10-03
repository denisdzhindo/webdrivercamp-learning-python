#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5


def replace(index):
  copy_ = list_.copy()
  copy_[index] = element_to_replace
  return copy_

result = replace(index)
print(f"Copy:     {result}\nOriginal: {list_}")

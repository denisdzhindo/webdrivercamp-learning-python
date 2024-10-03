#!/usr/bin/python3

list_ = [5, 4, 3, 2, 1]
index = 2

def retrieve(index):

  if index < len(list_) and index >= 0:
    return f"The element retrieved is {list_[index]}"
  else:
    return None

result = retrieve(index)
print(result)


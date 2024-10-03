#!/usr/bin/python3

# solution 1

list_ = [5, 4, 3, 2, 1]

def reverse(list_):

 reversed = []
 count = 1

 while count < len(list_) + 1:
    last = list_[len(list_) - count]
    reversed.append(last)
    count += 1
 return reversed

result = reverse(list_)
print(result)



# solution 2 print(list_[::-1)]


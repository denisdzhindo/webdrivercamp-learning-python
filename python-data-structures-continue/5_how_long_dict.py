#!/usr/bin/python3

# Write a function that returns the number of keys in a dictionary.

def keys_number(d):
 count = 0
 for key in d:
  count += 1
 return count

 # 2nd solution: keys = dict_.keys() return len(list(keys))

if __name__=="__main__":

 dict_ = {"lib": "requests", 1: "Selenium", "lang": "Python", "frame": "Behave"}
 number_of_keys = keys_number(dict_)
 print(f"The dictionary has {number_of_keys} keys")

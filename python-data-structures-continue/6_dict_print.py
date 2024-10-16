#!/usr/bin/python3

# Write a function which prints a dictionary by orderieng keys

def dict_print(dict_):
 for key in sorted(dict_):
     value = dict_[key]
     print(f"{key}: {value}")

if __name__=="__main__":

 dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java", "Python"], "frame": "Behave", "set": set()}
 print(dict_print(dict_))



 

#!/usr/bin/python3

# Write a function that returns a set of all elements present in only one set
# symmetric difference is diff which is not in set for both sets.


def not_common_elements(a, b):
 symmetric_difference = a.symmetric_difference(b)
 return symmetric_difference

if __name__=="__main__":
    
 set_a = {"API", "requests", "Selenium", "Python", "Behave"}
 set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
 elements = not_common_elements(set_a, set_b)
 [print(x) for x in sorted(list(elements))]

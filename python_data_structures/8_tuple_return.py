#!/usr/bin/python3

def tuple_return(list_):
    if len(list_) == 0:
        first_element = None
    else:
        first_element = list_[0]

    return len(list_), first_element



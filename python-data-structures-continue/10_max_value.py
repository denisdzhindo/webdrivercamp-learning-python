#!/usr/bin/python3


def max_value(d):
    max_value = 0
    max_key = ""

    if d == None:
        return None

    for key in d:
        if d[key] > max_value:
            max_value = d[key]
            max_key = key
    return max_key




if __name__=="__main__":
    dict_ = {'Apple': 13, 'Pear': 1, 'Plum': 20, 'Grape': 10}
    max_key = max_value(dict_)
    print(f"Max number - {max_key}")
    max_key = max_value(None)
    print(f"Max number - {max_key}")

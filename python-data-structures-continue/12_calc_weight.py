#!/usr/bin/python3

def calc_weight(list_=[]):

    if len(list_) == 0:
        return 0

    sum_tuple = []
    second = []

    for tup in list_:
        for element in range(len(tup) - 1):
            sum_tuple.append(tup[element] * tup[element + 1])
            second.append(tup[1])

    return sum(sum_tuple) / sum(second)

if __name__=="__main__":
    #list_ = []
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")                  


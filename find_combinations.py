# Determine every digit or possible 
# combination that sums to the target number
# 
# Input: list_of_number, target_number
# Output: Every single digit or combination that the 
#         sum is equal to the target_number

from itertools import combinations

def find_combinations(list_of_number, target_number):
    ret = list()

    for values in list_of_number:
        if values == target_number:
            ret.append([values])

    for x in range(2, len(list_of_number) + 1):
        for values in list(combinations(list_of_number, x)):
            a = list(values)
            b = sum(a)
            if b == target_number:
                ret.append(a)
    print(ret)
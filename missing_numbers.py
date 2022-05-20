# Based on a list of numbers, this code
# will find the max value and list all
# the numbers that didn't appeared on the
# list. From 1 to the max value.  

def missing_numbers(*nums):

    count_dict = dict()
    max_num = 0
    ret = list()

    for n in nums:
        try:
            x = int(n)
            if x > max_num:
                max_num = x
        except:
            return "Error"
            
    for i in range(1, max_num + 1):
        count_dict[i] = 0

    for i in nums:
        if i in count_dict:
            count_dict[i] += 1

    for keys, values in count_dict.items():
        if values == 0:
            ret.append(keys)

    return ret
# Given an array of distinct integers, determine the
# minimum absolute difference between any two elements.
# Print all element pairs with that difference in ascending order
# 
# Example:
# input = [6,2,4,10]
# The minimum absolute difference is 2 and the pairs with that 
# difference as (2,4) and (4,6). When printing element pairs (x,y),
# they should be ordered ascending first by x and then by y.
# 
# Return:
# Prints distinct element pairs that share the minimum absolute 
# difference, displayed in ascending order with each pair separated
# by one space on a single line
#     
# Output:             
#     2 4
#     4 6

def find(num_list):
    validate_doubles = set()
    storage = dict()
    diff = 0
    validate_min = set()

    for first_val in num_list:
        for second_val in num_list:
            if first_val != second_val:
                x = (first_val, second_val)
                y = sorted(x)
                z = tuple(y)
                validate_doubles.add(z)
                a = list(validate_doubles)
                b = sorted(a)
    # I think it's interesting to notice that the var 'b'
    # was created in the scope of the "double for" loop above
    # and yet it is accessible from outside. This is because
    # of the way Python handles and storage variables
    for values in b:
        diff = values[0] - values[1]
        storage[values] = abs(diff)

    for keys, values in storage.items():
        validate_min.add(values)

    for keys, values in storage.items():
        if values == min(validate_min):
            print(keys[0], keys[1])
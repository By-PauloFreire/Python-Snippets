# Given a number X, for each integer Y
# in the range from 1 to X inclusive,
# print one value per line as follows:
# 
# - If Y is a multiple of both 3 and 5, print FizzBuzz.
# - If Y is a multiple of 3 (but not 5), print Fizz.
# - If Y is a multiple of 5 (but not 3), print Buzz.
# - If Y is not a multiple of 3 nor 5, print the value of Y.
# 
# Constraint
# - 0 < X < 2 * 10⁵

def fizzBuzz(i):
    if i < 0 or i > 2000000:
        return print('Constraint Error')
    try:
        for n in range(1, i + 1):
            if n % 3 == 0 and n % 5 == 0:
                print('FizzBuzz')
            elif n % 3 == 0:
                print('Fizz')
            elif n % 5 == 0:
                print('Buzz')
            else:
                print(n)
    except:
        return 'Error'
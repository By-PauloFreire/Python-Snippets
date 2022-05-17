# This code expects a list of chars
# and will return whether the list is TRUE or FALSE

# To be considered TRUE, open brackets must be closed
# by the same type of bracket and in the correct order

# Constraint: 1 <= input <= 100

# e.g.    '()[]{}'    - TRUE
#         '([)]{}'      - FALSE

def validation(*list_of_chars):
    
    stack = list()

    if len(list_of_chars) < 1 or len(list_of_chars) > 100:
        return False

    try:
        for s in list_of_chars:
            if s in ['(', ')', '[', ']', '{', '}']:
                if s in ['(', '[', '{']:
                    stack.append(s)
                elif s == ')' and stack[0] == '(':
                    stack.pop()
                elif s == ']' and stack[0] == '[':
                    stack.pop()
                elif s == '}' and stack[0] == '{':
                    stack.pop()
            else:
                return False
    except:
        return False
    
    return not bool(stack)

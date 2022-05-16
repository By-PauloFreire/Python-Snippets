# This will keep track of the score.
# The rules are:
# D - Double the last score
# + - Add the last two score
# C - Cancel the last score
# int - Add to the score
#
# This exercise is about
# basic stack manipulation


def score(list_of_scores):

    stack = list()

    if len(list_of_scores) < 1 or len(list_of_scores) > 1000:
        return "Max length exceeded"

    for scores in list_of_scores:
        try:
            if int(scores):
                stack.append(int(scores));
        except:
            if str(scores) == "D" and len(stack) >= 1:
                x = stack[-1] * 2
                stack.append(x);
            elif str(scores) == "C" and len(stack) >= 1:
                stack.pop();
            elif str(scores) == "+" and len(stack) > 1:
                x = stack[-1] + stack[-2]
                stack.append(x)
            else:
                return "Error"
    return sum(stack)
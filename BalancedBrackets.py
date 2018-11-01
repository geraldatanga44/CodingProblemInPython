# Balanced Bracket Problem Hackerrank
# Free for distribution


def braces(ch):  # return opposite pair
    if ch == ']':  # no switch in python
        return '['  # work around
    if ch == '}':
        return '{'
    if ch == ')':
        return '('


def balancebraces(a):
    allbraces = ['(', ')', '[', ']', '{', '}']  # take care of other characters not pairs
    illegalstart = ['}', ']', ')']  # illegal start sequence must close before open
    goesinstack = ['{', '[', '(']  # characters that go into stack
    stack = []
    for ch in a:  # go over each individual character
        if ch not in allbraces:  # skip calculations if not character of interest
            continue
        if ch in illegalstart and len(stack) == 0:  # check for illegal start
            return False
        if ch in goesinstack:  # put close pair into stack
            stack.append(ch)
        if ch in illegalstart:  # reuse illegal for matching pairs
            if braces(ch) == stack.pop():  # returns open pair, should equal top stack character
                continue  # since we pop() just jump back up
            else:
                return False  # if top stack character don't match, problem, so exit
    return len(stack) == 0  # check for remaining characters


# try these test cases or make one on your own
case0 = '{[()]}'  # True
case1 = '{[(])}'  # False
case2 = '{{[[(())]]}}'  # True
case3 = '(a[n]d){(so)}[what]'  # True
print(balancebraces(case3))

# Find the Closest Palindrome
# Leetcode problem, brute force
# this doesn't solves the problem
# it can be optimized
# providing solution 2 for this


# method reverses number mathematically
def reversenumber(n):
    result = 0
    while n != 0:
        remainder = n % 10
        result = (result * 10) + remainder
        n //= 10
    return result


def nearestpalindromic(lim):
    temp = int(lim)
    while True:
        if reversenumber(temp) == temp and temp != int(lim):  # return # not equal to the #
            low = temp  # find low
            break
        temp -= 1

    temp = int(lim)

    while True:
        if reversenumber(temp) == temp and temp != int(lim):
            high = temp  # find high
            break
        temp += 1
    if high - int(lim) >= int(lim) - low:  # when to return low
        return str(low)
    return str(high)  # if not low, then high


print(nearestpalindromic('123'))

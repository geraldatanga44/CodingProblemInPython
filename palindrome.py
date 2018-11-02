"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads
the same backward as forward.
"""


def reverse(n):
    negative = n < 0  # use to determine signed
    if negative:
        n *= -1  # make value positive
    result = 0
    while n != 0:  # reverse value
        remainder = n % 10
        result = (result * 10) + remainder
        n //= 10
    if negative:
        return str(result) + '-'
    return str(result)


def palindrome(x):
    return reverse(x) == str(x)


print(palindrome(1221))

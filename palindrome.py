

def reverse(n):
    negative = n < 0  # use to determine signess
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

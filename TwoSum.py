# hackerrank twoSum problem with a twist - returns all pairs
# algorithm runs O(nlogn)


def binarysearch(array, target):  # binary search to find compliment in O(logn) time
    low = 0
    high = len(array) - 1
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] < target:
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        elif array[mid] == target:
            index = mid
            break
    return index


def merge(des, left, right):
    d_index = 0  # destination index
    r_index = 0  # right index
    l_index = 0  # left index
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            des[d_index] = left[l_index]
            d_index += 1
            l_index += 1
        else:
            des[d_index] = right[r_index]
            r_index += 1
            d_index += 1
    while l_index < len(left):
        des[d_index] = left[l_index]
        d_index += 1
        l_index += 1
    while r_index < len(right):
        des[d_index] = right[r_index]
        d_index += 1
        r_index += 1
    return des


# recursive merge sort
# implemented one for fun
def mergesort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid: len(arr)]

    mergesort(left)
    mergesort(right)

    return merge(arr, left, right)


def compliments(array, target):
    if len(array) < 2:  # array must have at least two values
        return []
    pair = []  # return all unique pairs
    mergesort(array)  # sort array for effective binary search
    for value in array:
        temp = []  # track pairs
        compliment = target - value  # find value compliment
        index = binarysearch(array, compliment)  # if compliment exist
        if index != -1:
            temp.append(value)
            temp.append(array[index])
            mergesort(temp)  # we don't want duplicate order like [-1, 10] and [10, -1]
            if temp not in pair:  # only add if pair doesn't exit
                pair.append(temp)
    return pair


# test case
a = [0, 3, 9, - 1, 8, 1, 10, 4, 5, 6, 3, 2, 7]
print(compliments(a, 9))

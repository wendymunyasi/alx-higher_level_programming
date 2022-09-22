#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): a list of integers

    Your algorithm must have the lowest complexity.
    Note: there may be more than one peak in the list.

    The most naive solution to this is to just go through each element
    one-by-one and see if it's qualified as a peak. This solution will take
    O(n) time complexity at the worst case and O(1) for space complexity
    which is super for most algorithm problem. So, here comes the tricky
    part, solve it with O(log(n)) time complexity!

    Usually Binary Search is being used in sorted array(it could also mean
    Bitonic array, or array that's sorted in some other ways), but this
    one is a little bit different as we can't sort the array.

    In Binary Search, we always check the middle value and see if it's
    qualified to be a peak, if not then we change the start or end pointer
    so that we get a new middle value.

    Returns:
        int: peak(s)
    """
    list_ = list_of_integers
    # if there is no list of integers return None
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]

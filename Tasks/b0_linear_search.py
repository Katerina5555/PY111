"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_in_arr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= min_in_arr:
            min_in_arr = arr[i]
        else:
            continue

    print(arr)
    return arr.index(min_in_arr)

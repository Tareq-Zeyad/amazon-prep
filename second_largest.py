# Find Second largest element in an array
"""
Given an array of integers, our task is to write a program that efficiently finds the second largest element present in the array. 
"""


def findSecondMax(arr, arr_size):

    if (arr_size < 2):
        print("Invalid input")
        return arr.sort

    for i in range(arr_size-2, -1, -1):
        if (arr[i] != arr[arr_size - 1]):
            print("The 2nd largest element is: ", arr[i])
            return

        print("there is no 2nd largest element")


if __name__ == "__main__":
    arr = [12, 35, 1, 10, 30, 1]
    n = len(arr)
    print(findSecondMax(arr, n))

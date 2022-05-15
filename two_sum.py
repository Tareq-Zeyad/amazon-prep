# Problem 3: Two Sum
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def twoSum(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]


if __name__ == "__main__":

    nums = [2, 7, 11, 15, 20]
    target = 31
    print(twoSum(nums, target))

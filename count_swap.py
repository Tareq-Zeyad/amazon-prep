# Problem 1: Minimum swaps to make a binary string Plaindrome.
"""
Give a binary string consisting of 0's and 1's only. E.g., 0100101. We are allowed to pick
any two indexes and swap them. We have to return the minimum number of swaps required to make,
it a palindrome or -1 if it cannot. The string 0100101 can be made a palindrome by swapping
(3,4)-> 0101001 and swapping (0,1) -> 1001001 which is a palindrome. In this case, the
correct answer is 2.
"""
# Function to Count minimum swap


def CountSwap(s, n):
    s = list(s)
    count = 0
    ans = True

    for i in range(n // 2):

        left = i

        right = n - left - 1

        while left < right:

            if s[left] == s[right]:
                break
            else:
                right -= 1

        if left == right:
            ans = False
            break
        else:
            for j in range(right, n - left - 1):
                (s[j], s[j + 1]) = (s[j + 1], s[j])
                count += 1
    if ans:
        return (count)
    else:
        return -1


if __name__ == "__main__":

    # passing arguments
    s = '0100101'

    # Length of string
    n = len(s)

    # Function calling
    ans1 = CountSwap(s, n)
    print(ans1)

# Problem 2: Program to check Strength of Password
"""
A password is said to be strong if it satisfies the following criteria: 

1- It contains at least one lowercase English character.
- It contains at least one uppercase English character.
3- It contains at least one special character. The special characters are: !@#$%^&*()-+
4- Its length is at least 8.
5- It contains at least one digit.
Given a string, find its strength. Let a strong password is one that satisfies all above conditions. A moderate password is one that satisfies first three conditions and has length at least 6. Otherwise password is week.
"""


def StrongPass(stringText):
    n = len(stringText)
    hasLower = False
    hasUpper = False
    hasDigit = False
    specialChar = False
    normalChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    for i in range(n):
        if stringText[i].islower():
            hasLower = True
        if stringText[i].isupper():
            hasUpper = True
        if stringText[i].isdigit():
            hasDigit = True
        if stringText[i] not in normalChars:
            specialChar = True

    print("Strength of password: ", end="")

    if (hasLower and hasUpper and hasDigit and specialChar and n >= 8):
        print("Strong")
    elif ((hasLower or hasUpper) and specialChar and n >= 6):
        print("Moderate")
    else:
        print("Weak")


if __name__ == "__main__":

    stringText = "DeveloperArbeit12@!"
    StrongPass(stringText)

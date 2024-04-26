def isPalindrome(string):
    midPoint = len(string) // 2
    for i in range(midPoint):
        if string[i] != string[len(string)-1-i]:
            return False
    return True

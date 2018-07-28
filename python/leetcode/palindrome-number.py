#https://leetcode.com/problems/palindrome-number/description/
def isPalindrome(x):
    if x<0:
        print("false")
    else:
        digits = 0
        t=x
        while t>0:
            print("here")
            digits+=1
            t=t/10
        print("digits:", digits)

isPalindrome(121)
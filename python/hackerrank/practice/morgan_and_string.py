"""
    https://www.hackerrank.com/challenges/morgan-and-a-string/problem
2
JACK
DANIEL
ABACABA
ABACABA
-
DAJACKNIEL
AABABACABACABA

DAJACKNIEL
AABABACABACABA

Incase of an equal string make sure you check for lexicographically minimal string.
For time saving, when we check for lexicographically least string return merged peace as well.
"""


def lexicographicalorder(a, b, i, j):
    result = []


def morganAndString(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            result.append(a[i])
            i += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    print(''.join(result))


t = int(input())
for t_itr in range(t):
    a = input()
    b = input()
    morganAndString(a, b)

lexicographicalorder("ZJWDEGFNRMTIYSXLVFDJVMTLPSX","ZJPVFQCGSRYJAFEJETMCVFSLIQM",0,0)
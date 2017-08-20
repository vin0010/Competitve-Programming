import math
#https://www.hackerrank.com/challenges/sherlock-and-squares
T = int(input())
for i in range(T):
    a,b = input().split(' ')
    # print(a)
    # print(b)
    print(math.floor(math.sqrt(int(b)))-math.ceil(math.sqrt(int(a)))+1)

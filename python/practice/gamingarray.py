# https://www.hackerrank.com/challenges/an-interesting-game-1
g=int(input())

for t in range(g):
    n=input()
    arr=list(map(int, input().split()))
    maxi=0
    count=0
    for i in arr:
        if i>maxi:
            maxi=i
            count+=1
    print("BOB" if count%2 is 1 else "ANDY")
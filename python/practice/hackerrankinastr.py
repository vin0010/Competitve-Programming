# https://www.hackerrank.com/challenges/hackerrank-in-a-string
n=int(input())
h="hackerrank"

for t in range(n):
    s=input()
    index=0
    for i in s:
        if i == h[index]:
            index+=1
        if index==10:
            print("YES")
            break
    if index<10:
        print("NO")

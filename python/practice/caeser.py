n=input()
s=input()
k=int(input())
for i in s:
    if i.isalpha():
        print(chr(ord(i) + k), end='')
    else:
        print(i, end='')
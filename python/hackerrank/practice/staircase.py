n=int(input())
space=' '
hash='#'
for i in range(1, n+1):
    print(space*(n-i), end='')
    print(hash * i)
t = int(input())


def find_days(a, b, k):
    if a==b or a<b:
        print(-1)
    else:
        print(((k - a) // (a - b)) + 1)


for i in range(t):
    a = int(input())
    b = int(input())
    k = int(input())
    find_days(a, b, k)

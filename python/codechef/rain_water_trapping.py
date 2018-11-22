"""
    https://www.codechef.com/status/CRES102,vin10

"""

# def trap1(arr):
#     print(len(arr))


def trap(arr):
    # print("====>", arr)
    # print(len(arr))

    if len(arr) <= 2:
        return 0
    left = []
    lmax = arr[0]
    rmax = arr[-1]
    right = [None] * len(arr)
    l = 0
    r = len(arr) - 1
    while l < len(arr) and r > -1:
        if arr[l] > lmax:
            lmax = arr[l]
        left.append(lmax)
        if arr[r] > rmax:
            rmax = arr[r]
        right[r] = rmax
        l += 1
        r -= 1

    result = 0
    for i in range(len(arr) - 1):
        small = left[i] if left[i] < right[i] else right[i]
        result += small - arr[i]
    print(result)


n = int(input())
for x in range(n):
    # print(x)
    le = int(input())
    l = list(map(int, input().split()))
    # print(l)
    trap(l)

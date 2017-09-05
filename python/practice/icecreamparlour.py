# https://www.hackerrank.com/challenges/icecream-parlor
t = int(input())
for x in range(t):
    m = int(input())
    n = int(input())
    arr = list(map(int, input().split()))
    result=dict()
    for index,value in enumerate(arr):
        result[value] = result.setdefault(value,[])+[index+1]

    for i in result.keys():
        # print("key", i)
        key = m - i
        if 2*i == m and len(result[i]) == 2:
            print("{} {}".format(result[i][0],result[i][1]))
            break
        elif key in result:
            print("{} {}".format(result[key][0],result[i][0])) if result[key][0]<result[i][0] else print("{} {}".format(result[i][0],result[key][0]))
            break
    # print(result)

"""
1
4
5
1 4 5 3 2
"""
def find_divisor_count(mini, maxi, common):
    return common // mini + common // maxi - 2


def process(a, b, target, start):
    i = start + a
    j = start + b
    counter = 0
    current = i
    while counter != target:
        if i < j:
            current = i
            i += a
        elif i > j:
            current = j
            j += b
        counter += 1
    print(current)


def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x * y) // gcd(x, y)
    return lcm


def solve(a, b, n):
    common = lcm(a,b)
    # interval = (find_divisor_count(a, b, n, common) if a < b else find_divisor_count(b, a, n, common)) + 1
    if a == b:
        print(a * n)
        return
    interval = find_divisor_count(a, b, common) + 1
    # print(interval)
    if n % interval == 0:
        print(common * (n // interval))
    else:
        counter = 0
        target = n % interval
        # print("target:",target)
        process(a, b, target, common * (n // interval))
        """
        mini = min(a,b)
        list=[]
        print("Range: ", common * (n // interval) + a," - ", common * ((n // interval) + 1), " by ", a)
        for i in range(common * (n // interval) + a, common * ((n // interval) + 1), a):
            if i % a == 0:
                list.append(i)
                # print("appending:",i)
        print("Range: ", common * (n // interval) + b, " - ", common * ((n // interval) + 1), " by ", b)
        for i in range(common * (n // interval) + b, common * ((n // interval) + 1), b):
            if i % b == 0:
                list.append(i)
                # print("appending:", i)

        print(sorted(list)[target-1])
        """
        """
        for i in range(common * (n // interval) + 1, a * n):
            # print("i:",i,"   a:",a," b:",b)
            if i % a == 0 or i % b == 0:
                counter += 1
            if counter == target:
                print(i)
                break
        """


T = int(input())
for _ in range(T):
    a, b, n = map(int, input().split())
    solve(a, b, n)

"""
1
3 5 15
"""

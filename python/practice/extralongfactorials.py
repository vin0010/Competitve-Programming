#https://www.hackerrank.com/challenges/extra-long-factorials
n=int(input())
result=1
for i in range(2, n+1):
    # print("Current:")
    # print(i*2)
    # result*=i
    result*=i;
print(result)

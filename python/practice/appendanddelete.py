#https://www.hackerrank.com/challenges/append-and-delete
import sys
s=input()
t=input()
k=int(input())
index = min(len(s),len(t))
if t==s and k>1:
    print("Yes")
    sys.exit()

sum=0
for i in range(index):
    if s[i]==t[i]:
        sum+=1
        print("sum increased {0} and {1}".format(s[i],t[i]))
    else:
        break
print("sum:{0}".format(sum))
count=(len(t)-sum)+(len(s)-sum)
print("count:{0}".format(k))
if count==k:
    print("Yes")
else:
    print("No")
# print(s[0])
# for i in s:
#     print(" {0}".format(i))
# print("s: {0}\t t:{1}\t k:{2}".format(s,t,k))
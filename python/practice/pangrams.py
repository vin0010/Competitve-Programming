# https://www.hackerrank.com/challenges/pangrams
s=input()
count=dict()
for i in s:
    if i.isalpha():
        count[i.upper()] = count.setdefault(i.upper(),1)
if len(count.keys()) is 26:
    print("pangram")
else:
    print("not pangram")
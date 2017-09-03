# https://www.hackerrank.com/challenges/minimum-loss
n = int(input())
str_arr=input().split(' ')
map=dict()
for i,v in enumerate(str_arr):
    map[int(v)] = i
# arr = [int(n) for n in input().split(' ')]
# for key in sorted(map.keys()):
sorted_keys=sorted(map.keys(),reverse=True)

# for index, key in enumerate(sorted_keys):
min_loss=10**10
for i in range(len(sorted_keys)-1):
    ckey=sorted_keys[i]
    nkey=sorted_keys[i+1]
    if map[ckey]<map[nkey] and ckey>nkey:
        min_loss = min(min_loss, ckey-nkey)

print(min_loss)
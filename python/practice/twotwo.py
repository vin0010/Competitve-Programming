# https://www.hackerrank.com/challenges/two-two/problem
# def substrings(word):
#     length=len(word)
#     for i in range(length):
#         for j in range(i,length):
#             #print("i:{0} and j:{1}".format(i,j))
#             print(word[i:j+1])
def getpowersoftwo():
    powerset=set()
    for i in range(1,800,1):
        powerset.add(pow(2,i))
    return powerset

def check_all_substrings(powerset, input_string):
    count=0
    length = len(input_string)
    for i in range(length):
        for j in range(i,length):
            s=input_string[i:j + 1]
            # print(input_string[i:j + 1])
            if s[0] == "0":
                print("removing for {0}".format(s))
                s = s[1:]
                print(s)
            if s:
                if int(s) in powerset:
                    print("{0} eisxt".format(int(input_string[i:j + 1])))
                    count+=1
            # else:
                # print("{0} not eisxt".format(input_string[i:j + 1]))
    print(count)
    print(powerset)
    # print("2" in powerset)



T=int(input())
# print(T)
# list=[]
temp=''
powerset=getpowersoftwo()
for i in range(T):
    temp=input()
    check_all_substrings(powerset,temp)
    # list.append(input())


# substrings(list[0])
# print("Coming here")



def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

# print(get_all_substrings('abcde'))
names = ["Alice","Bob","Bob"]
heights= [155,185,150]
li=[]
n=len(heights)
dic={}
for i in range(n):
    if heights[i] not in dic:
        dic[heights[i]]=names[i]
print(dic)#{155: 'Alice', 185: 'Bob', 150: 'Bob'}
for key in sorted(dic,reverse=True):
    li.append(dic[key])
print(li)#['Bob', 'Alice', 'Bob']
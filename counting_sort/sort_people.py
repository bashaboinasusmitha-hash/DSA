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
#sorting an array of squares:
nums = [-4,-1,0,3,10]
li=[]
for i in nums:
    li.append(i**2)
key=max(li)
count=[0]*(key+1)
ans=[0]*len(li)
for i in range(len(li)):
    count[li[i]]+=1
for j in range(1,len(count)):
    count[j]+=count[j-1]
for k in range(len(li)-1,-1,-1):
    ans[count[li[k]]-1]=li[k]
    count[li[k]]-=1
for num in range(len(li)):
    li[num]=ans[num]
print(li)#[0, 1, 9, 16, 100]
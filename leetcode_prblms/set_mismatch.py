nums=[1,1]
n=len(nums)
nums_1=set(nums)
li=[]
dic={}
for num in nums:
    if num not in dic:
        dic[num]=1
    else:
        dic[num]+=1
print(dic)
for val in dic:
    if dic[val]>1:
        li.append(val)
for i in range(1,n+1):
    if i not in nums_1:
        li.append(i)
print(li)

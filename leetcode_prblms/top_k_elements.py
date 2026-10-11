nums =[1,2,1,2,1,2,3,1,3,2]
k = 2
n=len(nums)
li=[]
dic={}
for i in nums:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)#{1: 4, 2: 4, 3: 2}
for key,value in sorted(dic.items(),key=lambda x:x[1],reverse=True):
    li.append(key)
    if len(li)==k:
        break
print(li)
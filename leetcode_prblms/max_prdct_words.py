words=["abcw","baz","foo","bar","xtfn","abcdef"]
n=len(words)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        found=False
        for k in words[i]:
            for l in words[j]:
                if k==l:
                    found=True
        if found is False:
            a=(len(words[i]))*(len(words[j]))
            ans=max(ans,a)
print(ans)
#move zeros:
nums=[0,1,0,3,12]
n=len(nums)
li=[]
li_1=[]
for i in range(n):
    if nums[i]!=0:
        li.append(nums[i])
    else:
        li_1.append(nums[i])
print(li+li_1)
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]==0:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)
#disappeared  elements:
nums=[4,3,2,7,8,2,3,1]
n=len(nums)
li=[]
for i in range(1,n+1):
    if i not in nums:
        li.append(i)
print(li)
#using set method:
nums=[1,1]
n=len(nums)
s=set(nums)
li=[]
for i in range(1,n+1):
    if i not in s:
        li.append(i)
print(li)
#product of array except self;
nums=[1,2,3,4]
n=len(nums)
ans=[]
a=1
for i in range(n):
    a=a*nums[i]
for i in nums:
    ans.append(a//i)
print(ans)
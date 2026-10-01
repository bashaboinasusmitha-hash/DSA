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
#median of two sorted arrays method-1:
nums1=[1,3]
nums2=[2]
nums3=nums1+nums2
n=len(nums3)
key=max(nums3)
count=[0]*(key+1)
ans=[0]*n
for i in range(n):
    count[nums3[i]]+=1
for j in range(1,len(count)):
    count[j]+=count[j-1]
for k in range(n):
    ans[count[nums3[k]]-1]=nums3[k]
    count[nums3[k]]-=1
print(ans)#[1, 2, 3]
for num in range(n):
    nums3[num]=ans[num]
left=0
median=nums3[(n//2)]
if n%2==0:
    median=(nums3[(n//2-1)]+nums3[(n//2)])/2
print(median)#2

#sorting the sentence:
s="is2 sentence4 This1 a3"
n=len(s)
a=[" "]*len(s)
s=s.split()
for i in s:
    pos=int(i[-1])
    a[pos-1]=i[:-1]
ans=' '.join(a)
print(ans)#This is a sentence 
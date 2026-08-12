def merge(nums,lb,mid,up):
    b=[0]*len(nums)
    i=lb
    j=mid+1
    k=lb
    while i<=mid and j<=up:
        if nums[i]<=nums[j]:
            b[k]=nums[i]
            i+=1
            k+=1
        else:
            b[k]=nums[j]
            j+=1
            k+=1
    while i<=mid:
        b[k]=nums[i]
        i+=1
        k+=1
    while j<=up:
        b[k]=nums[j]
        j+=1
        k+=1
    for k in range(lb,up+1):
        nums[k]=b[k]
def merge_sort(nums,lb,up):
    if lb<up:
        mid=(lb+up)//2
        merge_sort(nums,lb,mid)
        merge_sort(nums,mid+1,up)
        merge(nums,lb,mid,up)
nums= [15, 5, 24, 8, 1, 3, 16, 10, 20]
merge_sort(nums,0,len(nums)-1)
print(nums)

#sort by parity:
nums=[1,2,3,4]
n=len(nums)
li=[]
li_1=[]
for i in range(n):
    if nums[i]%2==0:
        li.append(nums[i])
    elif nums[i]%2!=0:
        li_1.append(nums[i])
final=li+li_1
print(final)

#sort an array by parity II
nums=[4,2,6,5,7,9]
n=len(nums)
even=[]
odd=[]
for i in range(n):
    if nums[i]%2==0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
ans=[0]*len(nums)
e=0
o=0
final=even+odd
for j in range(len(final)):
    if j%2==0:
        ans[j]=even[e]
        e+=1
    else:
        ans[j]=odd[o]
        o+=1
print(ans)
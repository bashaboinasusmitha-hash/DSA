#quick sort implementation when pivot = first element:
def partition(nums,low,high):
    pivot=nums[low]
    start=low+1
    end=high
    while start<end:
        while start<high and nums[start]<=pivot:
            start+=1
        while end>low and nums[end]>pivot:
            end-=1
        if start<end:
            nums[start],nums[end]=nums[end],nums[start]
    nums[low],nums[end]=nums[end],nums[low]
    return end
def quick_sort(nums,low,high):
    if low<high:
        p=partition(nums,low,high)
        quick_sort(nums,low,p-1)
        quick_sort(nums,p+1,high)
nums=[8, 3, 1, 7, 0, 10, 2]
quick_sort(nums,0,len(nums)-1)
print(nums)
#max prdct of two digits:
n=31
li=[]
while n>0:
    digits=n%10
    li.append(digits)
    n=n//10
li.reverse()
res=0
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        ans=li[i]*li[j]
        res=max(ans,res)
print(res)
#max subarray:
nums=[-2,1,-3,4,-1,2,1,-5,4]
n=len(nums)
ans=[]
res=0
for i in range(n-1):
    res+=nums[i]
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
            temp.append(nums[k])
        ans.append(temp)
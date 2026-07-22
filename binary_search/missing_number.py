nums=[3,0,1,2]
nums.sort()
l=0
r=len(nums)-1
while l<=r:
    mid=(l+r)//2
    if nums[mid]==mid:
        l=mid+1
    else:
        r=mid-1
print(l)
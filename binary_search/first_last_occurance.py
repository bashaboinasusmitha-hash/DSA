nums=[5,7,7,8,8,10]
target=8
left=0
right=len(nums)-1
ans=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        ans=mid
        right=mid-1
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
ans2=-1
left=0
right=len(nums)-1 
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        ans2=mid
        left=mid+1
    elif nums[mid]<target:
        left =mid+1
    else:
        right=mid-1
print([ans,ans2])
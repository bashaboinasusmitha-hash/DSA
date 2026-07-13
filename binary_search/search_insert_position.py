nums=[1,2,4,5,6,8]
target=9
left=0
right=len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print(left)
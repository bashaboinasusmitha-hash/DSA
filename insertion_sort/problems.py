#selection_sort:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)
#sorting in descending order:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]<key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)
#count the number of passes:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
ans=0
for i in range(1,n):
    ans=1
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
    ans+=1
print(nums)
print(ans)
#count number of shifts:
#insertion_sort:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)
#sorting in descending order:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]<key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums)
#count the number of shifts:
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
shifts=0
for i in range(1,n):
    key=nums[i]
    j=i-1
    while j>=0 and nums[j]>key:
        nums[j+1]=nums[j]
        shifts+=1
        j-=1
    nums[j+1]=key
print(nums)
print(shifts)
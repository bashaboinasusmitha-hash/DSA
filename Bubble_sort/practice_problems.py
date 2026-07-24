#Sort an array in ascending order
nums=[5, 2, 9, 1, 7]
n=len(nums)
for i in range(n-1):
    for j in range(n-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
#sort in descending order:
nums=[8, 3, 1, 6, 4]
n=len(nums)
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j]<nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)
#count the number of swaps :
nums=[8, 3, 1, 6, 4]
n=len(nums)
res=0
for i in range(n-1):
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            res+=1
print(res)
#improvement of bubble sort:
nums=[3,4,1,2,7,0]
n=len(nums)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swap=True
    if not swap:
        break   
print(nums)
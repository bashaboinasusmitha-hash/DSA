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
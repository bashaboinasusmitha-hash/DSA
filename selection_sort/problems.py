#basic selection sort implement :
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if nums[j]<nums[min_idx]:
            min_idx=j
    nums[i],nums[min_idx]=nums[min_idx],nums[i]
print(nums)
#finding the number of passes :
nums=[64, 34, 25, 12, 22, 11, 90, 5]
n=len(nums)
max_pass=0
for i in range(n-1):
    min_idx=i
    max_pass=1
    for j in range(i+1,n):
        if nums[j]<nums[min_idx]:
            min_idx=j
    nums[i],nums[min_idx]=nums[min_idx],nums[i]
    max_pass+=1
print(max_pass)
'''time complexity of selection sort : o(n**2)'''
#sorting an array in descending order:
nums=[5, 1, 4, 2, 8]
n=len(nums)
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if nums[j]>nums[min_idx]:
            min_idx=j
    nums[i],nums[min_idx]=nums[min_idx],nums[i]
print(nums)
#sorting an array containing duplicates:
nums=[4, 2, 4, 1, 2]
n=len(nums)
for i in range(n-1):
    min_idx=i
    for j in range(i+1,n):
        if nums[j]<nums[min_idx]:
            min_idx=j
    nums[i],nums[min_idx]=nums[min_idx],nums[i]
print(nums)
nums = [1,3,1,1,2]
arr=[0]*len(nums)
n=len(nums)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]==nums[j]:
            arr[i]+=abs(i-j)
            arr[j]+=abs(i-j)
print(arr)
print("hello")
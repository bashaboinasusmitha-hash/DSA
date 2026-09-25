nums = [1,2,3,2,5]
n=len(nums)
ans=nums[0]
for i in range(1,n):
    if nums[i]==nums[i-1]+1:
        ans+=nums[i]
    else:
        break
print(ans)
while ans in nums:
    ans+=1
print(ans)
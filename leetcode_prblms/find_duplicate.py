#finding dupliacte element:
nums = [1,3,4,2,2]
nums.sort()
n=len(nums)
for i in range(n-1):
    if nums[i]==nums[i+1]:
        print(nums[i])
        break
#leetcode 167 : Two sum II
numbers=[-1,0]
target=-1
numbers=[0]+numbers
n=len(numbers)
for i in range(1,n-1):
    for j in range(i+1,n):
        if numbers[i]+numbers[j]==target:
            print([i,j])#[1,2]
#optimal solution:
numbers=[2,7,11,15]
target=9
n=len(numbers)
left=0
right=n-1
while left<right:
    total=numbers[left]+numbers[right]
    if total==target:
        print([left+1,right+1])#[1,2]
        break
    elif total<target:
        left+=1
    else:
        right-=1

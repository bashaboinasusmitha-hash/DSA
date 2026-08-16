#radix sort implementation:
def count_sort(nums,n,pos):
    count=[0]*10
    b=[0]*n
    #prepare count array:
    for i in range(n):
        digits=(nums[i]//pos)%10
        count[digits]+=1
    #update count array:
    for j in range(1,10):
        count[j]+=count[j-1]
    #sort the array(b)
    for k in range(n-1,-1,-1):
        digits=(nums[k]//pos)%10
        b[count[digits]-1]=nums[k]
        count[digits]-=1
    for num in range(n):
        nums[num]=b[num]
def radix_sort(nums):
    n=len(nums)
    high=max(nums)
    pos=1
    while high//pos>0:
        count_sort(nums,n,pos)
        pos*=10
nums=[432, 8, 530, 90, 88, 231, 11, 45, 677, 199]
radix_sort(nums)
print(nums) #[8, 11, 45, 88, 90, 199, 231, 432, 530, 677] 
#leetcode:164
def count_sort(nums,n,pos):
    count=[0]*10
    b=[0]*n
    for i in range(n):
        digits=(nums[i]//pos)%10
        count[digits]+=1
    for j in range(1,len(count)):
        count[j]+=count[j-1]
    for k in range(n-1,-1,-1):
        digits=(nums[k]//pos)%10
        b[count[digits]-1]=nums[k]
        count[digits]-=1
    for num in range(n):
        nums[num]=b[num]
def radix_sort(nums):
    n=len(nums)
    high=max(nums)
    pos=1
    while high//pos>0:
        count_sort(nums,n,pos)
        pos*=10
nums=[3,6,9,1]
radix_sort(nums)#(1,3,6,9)
ans=0
if len(nums)<2:
    print(ans)
else:
    for number in range(1,len(nums)):
        a=nums[number]-(nums[number-1])
        ans=max(a,ans)
    print(ans)#3
#simple way:
nums=[3,6,9,1]
n=len(nums)
nums.sort()
ans=0
if n<2:
    print(ans)
else:
    for i in range(1,n):
        res=nums[i]-nums[i-1]
        ans=max(res,ans)
    print(ans)#3
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
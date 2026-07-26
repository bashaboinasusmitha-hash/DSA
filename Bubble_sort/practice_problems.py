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
#count number of passes:
nums=[1, 2, 3, 5, 4]
n=len(nums)
pass_count=0
for i in range(n-1):
    pass_count+=1
    swap=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swap=True
    if not swap:
        break
print(pass_count)
#Print the array after every pass
nums=[1, 2, 3, 5, 4]
n=len(nums)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swap=True
    print(f"{i+1} : {nums}")
    if not swap:
        break
#sort only even numbers:
nums=[8, 5, 4, 7, 2]
n=len(nums)
li=[]
for i in range(n):
    if nums[i]%2==0 :
        li.append(nums[i])
m=len(li)
for i in range(m-1):
    for j in range(m-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
a=0
for k in range(n):
    if nums[k]%2==0:
        nums[k]=li[a]
        a+=1
print(nums)
#contains duplicates:
nums=[1,2,3,1]
n=len(nums)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swap=True
    if not swap:
        break
found=False
for k in range(len(nums)-1):
    if nums[k]==nums[k+1]:
        found=True
        break
print(found)
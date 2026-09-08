arr1 = [4,5,8] 
arr2 = [10,9,1,8]
d = 2
count=0
nums=[]
n=len(arr1)
m=len(arr2)
for i in range(n):
    valid=True
    for j in range(m):
        if abs(arr1[i]-arr2[j])<=d:
            valid=False
            break
    if valid:
        nums.append(arr1[i])
print(len(nums))
#construct uniform parity:
nums1=[2,3]
n=len(nums1)
nums2=[0]*n
all_even=True
for i in range(n):
    if nums1[i]%2!=0:
        all_even=False
        break
all_odd=True
for i in range(n):
    if nums1[i]%2==0:
        all_odd=False
        break
for i in range(n):
    if all_odd or all_even:
        nums2[i]=nums1[i]
    else:
        for j in range(n):
            if i!=j and nums1[i]%2!=nums1[j]%2:
                nums2[i]=nums1[i]-nums1[j]
                break
all_even=True
for k in range(len(nums2)):
    if nums2[k]%2!=0:
        all_even=False
        break
all_odd=True
for m in range(len(nums2)):
    if nums2[m]%2==0:
        all_odd=False
if all_even or all_odd:
    print(True)
else:
    print(False)
#find the smallest number greater than target:
letters=["c","f","j"]
target = "c"
ans=[]

for i in letters:
    if target<i:
        ans.append(i)
if len(ans)==0:
    print(letters[0])
print(min(ans))
#construct uniform parity II:
nums1 = [4,6]
n=len(nums1)
nums2=[0]*n
all_even=True
for i in range(n):
    if nums1[i]%2!=0:
        all_even=False
        break
if all_even:
    for i in range(n):
        nums2[i]=nums1[i]
    print(True)
else:
    smallest=min(nums1)
    if smallest%2==1:
        for i in range(n):
            if nums1[i]%2==0:
                nums2[i]=nums1[i]-smallest
            else:
                nums2[i]=nums1[i]
        print(nums2)
        print(True)
    else:
        print(False)
#search in rotated sorted array:
nums=[4,5,6,7,0,1,2]
target=0
left=0
right=len(nums)-1
for i in range(n-1):
    if nums[i]>nums[i+1]:
        left=i+1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
else:
    print(-1)
'''nums=[1]
target=1
n=len(nums)
if n==1:
    if nums[0]==target:
        print()
    else:
        print(-1)
for i in range(n-1):
    if nums[i]>nums[i+1]:
        if nums[i+1]==target:
            print(i+1)
        else:
            i+=1
    else:
        print(-1)'''
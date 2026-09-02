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
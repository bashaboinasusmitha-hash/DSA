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
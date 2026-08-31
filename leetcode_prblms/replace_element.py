#brute force way
arr = [17,18,5,4,6,1]
li=[0]*len(arr)
li[-1]=-1
n=len(arr)
for i in range(n-1):
    a=max(arr[i+1:])
    li[i]=a
print(li)
#optimal way:
arr=[17,18,5,4,6,1]
n=len(arr)
max_right=arr[-1]
arr[-1]=-1
for i in range(n-2,-1,-1):
    temp=arr[i]
    arr[i]=max_right
    max_right=max(max_right,temp)
print(arr)
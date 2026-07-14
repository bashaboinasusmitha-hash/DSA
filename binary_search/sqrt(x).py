def square_root(x):
    l=1
    r=x
    while l<=r:
        mid=(l+r)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            l=mid+1
        else:
            r=mid-1
    else:
        return r
print(square_root(8))
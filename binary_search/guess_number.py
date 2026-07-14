pick=6
def guess(num):
    if num>pick:
        return -1
    elif num==pick:
        return 0
    else:
        return 1  
def guess_number(n):
    left=1
    right=n
    while left<=right:
        mid=(left+right)//2
        results=guess(mid)
        if results==0:
            return mid
        elif results==1:
            left=mid+1
        else:
            right=mid-1
print(guess_number(10))
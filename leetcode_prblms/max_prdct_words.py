words=["abcw","baz","foo","bar","xtfn","abcdef"]
n=len(words)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        found=False
        for k in words[i]:
            for l in words[j]:
                if k==l:
                    found=True
        if found is False:
            a=(len(words[i]))*(len(words[j]))
            ans=max(ans,a)
print(ans)
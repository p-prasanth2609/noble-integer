A=list(map(int,input().split()))
A.sort()
p=0
for i in range(len(A)):
    if(A[i]==len(A)-1-i):
        p+=1
if(p==0):
    print(p)
else:
    print(p)

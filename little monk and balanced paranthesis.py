n=int(input())
a=list(map(int,input().split()))
s=[]
c=0
for i in range(0,n):
    if a[i]>0:
        s.append(i)
    elif a[i]<0:
        if s and a[i]==-a[s[-1]]:
            s.pop()
            if not s:
                #print(s)
                temp=-1
            else:
                #print(s)
                temp=s[-1]
            c= max(c,i-temp)
        else:
            s.append(i)
print(c) 

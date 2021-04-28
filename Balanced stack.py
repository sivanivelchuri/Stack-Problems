l=[1,-1,2,3,-1]
r=[0]
top=0
length=0
for i in range(0,len(l)):
    if l[i]>0:
        r.append(i+1)
        top=i+1
    elif l[top]==-l[i]:
        length=(i+1)-top
        r.pop(top)
        top=-1
    else:
        r.append(i)

        
        

n=int(input())
arr=list(map(int,input().split()))
c=0
stack=[]
for i in range(n):
    while (stack!=[] and stack[-1]<arr[i]):
        stack.pop()
        c+=1
    if stack!=[]:
        c+=1
    stack.append(arr[i])
print(c)
        

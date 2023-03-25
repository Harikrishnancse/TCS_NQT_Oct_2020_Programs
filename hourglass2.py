N=int(input("Enter number to print HOUR-GLASS-PATTERN : "))
arr=[]
for i in range(0,N):
    temp=[]
    for j in range(0,N):
        if i <=(N-1)/2 :
            if i<=j<N-i:
                temp.append('*')
            else:
                temp.append(' ')
        else:
            if N-1-i<=j<=i:
                temp.append('*')
            else:
                temp.append(' ')
    arr.append(temp)
for item in arr:
    print(''.join(item))

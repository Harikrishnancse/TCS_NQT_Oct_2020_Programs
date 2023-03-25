n=int(input("Enter number to print HOUR-GLASS-PATTERN : "))
N=2*n-1
arr=[]
for i in range(0,N):
    temp=[]
    for j in range(0,N):
        if i <=(N-1)/2 :
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                if i<=j<N-i:
                    temp.append('*')
                else:
                    temp.append(' ')
            else:
                temp.append(' ')
        else:
            if (i%2==0 and j%2==0) or (i%2==1 and j%2==1):
                if N-1-i<=j<=i:
                    temp.append('*')
                else:
                    temp.append(' ')
            else:
                temp.append(' ')
    arr.append(temp)
for item in arr:
    print(''.join(item))
                
            
            

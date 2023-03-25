'''
Maximum product of 4 numbers in a array
'''
n=int(input("enter number of elements : "))
print("Enter ",n," Elements ")
i=0
arr=[]
while(i<n):
    el=input()
    arr.append(int(el))
    i=i+1
max = 0
if n>=4:
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    temp = (arr[i]*arr[j])
                    temp1 = (arr[k]*arr[l])
                    res= temp * temp1
                    if res >= max:
                        print('(',i,',',j,',',k,',',l,')->',res)
                        max = res
    print(max)
else:
    print("Insufficient data")

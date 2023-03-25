arr=[]
temp=True
print("Enter distances of each participant and end with type \'q\' ")
while(temp):
    inp=input()
    if inp=='q':
        break
    else:
        arr.append(float(inp))

out_arr = []
for item in arr:
    if item > 15.192 or item < 0.0:
        out_arr.clear()
        out_arr.append("Wrong input")
    elif item == 15.192:
        pass
    else:
        out_arr.append(item)

print("Long runners excluding finishers : ")

if type(out_arr[0]) is str:
    print("Invalid data")
else:
    out_arr=sorted(out_arr,reverse=True)
    if 1 <= len(out_arr) <= 3:
        print(out_arr)
    else:
        print(out_arr[:3])
    
    
        




n=int(input("Enter the size of an array"))
arr=[]
for i in range(n):
    num=int(input("Enter the elements"))
    arr.append(num)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array:",arr)
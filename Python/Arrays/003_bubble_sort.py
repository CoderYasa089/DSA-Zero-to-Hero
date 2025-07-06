#Program 3: Implement Bubble Sort to sort elements of an array in ascending order.
arr=[10,50,3,29,5]
print("Initial array: ",arr)
n=len(arr)  #Store length of arr into n
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
           temp=arr[j]
           arr[j]=arr[j+1]
           arr[j+1]=temp

print("\nSorted array is: ",arr)
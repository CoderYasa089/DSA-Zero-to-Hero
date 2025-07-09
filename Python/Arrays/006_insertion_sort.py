#Program 5: Implement Insertion Sort to sort elements of an array in ascending order.
arr=[12,5,7,3,6]
n=len(arr)
for j in range(1,n):
    i=j-1
    key=arr[j]
    while(i>=0 and key<arr[i]):
        arr[i+1]=arr[i]
        i=i-1
    arr[i+1]=key
print("Sorted array is: ",arr)
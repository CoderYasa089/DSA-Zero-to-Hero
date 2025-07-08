#Program 5: Implement Selection Sort to sort elements of an array in ascending order.
#Selection sort: Select lowest element in the array and move it to the front of the array.
#Don't use 'min' as variable name
arr=[12,5,22,14,4,2]
n=len(arr)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if(arr[j]<arr[min_index]):
            min_index=j
    if(min_index != i):
        arr[i],arr[min_index]=arr[min_index],arr[i]
print("Sorted Array: ",arr)
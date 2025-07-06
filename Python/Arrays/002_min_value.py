#Program 2: Find minimum value in an Array(list)
arr=[29,4,5,30,20]
min_value=arr[0]
for i in arr:
    if i < min_value:
        min_value = i

print("Minimum Value in array: ",min_value)
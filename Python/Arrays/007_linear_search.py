#Program 6: Implement Linear Search to find a given element from the array of elements.
arr=[12,4,5,2,8,3]
n=len(arr)
target_value=int(input("Enter the Value to search:"))
element_caught=False
target_index=-1
for i in range(n):
    if(arr[i]==target_value):
        element_caught=True
        target_index=i
        break
        
if(element_caught==True):
    print(f"\nElement {target_value} found at index:{target_index}")
else:
    print("\nElement not found in the array!")
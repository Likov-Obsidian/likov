def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    
    else:
        return binary_search(arr, target, mid + 1, right)

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

print(binary_search(arr, 23))
print(binary_search(arr, 2))
print(binary_search(arr, 91))
print(binary_search(arr, 10))
print(binary_search(arr, 38))
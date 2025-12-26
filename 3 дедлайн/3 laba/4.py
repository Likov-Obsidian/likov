def find_max(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    if not arr or left > right:
        return None
    
    if left == right:
        return arr[left]
    
    mid = (left + right) // 2
    
    left_max = find_max(arr, left, mid)
    right_max = find_max(arr, mid + 1, right)
    
    return left_max if left_max > right_max else right_max

numbers = [3, 7, 1, 9, 4, 2]
print(find_max(numbers))
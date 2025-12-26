# Медленное решение O(n²) - дано
def find_pair_slow(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None


def find_pair_fast(arr, target):
    seen = set()
    
    for num in arr:
        needed = target - num
        if needed in seen:
            return (needed, num)
        seen.add(num)
    
    return None

arr = [2, 7, 11, 15, 3, 8]
target = 10

print("Медленное решение:", find_pair_slow(arr, target))
print("Быстрое решение:", find_pair_fast(arr, target))
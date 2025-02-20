def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1  # Target is not present in the array

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Example usage
arr = [2, 3, 4, 10, 40]
target = int(input("enter number to search: "))

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element is present at index {result}")
else:
   print("Element is not present in array")
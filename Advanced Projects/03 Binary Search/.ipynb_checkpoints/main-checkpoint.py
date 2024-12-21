def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Ignore left half
        else:
            right = mid - 1  # Ignore right half

    return -1  # Target not found

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Target not found

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid  # Target found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)  # Search right half
    else:
        return binary_search_recursive(arr, target, left, mid - 1)  # Search left half

def test_binary_search():
    arr = [2, 3, 4, 10, 40]
    target = 10

    print("Testing Iterative Binary Search:")
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")

    print("\nTesting Recursive Binary Search:")
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")

if __name__ == "__main__":
    test_binary_search()
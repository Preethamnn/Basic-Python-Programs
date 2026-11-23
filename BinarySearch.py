# Read number of elements
n = int(input("Enter number of elements: "))

# Read sorted elements
arr = []

print("Enter elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

# Element to search
key = int(input("Enter element to search: "))

# Initialize pointers
low = 0
high = n - 1

# Binary Search
while low <= high:

    # Find middle index
    mid = (low + high) // 2

    # Element found
    if arr[mid] == key:
        print("Element found at index", mid)
        break

    # Search in right half
    elif arr[mid] < key:
        low = mid + 1

    # Search in left half
    else:
        high = mid - 1

# Element not found
if low > high:
    print("Element not found")
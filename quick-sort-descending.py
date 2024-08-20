def partition_descending(A, low, high):
    """
    Structure: | HIGH | LOW | UNSORTED | PIVOT |
    Partition function for QuickSort in descending order.
    It places elements greater than the pivot to the left and elements less than the pivot to the right.
    """
    # Choose the rightmost element as pivot
    pivot = A[high]
    # Pointer to end of HIGH subarray (elements greater than pivot)
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if A[j] >= pivot:  # Found element greater than or equal to pivot, move it into HIGH (which is before LOW)
            i += 1  # grow len(HIGH) by one, i now points to the first element of LOW
            A[i], A[j] = A[j], A[i]  # Swap the elements to place A[j] in the HIGH subarray
    # Place the pivot element in its correct position
    A[i + 1], A[high] = A[high], A[i + 1]
    # Return the position of pivot after swapping
    return i + 1

def quickSort_descending(A, low, high):
    if low < high:
        # Find pivot element such that
        # element greater than pivot are on the left
        # element less than pivot are on the right
        partition_i = partition_descending(A, low, high)
        quickSort_descending(A, low, partition_i - 1)  # Recursive call on the left of pivot
        quickSort_descending(A, partition_i + 1, high)  # Recursive call on the right of pivot

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print("Original array:", arr)
quickSort_descending(arr, 0, len(arr) - 1)
print("Sorted array in descending order:", arr)

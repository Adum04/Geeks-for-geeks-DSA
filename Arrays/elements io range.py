def check_elements(self, arr, n, A, B):
    arr_set = set(arr)

    # Check if all numbers in the range [A, B] are in arr_set
    for i in range(A, B + 1):
        if i not in arr_set:
            return False  # Return False if any number is not found

    return True

def linear_search(arr, target):
    ''' not sure if this counts as linear search
    if target in arr:
        return arr.index(target)
    '''   
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1 # "- 1" accounts for 0 index
    while low_index <= high_index:
        middle_index = (low_index + high_index) // 2 # floor division will return an integer

        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target: # if target is below middle then can get rid of values higher than middle
            high_index = middle_index
        elif arr[middle_index] < target: # if target is above middle then can get rid of values lower than middle
            low_index = middle_index
    


    return -1  # not found

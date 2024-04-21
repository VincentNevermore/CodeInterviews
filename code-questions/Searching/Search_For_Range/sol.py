def searchForRange(array, target):
    left = 0
    right = len(array) - 1

    res = [-1, -1]

    # Search for the first occurance of a number
    while left <=right:
        mid = left + (right-left)//2
        if array[mid] == target:
            res[0] = mid
            right = mid - 1
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid - 1

    left = 0
    right = len(array) - 1

    # Search for the last occurance of a number
    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == target:
            res[1] = mid
            left = mid + 1
        elif array[mid] < target:
            left = mid+1
        else:
            right = mid - 1

    return res

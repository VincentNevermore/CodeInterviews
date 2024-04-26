def indexEqualsValue(array):
    # Write your code here.
    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]

        if middleValue < middleIndex:
            leftIndex = middleIndex + 1
        elif middleValue == middleIndex and middleIndex == 0:
            return middleIndex
        elif middleValue == middleIndex and array[middleIndex-1] < middleIndex - 1:
            return middleIndex
        else:
            rightIndex = middleIndex - 1

    return -1

#O(logn) time | O(1) space

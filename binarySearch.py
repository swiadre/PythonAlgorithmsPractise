def binarySearch(arr, target, left, right):
    if right >= left:                                       # Checking if the target exist
        mid = (right + left) // 2                           # Counting mid number
        
        if arr[mid] == target:                              # Checking if pointer (mid) is target
            return mid

        elif target > arr[mid]:                             # If target is on right or left side
            return binarySearch(arr, target, mid + 1, right)# We set new left border and start from begining
                                                            
        else:
            return binarySearch(arr, target, left, mid - 1) # if target is on left we are setting new right border
    else:                                                   # And call our function again
        return False                                        # If target isn't in list we return False
        

array = [3,4,5,6,7,8,9]
left = 0
right = len(array) - 1
target = 6

print(binarySearch(array, target, left, right))

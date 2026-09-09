def brute_max_sub_array(A):
    """
    Brute-force approach for the Maximum Subarray problem.
    Time Complexity: O(n^2)
    """
    if not A:
        return 0, 0, 0
        
    k, l = 0, 0
    max_sum = A[0]
    
    for i in range(len(A)):
        temp_sum = 0
        for j in range(i, len(A)):
            temp_sum += A[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                k = i
                l = j
                
    return k, l, max_sum 


def find_max_cross_sub_array(A, low, mid, high):
    """
    Helper function to find the maximum subarray crossing the midpoint.
    Time Complexity: O(n)
    """
    left_sum = A[mid]
    temp_sum = A[mid]
    max_left = mid 
  
    i = mid - 1
    while i >= low:
        temp_sum += A[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i
        i -= 1 
    
   
    right_sum = A[mid + 1]
    temp_sum = A[mid + 1] 
    max_right = mid + 1
    
   
    j = mid + 2 
    while j <= high:
        temp_sum += A[j]
        if temp_sum > right_sum:
            right_sum = temp_sum 
            max_right = j
        j += 1
        
    return max_left, max_right, left_sum + right_sum


def find_max_sub_array(A, low, high):
    """
    Divide and Conquer approach for the Maximum Subarray problem.
    Time Complexity: O(n log n)
    """
    if high == low:
        return low, high, A[low]
    else:
        mid = (high + low) // 2 
        
        left_low, left_high, left_sum = find_max_sub_array(A, low, mid)
        right_low, right_high, right_sum = find_max_sub_array(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_cross_sub_array(A, low, mid, high)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum 
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum 
        else: 
            return cross_low, cross_high, cross_sum


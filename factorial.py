def factorial(n = 0, result = 0): 
    if n <= 1:                     # For values smaller than 2 function always will return 1
        return 1
    else:
        result = n * factorial(n-1)# Recursive factorial counting

    return result                  # Returning final result


print(factorial(5))
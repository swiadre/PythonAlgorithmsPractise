def algEuklidesa(a, b):             # Greatest common divisor by Euclidean algorithm
    while a != b:                   # Loop where we are checking if a is greater than b
        if a > b:                   # If a is greater than b
            a = a - b               # We are setting a as difference between a and b
        if a < b:                   # And if a is less than b
            b = b - a               # If it is true we are setting b as a difference between a and b

    return a                        # We can return a as a result because the loop ended 
                                    

print(algEuklidesa(13, 29))
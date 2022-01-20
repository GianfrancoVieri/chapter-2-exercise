def isprime(x):
    """takes in a single integer argument x and returns 
    True or False depending on whether or not the argument is prime"""
    import math 
    y = math.isqrt(x) + 1
    c = 0
    if x == 1:
        return False
    else:
        for n in range(2,y):
            if x%n == 0:
                return False
        return True


    

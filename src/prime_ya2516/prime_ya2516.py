import math

def is_prime(n):
    """
    Check if a given number is a prime number.
    
    Parameters
    ----------
    n : an arbitrary number
    
    Returns
    -------
    Output a Boolean value.  
    'True' if the input number is prime, and 'False' if it is not.
    
    Examples
    --------
    >>> from prime_ya2516 import prime_ya2516
    >>> n = 5
    >>> is_prime(n)
    True
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
from typing import List
def get_factors(num: int, prime:bool=False) -> List[int]:
    """
    Returns a list of factors of provided num
    
    Args:
        num (int): the number for which we want factors
    Returns:
        List[int]: a list of factors of num
    """
    factors = []
    for i in range(1, num + 1): #range returns ints between start (defaults to 0), end (exclusive)
        if num % i == 0:
            factors.append(i)
    if prime:
        factors = [f for f in factors if len(get_factors(f)) == 2]
    return factors

def get_prime_factors(num: int) -> List[int]:
    primes = []
    for i in get_factors(num):
        factors = get_factors(i)
        if len(factors) == 2:
            primes.append(i)
    return primes
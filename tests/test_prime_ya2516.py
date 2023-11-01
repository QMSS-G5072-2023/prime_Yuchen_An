from prime_ya2516 import prime_ya2516

def test_is_prime():
    # Test the is_prime function with known prime numbers
    primes = [2,3,5,7,11]
    for i in primes:
        assert prime_ya2516.is_prime(i) == True, f'Test failed with {i}'
    
    # Test the is_prime function with known composite numbers
    composites = [4,6,8,9,10]
    for i in composites:
        assert prime_ya2516.is_prime(i) == False, f'Test failed with {i}'
    
    # Test the is_prime function with known edge cases
    edge_cases = [-1, 0, 1]
    for i in edge_cases:
        assert prime_ya2516.is_prime(i) == False , f'Test failed with {i}' 
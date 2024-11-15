#1
def isPrime(broj):
    if broj <= 1:
        return False
    
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False

    return True

print(isPrime(7))  # True
print(isPrime(10))  # False

#2
def isPrime(broj):
    if broj <= 1:
        return False
    for i in range(2, int(broj**0.5) + 1):
        if broj % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [broj for broj in range(start, end + 1) if isPrime(broj)]

print(primes_in_range(1, 10))  # [2, 3, 5, 7]
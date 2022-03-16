input = "abc"
import random
import math

def isPrime(a):
    for i in range(2,math.ceil(math.sqrt(a))+1):
        if a % i == 0: return False
    return True

def generate_prime(minimal_value, count=1):
    primes = []
    while(len(primes) < count):
        minimal_value += 1
        if isPrime(minimal_value):
            primes.append(minimal_value)
    
    return primes        


print(generate_prime(100, 10))

print(isPrime(1117))
    # może a-1
#    a**2 + b**3 + c**4 % (a*b*c)

def calc_lower_bound(input):
    bound = 0; mod = 1
    for char, power in zip(input, range(len(input))):
        bound += ord(char)**(power%128)
        mod *= ord(char)
    
    return bound % 1117

print(calc_lower_bound("abcsf"))
def hash(input):
    s = 0
    prime = generate_prime(100, len(input))
    for char, p in zip(input, prime):
        s = s + ord(char) * p 
    return s % 100

print(hash("abc"))
print(hash("axd"))


def test_collision(function):
    

    
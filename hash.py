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


#print(generate_prime(100, 10))
#print((256).to_bytes(2,byteorder="big")==b'\x01\x00')
a = b'\x01\x00'
#print(len(a))

#for byte in a:
#    print(byte)
#print((a))
#print(bytes([651321]))
#print(isPrime(1117))
    # może a-1
#    a**2 + b**3 + c**4 % (a*b*c)

def calc_lower_bound(input):
    bound = 0; mod = 1
    for char, power in zip(input, range(len(input))):
        bound += (char)**(power%128)
        mod *= (char)
    
    return bound % 1117

#"1234123"-> 01011010110
#12332133 -> 0 - 1000000

#print(calc_lower_bound("abcsf"))
def hash(input):
    s = 0
    prime = generate_prime(1000, len(input))
    for char, p in zip(input, prime):
        s = s + (char) * p 
    return s % 1000


def hash_str(input):
    return hash(bytes(input, 'utf-8'))

def hash_int(input):
    return hash((input).to_bytes(8,byteorder="big"))


#print(hash(b'\x01\x02\x03'))
#rint(hash_str("abd"))
#print(hash_int(123))

#print(hash("axd"))


def test_collision():
    BYTES_TO_TEST = 3
    collision_values = set()
    s = set()
    for i in range(2**(8*1)):
        if hash_int(i) in s:
            collision_values.add(i)
        else:
            s.add(hash_int(i))

    print((collision_values))        

(test_collision())

print(hash_int(128), hash_int(127), hash_int(255), hash_int(254))
            
    
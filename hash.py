input = "abc"
import random
import math
from sys import byteorder

#liczba bitów na których zapisujemy
N = 8*4


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
# print((256).to_bytes(2,byteorder="big")==b'\x01\x00')
# print(ord("A"))
# print((65).to_bytes(N,byteorder="big"))
# print(int.from_bytes((ord("A")).to_bytes(N,byteorder="big"), byteorder='big'))
# a = b'\x01\x00'
# print(a)

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

# print(calc_lower_bound("abcsf"))
def hash_str(input):
    return hash(bytes(input, 'ascii'))

def how_many_bytes(num: int):
    if num < 1:
        return 1
    # 0-255 -> 1
    # 256-65535 -> 2 ...
    return (math.ceil(math.log2(num-1))//8)+1

def hash_int(input):
    return hash((input).to_bytes(how_many_bytes(input),byteorder="big"))

PRIME = generate_prime(2**N, 1)[0]
print(PRIME)
print('---------------------')

def hash(input):
    s = 0
    prime = generate_prime(1000, len(input))
    # print("len: ", len(input), prime)
    for char, p in zip(input, prime):
        s = s + ((char) * p ** 3) % (5 ** p)    #lepiej, ale still nie do końca
    # print("s: ", s)
    return s % PRIME

def test_collision():
    BYTES_TO_TEST = 3
    collision_values = set()
    s = set()
    for i in range(2**(N)):
        if hash_int(i) in s:
            collision_values.add(i)
        else:
            s.add(hash_int(i))

    print((collision_values))  

# https://www.geeksforgeeks.org/birthday-attack-in-cryptography/
def test_birthday_int():
    collision_values = set()
    s = set()
    randed = set()
    for i in range(2**(N//2)):
        t = random.randint(0, 2**N)
        randed.add(t)
        # print("i: ", i)
        if hash_int(t) in s:
            # print("i: ", i)
            collision_values.add(t)
        else:
            s.add(hash_int(t))

    print(len(randed))
    print("collision: ", len(collision_values))
    # print(collision_values)     #{30}, {240}, {150}, {95}, {102}


def test_birthday_string():
    collision_values = set()
    s = set()
    randed = set()
    for i in range(2**(N//2)):
        t = random.randint(0, 2**N)
        randed.add(t)
        # print("i: ", i)
        if hash_int(t) in s:
            collision_values.add(t)
        else:
            s.add(hash_int(t))

def generating_testing_values():
    pass

# (test_collision())
test_birthday_int()
# test_values ={'aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah'}



# print(hash_int(128), hash_int(127), hash_int(255), hash_int(254))
            
    
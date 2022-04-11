input = "abc"
import math
import random
import multiprocessing

N=32

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

PRIME = generate_prime(2**32, 1)[0]

print(PRIME)
#print(calc_lower_bound("abcsf"))
def hash(input):
    s = 0
    prime = generate_prime(1000, len(input))
    for char, p in zip(input, prime):
        s += ((char) * pow(p,3,pow(5,p, 1<<N)) % PRIME) 
    return s % (1<<N)


def hash_str(input):
    return hash(bytes(input, 'ascii'))

def how_many_bytes(num: int):
    if num <= 1:
        return 1
    # 0-255 -> 1
    # 256-65535 -> 2 ...
    try:
        return (math.ceil(math.log2(num-1))//8)+1
    except:
        print(num)
        raise ValueError()


def hash_int(input):
    return hash((input).to_bytes(how_many_bytes(input),byteorder="big"))


def xor_bytes(a: bytes, b: bytes):
    return bytes(_a ^ _b for _a, _b in zip(a, b))

def get_bit(num: int, byte_no: int):
    return 1 if num & (1 << byte_no) else 0 

def get_bits(num: int):
    return [get_bit(num, i) for i in reversed(range(8))]

def count_ones(b: bytes):
    count = 0
    for byte in b:
        count += sum(get_bits(byte))
    return count

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


def test_SAC():
    input_size = 2
    input_bits = input_size * 8
    alpha = [1<<i for i in range(input_bits)]
    output_bits_count = N
    output_bytes_count = N//8

    # 1, 2, 4, ... 128
    # f(x) XOR f(x XOR alpha)
    ones_count = 0
    bits_checked = 0
    # for every input with given lenght
    for arg in range(2**input_bits):
        # for every bit 
        for delta_vector in alpha:
 
            # for every output bit compare it with hash with one byte flipped at input
            output_bits, shifted_output_bits = hash_int(arg).to_bytes(output_bytes_count, byteorder='big'), hash_int(arg ^ delta_vector).to_bytes(output_bytes_count, byteorder='big')
            output_diff = xor_bytes(output_bits, shifted_output_bits)
            #print(output_diff)
            ones_count += count_ones(output_diff)
            bits_checked += output_bits_count

    return(ones_count/bits_checked)

# https://www.geeksforgeeks.org/birthday-attack-in-cryptography/
print("dupa")
from alive_progress import alive_bar
def test_birthday_int():
    collision_values = set()
    s = set()
    randed = set()
    with alive_bar(2**(N//2)) as bar:
        for i in range(2**(N//2)):
            t = random.randint(0, 2**N)
            randed.add(t)
            # print("i: ", i)
            if hash_int(t) in s:
                # print("i: ", i)
                collision_values.add(t)
            else:
                s.add(hash_int(t))
            bar()

    print(len(randed))
    print("collision: ", len(collision_values))
    # print(collision_values)     #{30}, {240}, {150}, {95}, {102}
random.seed(0)
def test_rho():
    outputs = []
    msg = random.randint(0, 2**N)
    print("msg:", msg)
    collision = False
    while(not collision):
        hash_msg = hash_int(msg)
        if hash_msg not in outputs:
            outputs.append(hash_msg)
        else:
            collision = True
        msg = hash_msg
    
    index = outputs.index(hash_msg) - 1
    collision_msg = outputs[index]
    print("colision messages:", collision_msg, outputs[-1])
    print("collision after ", len(outputs), "cycles")

test_rho()

def generating_testing_values():
    pass

# (test_collision())
test_birthday_int()
# test_values ={'aaa', 'aab', 'aac', 'aad', 'aae', 'aaf', 'aag', 'aah'}


print(test_SAC())


    
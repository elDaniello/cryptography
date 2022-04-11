input = "abc"
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
    return s % 2**16


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
    for i in range(2**(8*1)):
        if hash_int(i) in s:
            collision_values.add(i)
        else:
            s.add(hash_int(i))

    print((collision_values))        


def test_SAC():
    input_size = 2
    input_bits = input_size * 8
    alpha = [1<<i for i in range(input_bits)]
    output_bits_count = 16
    output_bytes_count = 2

    # 1, 2, 4, ... 128
    # f(x) XOR f(x XOR alpha)
    ones_count = 0
    bits_checked = 0
    # for every input with given lenght
    for arg in range(2**input_bits):
        # for every bit shifted
        for delta_vector in alpha:
 
            # for every output bit compare it with hash with one byte flipped at input
            output_bits, shifted_output_bits = hash_int(arg).to_bytes(output_bytes_count, byteorder='big'), hash_int(arg ^ delta_vector).to_bytes(output_bytes_count, byteorder='big')
            output_diff = xor_bytes(output_bits, shifted_output_bits)
  
            ones_count += count_ones(output_diff)
            bits_checked += output_bits_count

    return(ones_count/bits_checked)
    


print(test_SAC())


    
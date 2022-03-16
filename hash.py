input = "abc"

def hash(input):
    s = 0
    prime = [31, 37, 41]# 43]
    for char, p in zip(input, prime):
        s = s + ord(char) * p 
    return s % 43

print(hash("abc"))
print(hash("auf"))

    
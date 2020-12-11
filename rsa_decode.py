# RSA cipher implementation by Bohdan Pakhomov
def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)

def pow_mod(x, y, z):
    # Calculate (x ** y) % z efficiently
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number

def get_d(e, phi):
    d = pow_mod(e, (phi_func(phi)-1), phi)
    return d

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q
    #Phi is the totient of n
    phi = (p-1) * (q-1)
    #Choose an integer e such that e and phi(n) are coprime
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    #Use Extended Euclid's Algorithm to generate the private key
    d = get_d(e, phi)
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = ""
    for c in ciphertext:
        i = ord(c)-ord('A')
        enc = pow_mod(i, key, n)
        plain += chr(enc+ord('A'))
    #Return the array of bytes as a string
    return plain

if __name__ == '__main__':
    print("RSA Decrypter")
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    e = int(input("Enter e: "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public ," and your private key is ", private)

    with open('output_rsa.txt', 'r') as f:
         message = f.read().replace(' ', '').upper().replace('\n', '')

    print("Encrypted msg:", message)

    print("Decrypting message with private key ", private ," . . .")
    print("Your message is:")
    decrypted = decrypt(private, message)
    print(decrypted)

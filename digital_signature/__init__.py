import math


def generate_public_n_private_keys(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    d = 2
    while 1 < d < m:
        if math.gcd(d, m) == 1:
            break
        else:
            d += 1
    e = 2
    while True:
        if (e * d) % m == 1:
            break
        else:
            e += 1
    public_key = (e, n)
    private_key = (d, n)
    return public_key, private_key


def encrypt(m, public_key):
    e, n = public_key
    if m > n:
        raise ValueError('m is greater than n')
    else:
        return (m ** e) % n


def decrypt(c, private_key):
    d, n = private_key
    return (c ** d) % n


def encrypt_string(string, public_key):
    return [encrypt(ord(integer), public_key) for integer in string]


def decrypt_string(encrypted_string, private_key, encoding='utf-8'):
    return ''.join([chr(decrypt(integer, private_key)) for integer in encrypted_string])

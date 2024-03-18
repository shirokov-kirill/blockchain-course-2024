import hashlib
from digital_signature import generate_public_n_private_keys, encrypt_string, decrypt_string


class Rsa:

    def __init__(self):
        pass

    def generate_keys(self, p, q):
        public_key, private_key = generate_public_n_private_keys(p, q)
        return public_key, private_key

    def sign_string(self, text: bytes, private_key):
        h = hashlib.new('sha512_256')
        h.update(text)
        return encrypt_string(h.hexdigest(), private_key)

    def verify_signature(self, signed_str, text: bytes, public_key):
        h_a = decrypt_string(signed_str, public_key)
        h_b = hashlib.new('sha512_256')
        h_b.update(text)
        if h_a == h_b.hexdigest():
            return True
        else:
            return False
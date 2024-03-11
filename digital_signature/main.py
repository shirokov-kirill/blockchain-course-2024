from rsa import Rsa


def try_read_from_file(file_path):
    mode = 'r' if file_path.endswith('.txt') else 'rb'
    try:
        with open(file_path, mode=mode) as file:
            return file.read()
    except:
        print("File not found in destination: " + file_path)
        return None


def write_to_file_output(text: str):
    try:
        with open("output.txt", "w") as output:
            output.write(str(text))
    except FileNotFoundError:
        print("File not found.")


def digital_signature_example():
    print('Enter path to the .txt file:')
    file_path = input("> ")
    text = try_read_from_file(file_path)
    if text is None:
        print("Nothing to encrypt.")
        return
    text = text.encode() if not isinstance(text, bytes) else text
    rsa_algo = Rsa()
    public_key, private_key = rsa_algo.generate_keys(11, 13)
    signature = rsa_algo.sign_string(text, private_key)

    if signature_valid := rsa_algo.verify_signature(signature, text, public_key):
        write_to_file_output(signature)
        print(f"""Encryption done.
Original message was: {text}

Signature validity: {str(signature_valid)}.""")
    else:
        print(f"""
Something went wrong.

Signature validity: {str(signature_valid)}.
""")


if __name__ == '__main__':
    digital_signature_example()

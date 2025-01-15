![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/TSCCTF%202025/Crypto/Classic/Chall.PNG)

```py
import os
import string
import secrets
import math

# Charset used for encoding and decoding
charset = string.digits + string.ascii_letters + string.punctuation

# Function to check if two numbers are coprime
def are_coprime(a, b):
    return math.gcd(a, b) == 1

# Function to compute modular inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Function to try decoding until the flag starts with 'TSC{'
def find_flag(enc_flag):
    while True:
        # Generate random A and B
        A = secrets.randbelow(2**32)
        B = secrets.randbelow(2**32)

        # Ensure A and len(charset) are coprime
        while not are_coprime(A, len(charset)):
            A = secrets.randbelow(2**32)

        # Check the uniqueness condition for the charset
        if len(set((A * x + B) % len(charset) for x in range(len(charset)))) != len(charset):
            continue  # If not unique, try again

        # Calculate modular inverse of A
        A_inv = modinv(A, len(charset))

        # Decrypt the encrypted flag
        dec_flag = []
        for enc_char in enc_flag:
            enc_index = charset.find(enc_char)
            original_index = (enc_index - B) * A_inv % len(charset)
            dec_flag.append(charset[original_index])

        # Join the decoded characters to form the flag
        decoded_flag = ''.join(dec_flag)

        # Check if the decoded flag starts with 'TSC{'
        if decoded_flag.startswith('TSC{'):
            return decoded_flag  # Return the decoded flag if it matches the expected pattern

# Read the encrypted flag from flag.txt
with open('flag.txt', 'r') as file:
    enc_flag = file.read().strip()

# Try decoding until we find the correct flag
decoded_flag = find_flag(enc_flag)

# Print the decoded flag
print("Decoded Flag:", decoded_flag)
```

### Output:

```py
Decoded Flag: TSC{c14551c5_c1ph3r5_4r5_fr4g17e}
```

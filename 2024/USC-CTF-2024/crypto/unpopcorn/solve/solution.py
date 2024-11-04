import string

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(p, m):
    gcd, x, y = extended_gcd(p, m)
    if gcd != 1:
        return None 
    else:
        return x % m

def unpop(message_hex, p, m):
    message = [int(x, 16) for x in message_hex.split()]

    n = len(message)
    half = n // 2
    message = message[half:] + message[:half] 
    message = [(x >> 3) for x in message] 

    p_inv = mod_inverse(p, m)
    if p_inv is None:
        return None 

    message = [(x * p_inv % m) for x in message]

    original_message = ''.join(chr(x ^ 42) for x in message)

    if all(c in string.printable for c in original_message):
        return original_message
    else:
        return None

message_hex = "3FB60 4F510 42930 31058 DEA8 4A818 DEA8 1AA88 65AE0 1C590 17898 1C590 29170 3FB60 55D10 29170 42930 6A7D8 4C320 4F510 5FC0 193A0 4F510 2E288 29170 643F8 31058 6A7D8 4A818 1AA88 1AA88"
m = 57983

for p in range(1, m):
    flag = unpop(message_hex, p, m)
    if flag:
        print(f"Potential flag with p={p}: {flag}")

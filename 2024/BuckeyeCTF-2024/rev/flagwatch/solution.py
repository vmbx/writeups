def decode_flag():
    encrypted_flag = [62, 63, 40, 58, 39, 40, 111, 63, 52, 50, 53, 63, 104, 48, 48, 37, 3, 61, 3, 55, 57, 37, 48, 108, 59, 59, 111, 46, 33]
    decrypted_flag = ""

    # XOR each encrypted byte with 92 to get the original character
    for value in encrypted_flag:
        decrypted_flag += chr(value ^ 92)

    return decrypted_flag

if __name__ == "__main__":
    flag = decode_flag()
    print(f"Decrypted Flag: {flag}")

def rot47(char, shift):
    if 33 <= ord(char) <= 126:
        return chr(33 + ((ord(char) - 33 + shift) % 94))
    return char

def decode_rot47(encoded_str, shift):
    decoded_str = ''.join(rot47(char, shift) for char in encoded_str)
    return decoded_str

encoded_string = "( . # ) = u * M 1 * M M M y 1 7 M 5 * 1 7 . & M * # 8 ' M . ' 6 M * ' 4 M s l e e p M b r o A M Z o ?"

for shift in range(1, 63):
    decoded_string = decode_rot47(encoded_string, shift)
    print(f"Shift {shift}: {decoded_string.replace(' ', '')}")

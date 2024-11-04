### Drink Up

- **Description:** The challenge involved analyzing a can with the company name **XXTEA**. The steps to retrieve the flag included base64 decoding followed by XXTEA decryption. The key used for decryption was **"Tea Turned Up to the Max!"**. The flag was extracted from the decrypted text.
- **Steps:**

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Cryptography/Drink%20Up/drink.png)

  1. **Base64 Decode** the provided string.
  2. **XXTEA Decrypt** the resulting text using the key.
- **Encoded Text:**
  ```
  zxk1ehfZ/kx7tzSyQeSm2XuGitnxsN8rG/mwxNaCjFFc2rCrTTWpwViZFpwI4xRccvdwm/Ta6l3GFeaPs96l7BPziIu+DsfoS6bdy5ByHSyW+D5bCgtTCuoVvMOlPC7xILtjlt6/Ky6ZPaV40gfmtM/iuRGR+zveFLNyWy9Tlu3TnOaq0lP6wp65lGEFBTHPSwho0jIP47pxoKryxnh7svJrTD1wh+D+YudNjDpPr39yH/iMlU+5xiK2dXjiD0UtL3vSSQ55MLCPpN/kFW6AuO2OEuadKXg2XYiXnAkLJcUxGdZhP7+Lo4LG3m5HsHdBmul5pX9gcvERFQSZOy2QfEv3+vRfLfoJPq6WQnBjwXUoVo/YHeD8SS+TDvg=
  ```

![image1](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Cryptography/Drink%20Up/solution.png)

- **Flag:** `flag{br3wed_4_the_B0ld!}`

---

### Ides-le Talk

- **Description:** This challenge required a simple **ROT13** decoding of the text to obtain the flag. ROT13 is a letter substitution cipher that replaces a letter with the 13th letter after it in the alphabet.

![image2](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Cryptography/Ides-le%20Talk/flag.png)

- **Flag:** `flag{L3t The#Mischiefs^8361n}`

---

### Social Pressure

- **Description:** The objective of this challenge was to decode a message using the **Atbash** cipher, which substitutes letters in a mirrored alphabet. After decoding, the name was extracted and formatted within the flag.

![image3](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Cryptography/Social%20Pressure/flag.png)

- **Flag:** `flag{Elroy_Ongaro}`

---

### Sleeping (Marble) Beauty

- **Description:** This challenge required a simple **ROT47** decoding of the text to obtain the flag.

```
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
```

![image4](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Cryptography/Sleeping%20(Marble)%20Beauty/flag.png)

- **Flag:** `flag{Uh-oh---You-should-have-let-her-SLEEP-BRO!-:O}`

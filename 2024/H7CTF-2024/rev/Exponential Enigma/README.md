# rev - Exponential Enigma

![Challenge](https://github.com/x03ee/CTF-Writeup/blob/main/2024/H7CTF-2024/rev/Exponential%20Enigma/challenge.png)

### Solution:

1. **Function Purpose**:
   - The `tetra` function calculates powers of 2 multiple times and manages large numbers to avoid errors. It returns a final result based on those calculations.

2. **Creating a List of Values**:
   - The `main` function calls the `tetra` function four times, with increasing numbers each time.
   - It uses the results to create a list (`var_38`) by making some adjustments to those results.

3. **Decoding the Message**:
   - The code has a long string in hexadecimal format, which represents some encoded information.
   - It converts this string into bytes (raw data).
   - Then, it processes each byte one by one:
     - For each byte, it picks a value from the list (`var_38`).
     - It combines (XORs) the byte with that value to get a character.
   - It collects these characters to form a readable message.

4. **Output**:
   - Finally, the decoded message is printed out, revealing the hidden information from the original hexadecimal string.

![Challenge](https://github.com/x03ee/CTF-Writeup/blob/main/2024/H7CTF-2024/rev/Exponential%20Enigma/flag.png)

### Final Flag:
```
H7CTF{78febc551a1f259113e4805fa183e024}
```

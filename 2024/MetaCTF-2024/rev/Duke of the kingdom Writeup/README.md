# Rev - Duke of the kingdom Writeup
### Solution:

This challenge involves decoding an encoded message extracted from the `duke.class` file. The process is detailed below:

### Step-by-Step Solution:

1. **Decompile the Class File:**
   Use **Jadx Gui** to decompile `duke.class`. This tool will help you view the source code in a human-readable format, allowing you to locate the encoded data.
   
![Jadx Gui](https://github.com/x03ee/MetaCTF-WriteUps/blob/main/rev/Duke%20of%20the%20kingdom%20Writeup/images/jadx%20gui.png)

3. **Encoded Data:**
   The encoded data is provided as an integer array. Each integer represents an encoded byte value:
```986, 995, 338, 950, 1103, 1013, 959, 338, 986, 959, 1076, 959, 401, 1085, 338, 923, 338, 968, 1022, 923, 977, 338, 968, 1049, 1076, 338, 1139, 1049, 1103, 338, 1031, 959, 1094, 923, 941, 1094, 968, 1157, 950, 1103, 1013, 509, 905, 923, 1094, 905, 1094, 986, 509, 905, 1094, 482, 1058, 905, 482, 968, 905, 1094, 986, 509, 995, 1076, 905, 941, 1022, 518, 1085, 1085, 1175```

4. **Decoding Formula:**
The integers are encoded using the formula:
`encoded_value = (byte[i] * 9) + 50`
To retrieve the original byte values, reverse the encoding formula:
`byte[i] = (encoded_value - 50) / 9`

5. **Decoding Process:**
- **Calculate Byte Values:** Apply the formula to each integer in the encoded array to find the original byte values.
- **Convert Byte Values to Characters:** Use ASCII encoding to convert the byte values into characters. The result will be a string that represents the flag.

### Python Code:

Here’s the Python code to automate the decoding process:

```python

iArr = [986, 995, 338, 950, 1103, 1013, 959, 338, 986, 959, 1076, 959, 401, 1085, 338, 923, 338, 968, 1022, 923, 977, 338, 968, 1049, 1076, 338, 1139, 1049, 1103, 338, 1031, 959, 1094, 923, 941, 1094, 968, 1157, 950, 1103, 1013, 509, 905, 923, 1094, 905, 1094, 986, 509, 905, 1094, 482, 1058, 905, 482, 968, 905, 1094, 986, 509, 995, 1076, 905, 941, 1022, 518, 1085, 1085, 1175]

flag_bytes = [(n - 50) // 9 for n in iArr]
flag = ''.join(chr(b) for b in flag_bytes)

print("Flag:", flag)
# Output: metactf{duk3_at_th3_t0p_0f_th3ir_cl4ss}
```
### Final Flag:
```
metactf{duk3_at_th3_t0p_0f_th3ir_cl4ss}
```

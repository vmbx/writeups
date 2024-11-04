## Twice the Trouble

### Description

In this challenge, you'll be given an encoded flag. Your task is to decode the flag using an XOR cipher. The encoding method used was the XOR Cipher, and you can decode it with the help of the tool available at [Dcode XOR Cipher](https://www.dcode.fr/xor-cipher).

The flag format is: `QUESTCON{...}`.

### Challenge Steps

1. **Retrieve the Encoded Flag:**  
   You will be provided with an encoded version of the flag during the challenge.

2. **Identify XOR Cipher Key:**  
   Use logical deduction or trial and error to determine the key used to XOR the flag.

3. **Decode the Flag:**
   - Go to [Dcode XOR Cipher Tool](https://www.dcode.fr/xor-cipher).
   - Input the encoded flag and the key you deduced.
   - Decode the flag to reveal the original text.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/QuestconCTF-2024/Reverse/Twice%20the%20Trouble/p1.png)

![image1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/QuestconCTF-2024/Reverse/Twice%20the%20Trouble/flag.png)

4. **Submit the Flag:**  
   Once decoded, the flag will be in the format `QUESTCON{doub13_troub13}`.



### Tools & Resources

- [Dcode XOR Cipher Tool](https://www.dcode.fr/xor-cipher)

---

## Unlock the Encrypted Flag

### Description

In this challenge, you are tasked with unlocking an encrypted flag by analyzing a Python utility. Upon inspecting the source code, you will discover the XOR key used for encryption, which you can then use to decode the flag.

The flag format is: `QUESTCON{...}`.

### Challenge Steps

1. **View Source of the Python Utility:**
   - Carefully inspect the Python script provided.
   - Look for any hardcoded XOR key within the script.

2. **Find the XOR Key:**
   - Identify the key used for encryption in the Python source.

3. **Decode the Flag:**
   - Using the identified XOR key, decode the encrypted flag.

![image2](https://github.com/x03ee/CTF-Writeup/blob/main/2024/QuestconCTF-2024/Reverse/Unlock%20the%20Encrypted%20Flag/p1.png)

![image3](https://github.com/x03ee/CTF-Writeup/blob/main/2024/QuestconCTF-2024/Reverse/Unlock%20the%20Encrypted%20Flag/flag.png)

4. **Submit the Flag:**  
   Once decoded, the flag will be in the format `QUESTCON{3ncrypt3d_f14g_r3v341}`.
   
---

## Unlock the Safe

### Description

In this challenge, your task is simple: view the Python source code to find a Base64 encoded string. Once found, decode the string to reveal the flag.

The flag format is: `QUESTCON{...}`.

### Challenge Steps

1. **View the Python Source Code:**
   - Inspect the Python script to locate a Base64 encoded string.

2. **Decode the Base64 String:**
   - Copy the Base64 encoded string and use any online decoder, such as [Base64 Decode](https://www.base64decode.org/), to decode it.

![image4](https://github.com/x03ee/CTF-Writeup/blob/main/2024/QuestconCTF-2024/Reverse/Unlock%20the%20Safe/flag.png)

3. **Submit the Flag:**  
   Once decoded, the flag will be in the format `QUESTCON{pl3as3_13t_m3_1nt0_th3_saf3}`.

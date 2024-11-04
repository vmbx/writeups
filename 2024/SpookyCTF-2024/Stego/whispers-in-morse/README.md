# Whisperz in Morse

![image](https://github.com/x03ee/SpookyCTF-2024/blob/main/Stego/whispers-in-morse/MaryMorse.jpg)

## Description

In this challenge, titled **Whisperz in Morse**, participants must extract a hidden flag from the provided image file `MaryMorse.jpg` using steganography techniques.

![image1](https://github.com/x03ee/SpookyCTF-2024/blob/main/Stego/whispers-in-morse/strings.png)

## Steps to Solve

1. **Extract the Flag:**
   To extract the hidden content from the image, use the following command:

   ```bash
   steghide extract -sf MaryMorse.jpg
   ```

2. **Password:**
   During the extraction process, you will be prompted for a password. Use the following key:

   ```
   M.A.__.R.Y
   ```

3. **Retrieve the Flag:**
   After successfully entering the password, a file named `flag.txt` will be created. Open this file to reveal the flag.

## Flag

```
NICC{tHe_whIspeRz_iN_Th3_aiR}
```

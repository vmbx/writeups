# Crypto - Mmm, Birthday Cake Writeup

## Challenge Overview

This challenge requires cracking a password-protected ZIP file using the tool `zip2john` and `john`. The password obtained reveals the flag.

## Step-by-Step Solution

1. **Download and Install `zip2john`:**  
   Ensure that you have `John the Ripper` and the `zip2john` utility installed. If you don't have them installed, you can download `John the Ripper` [here](https://www.openwall.com/john/), which includes the `zip2john` tool.

2. **Convert the ZIP file to a Hash:**  
   Use `zip2john` to extract the hash from the ZIP file. This hash is necessary for cracking the password.
   
   ```bash
   zip2john birthdaycake.zip > birthdaycake.hash
   ```

   This command reads the ZIP file `birthdaycake.zip` and outputs its hash to a file called `birthdaycake.hash`.

3. **Crack the Password with John the Ripper:**  
   Now, use `John the Ripper` to crack the password using the hash extracted in the previous step.
   
   ```bash
   john birthdaycake.hash
   ```

   John the Ripper will start trying different password combinations based on its internal wordlists or configurations. Once it finds the correct password, it will display it on the screen.

4. **Reveal the Cracked Password:**  
   After John the Ripper finishes cracking the password, you can use the following command to display the cracked password.
   
   ```bash
   john --show birthdaycake.hash
   ```

   This will show the extracted password and the file(s) associated with it. The cracked password is:

   ```
   060450
   ```

5. **Extract the Flag from the ZIP File:**  
   Now that we have the password (`060450`), you can unzip the `birthdaycake.zip` file using that password to reveal the flag.
   
   ```bash
   unzip birthdaycake.zip
   ```

   The flag contained inside is:

   ```
   MetaCTF{th3_b1rthd4y_c4k3_w4s_n0t_a_li3}
   ```

![John Output](https://github.com/x03ee/MetaCTF-WriteUps/blob/main/crypto/Mmm%2C%20Birthday%20Cake/images/john.PNG)

### Final Flag:

```
MetaCTF{th3_b1rthd4y_c4k3_w4s_n0t_a_li3}
```

This step-by-step solution demonstrates how to use `zip2john` and `john` to crack the password and retrieve the flag from a password-protected ZIP file.

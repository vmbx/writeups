## YoDawg Misc Challenge

```
We found this file on a USB drive, it seems to be some sort of gamified cyber skilled based learning system thingy?

Maybe if all of the challenges are sold we will get some answers, or maybe it is just the friends we make along the way.

Note - This may produce false positives with your virus scanner.
```

### The Files Given:

* `Yo Dawg.dll`
* `Yo Dawg.exe`
* `Yo Dawg.deps.json`
* `Yo Dawg.runtimeconfig.json`

Running `Yo Dawg.exe` presents a series of challenges.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo1.png)

We can extract flags from the DLL using a tool called `dnspy`.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo2.png)

After completing all the challenges, we reach the final one, titled "Form3".
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo3.png)

Upon inspecting the source code of Form3, we find a message box with the string `C0RR3CT`. The string `vjN5+ZTZgMGQ9d4rhzf+9g==` is encrypted with an `AES` cipher.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo4.png)

### The Decryption Code:

The method for decryption is defined in the following code:

```c
private string b(string A_0)
{
    string @string;
    try
    {
        using (Aes aes = Aes.Create())
        {
            aes.Key = this.aesKey;
            aes.IV = this.aesIV;
            aes.Mode = CipherMode.CBC;
            aes.Padding = PaddingMode.PKCS7;
            ICryptoTransform cryptoTransform = aes.CreateDecryptor(aes.Key, aes.IV);
            byte[] array = Convert.FromBase64String(A_0);
            byte[] array2 = cryptoTransform.TransformFinalBlock(array, 0, array.Length);
            @string = Encoding.UTF8.GetString(array2);
        }
    }
    catch (Exception ex)
    {
    }
    return @string;
}
```

We can see that `aes.Key` and `aes.IV` are being set from variables defined in the form's code:

```c
this.aesKey = Encoding.UTF8.GetBytes(this.flagmiddle11);
this.aesIV = Encoding.UTF8.GetBytes(this.flagmiddle9);
```

Where `this.flagmiddle11` and `this.flagmiddle9` are defined as:

```c
this.aesKey = Encoding.UTF8.GetBytes(this.flagmiddle11);
this.aesIV = Encoding.UTF8.GetBytes(this.flagmiddle9);
```

### The AES Key and IV:

After extraction:

```c
this.aesKey = b"qwertyuiopasdfghjklzxcvbnmNOSURF"
this.aesIV = b"0123456789DUCTF!"
```

We can use Python to decrypt the encrypted string:

```python
from base64 import b64decode
from Crypto.Cipher import AES

b64_ciphertext = "vjN5+ZTZgMGQ9d4rhzf+9g=="
key = b"qwertyuiopasdfghjklzxcvbnmNOSURF"
iv = b"0123456789DUCTF!" 

ciphertext = b64decode(b64_ciphertext)
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Remove padding
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

print("Decrypted:", plaintext.decode('utf-8'))
```

Output:

```python
Decrypted: flag{des4eva}
```

### Next Step:

After inputting this flag, we proceed to the final stage of the challenge.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo5.png)

![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo6.png)

For the final decryption, we apply a similar process, but this time using DES encryption.

```python
from Crypto.Cipher import DES
import base64

cipher_b64 = 'UDR6b0HwIOkbJ90U/dYB3iSF5iQ50Ci1b+T+YCQPJA3pl9IFtyJFrCWfB1szPlKy5EdvDb029rZ7w2gUAcSJiQ=='
key = b'hack\x00\x00\x00\x00'
iv = b'\x00' * 8

ciphertext = base64.b64decode(cipher_b64)
cipher = DES.new(key, DES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Manually unpad (PKCS#5/7)
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

print(plaintext.decode())
```

Output:

```python
Here's the final flag: DUCTF{1995_to_2025}
```

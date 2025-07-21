# YoDawg Misc Challenge

```
We found this file on a USB drive, it seems to be some sort of gamified cyber skilled based learning system thingy?

Maybe if all of the challenges are sold we will get some answers, or maybe it is just the friends we make along the way.

Note - This may produce false positives with your virus scanner.
```
We are givene:

* `Yo Dawg.dll`
* `Yo Dawg.exe`
* `Yo Dawg.deps.json`
* `Yo Dawg.runtimeconfig.json`

When running Yo Dawg.exe, challenges are given.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo1.png)

Flags for the challenges appear inside the dll using the tool dnspy.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo2.png)

After solving everything, head to the final challenge which is 'Form3'.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo3.png)

Viewing source of Form3, we spot message box, `C0RR3CT`. The string `vjN5+ZTZgMGQ9d4rhzf+9g==` is encrypted with `b`.

![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo4.png)

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
We can identify `aes.Key = this.aesKey;	aes.IV = this.aesIV;`. In the Form.
```c
this.g = false;
this.h = false;
this.i = false;
this.flagstart = "DUCTF{";
this.flagmiddle1 = "v398mvaUv==";
this.flagmiddle2 = "_never";
this.flagmiddle3 = "_oldschool";
this.flagmiddle4 = "miMIdmav39av827NAfm2";
this.flagmiddle5 = "_shoutout";
this.flagmiddle6 = "_ready";
this.flagmiddle7 = "_end";
this.flagmiddle8 = "_trim";
this.flagmiddle9 = "0123456789DUCTF!";
this.flagmiddle10 = "0987654321DUCTF!";
this.flagmiddle11 = "qwertyuiopasdfghjklzxcvbnmNOSURF";
this.flagmiddle12 = "NOSURFqwertyuiopasdfghjklzxcvbnm";
this.flagmiddle13 = "PADDING";
this.flagmiddle14 = "_hackers";
this.flagmiddle15 = "_jolt";
this.flagmiddle16 = "bmV2ZXJnb25uYWdpdmV5b3V1cA==";
this.flagend = "}";
this.aesKey = Encoding.UTF8.GetBytes(this.flagmiddle11);
this.aesIV = Encoding.UTF8.GetBytes(this.flagmiddle9);
```
```c
this.aesKey = Encoding.UTF8.GetBytes(this.flagmiddle11);
this.aesIV = Encoding.UTF8.GetBytes(this.flagmiddle9);
```
### After:
```c
this.aesKey = qwertyuiopasdfghjklzxcvbnmNOSURF
this.aesIV = 0123456789DUCTF!
```
We can create a py to decrpyt the string
```py
from base64 import b64decode
from Crypto.Cipher import AES

b64_ciphertext = "vjN5+ZTZgMGQ9d4rhzf+9g=="
key = b"qwertyuiopasdfghjklzxcvbnmNOSURF"
iv = b"0123456789DUCTF!" 

ciphertext = b64decode(b64_ciphertext)
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

print("Decrypted:", plaintext.decode('utf-8'))
```
```py
Decrypted: flag{des4eva}
```
One we input inside the right box it takes us to the last step.
![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo5.png)

![image](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/misc/YoDawg/images/yo6.png)
Using the same step as question 1, we can create a py script.

```py
from Crypto.Cipher import DES
import base64

cipher_b64 = 'UDR6b0hwIOkbJ90U/dYB3iSF5iQ50Ci1b+T+YCQPJA3pl9IFtyJFrCWfB1szPlKy5EdvDb029rZ7w2gUAcSJiQ=='
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
```py
Here's the final flag: DUCTF{1995_to_2025}
```

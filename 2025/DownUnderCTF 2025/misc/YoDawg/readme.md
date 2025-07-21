# YoDawg Misc Challenge

```
We found this file on a USB drive, it seems to be some sort of gamified cyber skilled based learning system thingy?

Maybe if all of the challenges are sold we will get some answers, or maybe it is just the friends we make along the way.

Note - This may produce false positives with your virus scanner.
```

![image]()


```py
from Crypto.Cipher import DES
import base64

cipher_b64 = 'UDR6b0hwIOkbJ90U/dYB3iSF5iQ50Ci1b+T+YCQPJA3pl9IFtyJFrCWfB1szPlKy5EdvDb029rZ7w2gUAcSJiQ=='
key = b'hack\x00\x00\x00\x00'
iv = b'\x00' * 8  # Default IV (nulls)

ciphertext = base64.b64decode(cipher_b64)
cipher = DES.new(key, DES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

# Manually unpad (PKCS#5/7)
pad_len = plaintext[-1]
plaintext = plaintext[:-pad_len]

print(plaintext.decode())
```

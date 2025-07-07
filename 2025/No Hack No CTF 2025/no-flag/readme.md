No Flag?
```
Nothing much, just a photo of a cat.
```

```                                                             
┌──(kali㉿kali)-[~/Downloads]
└─$ stegseek  flag.jpg ./rockyou.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "1313"
[i] Original filename: "flag.txt".
[i] Extracting to "flag.jpg.out".
```
`https://youtu.be/KLUeLae4y6k?t=11 ‌` Identified blank byte, which stores the flag.

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p1.png)

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p2.png)

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p3.png)
​
![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p4.png)

```py
hex_data = bytes.fromhex(
    "b1b7b1bc8485cc8dcfd288ce9bab97a0"
    "ca8fcb9cccd2d2c1cea085cc8dcfd2a8"
    "ce9bb7a091cf91d295cfceb1cc8dd2d2"
    "c1cfa09ccfcf93dededededede82f5"
)
decoded = bytes(b ^ 0xFF for b in hex_data)
print(decoded.decode('ascii'))
### NHNC{z3r0-w1dTh_5p4c3-->1_z3r0-W1dH_n0n-j01N3r-->0_c00l!!!!!!}
``​​​‌‌​‌‌​‌‌‌‌​‌‌​​​‌‌​‌‌‌‌​​‌​​​​‌​​‌​​​​‌​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​​‌‌‌‌‌‌​‌​​‌​‌​​​‌​​​‌‌​​‌‌‌​‌​​‌‌​‌‌‌​‌​‌​‌‌‌​​‌​‌‌‌‌​‌​​​​​‌‌​​‌​‌​‌​​​‌‌‌‌‌‌​​‌​‌‌‌​​‌‌‌​​‌‌​​‌‌​​‌‌​‌​​‌​‌‌​‌​​‌​‌‌​​​​​‌‌‌​​‌‌‌​‌​‌​​​​​‌​​​​‌​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​​‌‌‌‌‌‌​‌​​‌​‌​‌​‌​​​‌‌​​‌‌‌​‌​​‌‌​‌‌‌​‌‌​‌‌‌‌​‌​​​​​‌​​‌​​​‌‌‌​​‌‌‌‌‌​​‌​​​‌‌‌​‌​​‌​‌​​‌​‌​‌‌‌​​‌‌‌‌‌‌​​‌‌‌​‌​‌‌​​​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​‌​​‌​‌‌​‌​​‌​‌‌​​​​​‌‌‌​​‌‌‌‌‌​‌​​​​​‌​​‌‌‌​​‌‌​​‌‌‌‌‌‌​​‌‌‌‌‌​​‌​​‌‌‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​`

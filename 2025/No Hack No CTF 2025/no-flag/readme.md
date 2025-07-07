### No Flag?
```
Nothing much, just a photo of a cat.
```

![unicode stegano tool](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/blood.png)

But let's dig deeper...

```bash
┌──(kali㉿kali)-[~/Downloads]
└─$ stegseek flag.jpg ./rockyou.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "1313"
[i] Original filename: "flag.txt".
[i] Extracting to "flag.jpg.out".
```

Using StegSeek, we discover a hidden file (`flag.txt`) embedded in `flag.jpg` using the password `1313`.

Inside the flag.txt -> `https://youtu.be/KLUeLae4y6k?t=11 ‌​‌‌​​​‌‌​‌‌​‌‌‌‌​‌‌​​​‌‌​‌‌‌‌​​‌​​​​‌​​‌​​​​‌​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​​‌‌‌‌‌‌​‌​​‌​‌​​​‌​​​‌‌​​‌‌‌​‌​​‌‌​‌‌‌​‌​‌​‌‌‌​​‌​‌‌‌‌​‌​​​​​‌‌​​‌​‌​‌​​​‌‌‌‌‌‌​​‌​‌‌‌​​‌‌‌​​‌‌​​‌‌​​‌‌​‌​​‌​‌‌​‌​​‌​‌‌​​​​​‌‌‌​​‌‌‌​‌​‌​​​​​‌​​​​‌​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​​‌‌‌‌‌‌​‌​​‌​‌​‌​‌​​​‌‌​​‌‌‌​‌​​‌‌​‌‌‌​‌‌​‌‌‌‌​‌​​​​​‌​​‌​​​‌‌‌​​‌‌‌‌‌​​‌​​​‌‌‌​‌​​‌​‌​​‌​‌​‌‌‌​​‌‌‌‌‌‌​​‌‌‌​‌​‌‌​​​‌‌‌​​‌‌​​‌​​​‌‌​‌‌‌​‌​​‌​‌‌​‌​​‌​‌‌​​​​​‌‌‌​​‌‌‌‌‌​‌​​​​​‌​​‌‌‌​​‌‌​​‌‌‌‌‌‌​​‌‌‌‌‌​​‌​​‌‌‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌‌​‌‌‌‌​‌​​​​​‌​‌‌‌‌​‌​‌`, where a zero-width character is identified in blank.

Using [this Unicode Steganography tool](https://330k.github.io/misc_tools/unicode_steganography.html), we analyze the extracted content. It turns out zero-width characters like `U+200C` (Zero Width Non-Joiner) and `U+200B` (Zero Width Space) were used to encode binary data.

![unicode stegano tool](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p1.png)

Feeding the suspicious text into [CyberChef](https://gchq.github.io/CyberChef/), under the Unicode analysis section, we confirm the presence of these characters.

![cyberchef decoding](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p2.png)

Once decoded, we download the revealed hidden file.

![download hidden file](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p3.png)

We inspect the contents using `xxd` to view the raw hex data:

![xxd output](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p4.png)

The content is XOR-encoded, so we decode it with the following Python script:

```python
hex_data = bytes.fromhex(
    "b1b7b1bc8485cc8dcfd288ce9bab97a0"
    "ca8fcb9cccd2d2c1cea085cc8dcfd2a8"
    "ce9bb7a091cf91d295cfceb1cc8dd2d2"
    "c1cfa09ccfcf93dededededede82f5"
)
decoded = bytes(b ^ 0xFF for b in hex_data)
print(decoded.decode('ascii'))
# NHNC{z3r0-w1dTh_5p4c3-->1_z3r0-W1dH_n0n-j01N3r-->0_c00l!!!!!!}
```


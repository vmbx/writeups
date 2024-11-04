# Forensic Challenge - Wreck

![Challenge](https://github.com/x03ee/BuckeyeCTF-2024/blob/main/forensic/wreck/challenge.PNG)

## Solution
To tackle this challenge, I utilized **Foremost** to extract files from the provided dump. By running the command `./foremost dump`, I successfully recovered various files, including a folder containing JPEG images.

Upon inspecting the extracted files, I discovered a PNG image containing the flag.

![Extracted PNG Flag](https://github.com/x03ee/BuckeyeCTF-2024/blob/main/forensic/wreck/flag.jpg)

## Final Flag
```
bctf{D4MN_7h47_c0r3_dvmp_907_4_GY477}
```

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/USC-CTF-2024/forensics/Computer%20Has%20Virus/solve/chall.png)

Editing using notepad we find a file .exe encoded with base64.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/USC-CTF-2024/forensics/Computer%20Has%20Virus/solve/s1.png)

Now we decode the base64 using cyberchef.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/USC-CTF-2024/forensics/Computer%20Has%20Virus/solve/s2.png)

Inputing the exe into dnspy we found a .ps1 powershell script that has a base64 string encoded.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/USC-CTF-2024/forensics/Computer%20Has%20Virus/solve/s3.png)

Decoding the powershell script with base64 we could decode using powershell.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/USC-CTF-2024/forensics/Computer%20Has%20Virus/solve/flag.png)

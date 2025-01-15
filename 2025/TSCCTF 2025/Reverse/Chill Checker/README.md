![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/TSCCTF%202025/Reverse/Chill%20Checker/Chall.PNG)

I found the whispercode.  
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/TSCCTF%202025/Reverse/Chill%20Checker/BinaryNinja.PNG)

After analyzing the binary, I modified `Jle` to `jg` to make the condition true, allowing the flag to print when debugging on Linux.  
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/TSCCTF%202025/Reverse/Chill%20Checker/Ida.PNG)

Using `strace` or `ltrace`, I input the whispercode and observed the output.  
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/TSCCTF%202025/Reverse/Chill%20Checker/Flag.PNG)


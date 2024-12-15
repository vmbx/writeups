### "Administrator" Username Found

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/You%20know%20I%20know%20the%20token/1.png)

### Output When Importing the Username

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/You%20know%20I%20know%20the%20token/2.png)

### Finding the Function That Produces the Output and Modifying the Logic

Here, we locate the function responsible for the output and reverse its logic. Specifically, we change the instruction from `jnz` (jump if not zero) to `jz` (jump if zero).

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/You%20know%20I%20know%20the%20token/3.png)

### Flag

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/You%20know%20I%20know%20the%20token/flag.png)

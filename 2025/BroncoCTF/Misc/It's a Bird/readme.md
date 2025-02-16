### It's a Bird

`steghide extract -sf myBirb.jpg` wrote extracted data to "birb.csv".


Anything within the R collom / MSG 6. 
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/BroncoCTF/Misc/It's%20a%20Bird/image.png)

```py
ascii_values = [98, 114, 111, 110, 99, 111, 123, 105, 60, 51, 112, 108, 97, 110, 101, 115, 125]

decoded_message = ''.join(chr(i) for i in ascii_values)

print("Decoded Message:", decoded_message)

### Decoded Message: bronco{i<3planes}
```

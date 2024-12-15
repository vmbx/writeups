
# Deobfuscating the Python - Secret Serial Key Identification

### Description:
In this challenge, we identify a secret serial key by decrypting a locked file using a Python script. The script uses RSA and AES encryption methods. The objective is to unlock the flag and obtain the secret data.

### Steps:
1. **Decrypt the serial key** using RSA decryption.
2. **Unlock the product** by decrypting the locked file using AES in CBC mode.
3. **Extract the flag** from the decrypted file.

### Image 1: Code Snippet

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/locked%20unlocker/1.png)

```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long, long_to_bytes
from alive_progress import alive_bar

def key_decryptor(ciphertext):
    # Constants for RSA decryption
    d = 4603658780130581148915150220140209357434260720334171947464689689224115300059937591491927995062520871182721152309555936186188185035076128871154176204124793514488557135527608149566977491036337996020603266806593099534710926378143104232680282934708674028324260888928513479725201124908012923904062814280083965953750643748874417922582990140581447104359883546013632213300372709405906550337422870294600571797967308415692350001319846044256769035867042602480100026693980959744730774080841251147954497640746424227114619107029951275270629539250178389315031881132314376397792737912223417817283255802028819736850652480289527248653
    n = 14685324189506833621633107811016252161507381106280877435920825902296463588222347526580992212821242654402628189774220851293950600274703541388602153608650600757314994840159301791101046669751690593584924618968298465038031150257696014704169759196495613034523586560122072909260185257877656023066467007032069256593620750388889071255396806113069316347621756002927816606636249046941467604400177054039626140807225420227261522033732114158666152651006219442012006311015952815775894832796122883380450008664854141360533664966008511126694845625115250782538509459001723387038076625393501801355685209507943320132574334321194302347333
    c = bytes_to_long(ciphertext)
    m = pow(c, d, n)
    plaintext = long_to_bytes(m)
    return b'\x00' * (48 - len(plaintext)) + plaintext

def unlocker(flag):
    print('Starting decryption...')
    with alive_bar(256, title='Decrypting') as bar:
        for i in range(256):
            now_key = key_decryptor(flag[-256:])
            flag = flag[:-256]
            cipher = AES.new(key=now_key[:32], mode=AES.MODE_CBC, iv=now_key[32:])
            flag = cipher.decrypt(flag)
            flag = unpad(flag, 16)
            bar()
    print("Decryption complete! Saving output to 'flag.png'.")
    with open('flag.png', 'wb') as f:
        f.write(flag)

def main():
    serial_number = input('Enter the serial number to unlock this product: ')
    if serial_number == 'WA4Au-l10ub-18T7W-u9Yx2-Ms4Rl':
        print('Unlocking...')
        try:
            with open('flag.png.locked', 'rb') as f:
                locked_data = f.read()
            unlocker(locked_data)
        except FileNotFoundError:
            print("The file 'flag.png.locked' was not found!")
    else:
        print('Invalid serial number. Access denied.')

if __name__ == '__main__':
    main()
```

### Image 2: Code Execution

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/locked%20unlocker/2.png)

### Flag:

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/THJCC%20CTF%202024/Reverse/locked%20unlocker/Flag.png)

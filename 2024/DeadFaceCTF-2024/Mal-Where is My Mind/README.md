### Challenge 1: Mal-Where is My Mind 00

- **Description:** This challenge involved cracking a password hash that was infected. Using the **John the Ripper** tool, I was able to successfully retrieve the plaintext password and obtain the flag.
- **Tools Used:** John the Ripper
- **Flag Location:** The flag was saved in a text file (`flag00.txt`).

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2000/flag.png)

- **Flag:** `flag{How_can_I_describe_my_emotions_at_this_catastrophe}`

### Challenge 2: Mal-Where is My Mind 01

- **Description:** The second challenge required a thorough examination of the source code provided. After reviewing the code, I discovered a hidden vulnerability that led to the flag.
- **Tools Used:** Manual code review and static analysis tools
  
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2001/flag.png)

- **Flag:** `flag{Jack_Torrance_thought:_Officious_little_prick}`

### Challenge 3: Mal-Where is My Mind 02

- **Description:** In this challenge, the encoded string was base64 encoded with characters shifted around. I had to identify the pattern of shifting and correctly decode the base64 string to retrieve the flag.
  
![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2002/solution.png)

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2002/flag.png)

- **Flag:** `flag{I_dont_want_to_stay_here}`

### Challenge 4: Mal-Where is My Mind 03

- **Description:** The fourth challenge required decoding an ASCII encoded message. By converting the ASCII values back to their corresponding characters, I was able to uncover the flag.

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2003/binary.png)

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2003/flag.txt.png)

- **Flag:** `flag{I_do_not_propose_to_add_anything_to_what_has_already_been_written}`

### Challenge 5: Mal-Where is My Mind 04

- **Description:** This challenge involved multiple decoding steps. I first converted a hex string to its ASCII representation, then applied the ROT47 cipher, and finally decoded the result from base64 to obtain the flag.
- **Tools Used:** Hex conversion, ROT47, and base64 decoding

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2004/order.png)

![image](https://github.com/x03ee/DeadFaceCTF-2024/blob/main/Mal-Where%20is%20My%20Mind/Mal-Where%20is%20My%20Mind%2004/flag.txt.png)

- **Flag:** `flag{Ph'nglui_mglw'nafn_Cthulhu_R'lyeh_wgah'nagl_fhtagn}`

# Challenge: Won't Somebody Think of the Children

## Description

**Difficulty Level:** Medium

If Loab is back, we might need the council to help us out. The problem is that Anna sent Maya looking for them, but she still hasn't come back. This is her last known location... Maybe you can help find her.

I'd go, but I really don't want to be around those spooky ghost orphans.

## Challenge Overview

This challenge involves uncovering a hidden image within the provided data. By decoding a Base64-encoded string, you will reveal the images that lead you to the solution.

### Steps to Solve

1. **Base64 Decoding:** The first step is to decode the Base64 string provided in the challenge.
2. **Save the Images:** After decoding, save each output as an image file (e.g., `img1.png`, `img2.png`, ..., `img8.png`).
3. **Identify the Correct Image:** Examine the saved images and identify which one, named `img5`, is the correct one related to the challenge.

### Photos

Below are the images you will be working with:

![Image 1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/p1.PNG)
![Image 1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/p2.PNG)
![Image 1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/p3.PNG)
![Image 1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/p4.PNG)
![Image 1](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/p5.PNG)
![Image 7](https://github.com/x03ee/CTF-Writeup/blob/main/2024/SpookyCTF-2024/Forensic/wont-somebody-think-of-the-children/final.PNG)

- Pay attention to the metadata of the decoded image files; it may give clues about the correct image.
- Consider using tools like the `base64` command-line utility or online Base64 decoders to simplify the process.

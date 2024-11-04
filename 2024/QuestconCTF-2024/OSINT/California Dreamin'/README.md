# California Dreamin' CTF Challenge

## Overview
Welcome to the **California Dreamin'** Capture The Flag (CTF) challenge! In this challenge, participants will analyze a given image, perform geographical calculations, and find a hidden flag.

## Challenge Description
The challenge begins with a provided image, which holds clues to locate a specific place in California. Your task is to determine the distance to a notable landmark and uncover the flag hidden within the challenge.

![image](https://github.com/x03ee/QuestconCTF-2024/blob/main/OSINT/California%20Dreamin'/p1.png)

### Objective
1. Analyze the provided image to identify geographical markers.
2. Calculate the distance to the nearest state.
3. Use this distance to find the **Edwards Air Force Base**.
4. The flag can be retrieved by brute-forcing the meters away from this location.

![image1](https://github.com/x03ee/QuestconCTF-2024/blob/main/OSINT/California%20Dreamin'/p2.png)

## Steps to Solve
1. **Image Analysis**: Carefully examine the image for any visual clues that indicate location.
2. **Distance Calculation**: Use the identified location to calculate how far it is from the nearest state line.
3. **Geolocation**: Once you have the distance, navigate to the **Edwards Air Force Base**. 
4. **Brute Force**: Based on the distance, attempt to brute-force the flag using the following format.


```
QUESTCON{edwards-23}
```

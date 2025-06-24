## Reverse – *Game: Nitro Nexus*

### Challenge Overview

> *"I couldn’t afford the new Mario Kart game, so my friend gave me a copy of Nitro Nexus — a very buggy alternative. I’m usually great at racing games, but there’s just one problem… I can’t get past the first level."*

Challenge builds are available [here](https://drive.google.com/drive/folders/1L39C3J49w4awgTqAO-UCdICT79UQ_9WK).

---

### Technical Background

The method computes a level 2 collation weight for a Unicode character by handling special extender cases, using custom tables for CJK characters, falling back to default values if needed, and optionally remapping the result for cultural accuracy like a “game over” level screen where all character comparison rules are finalized and locked in for precise sorting.


---

Upon launching Nitro Nexus, the first screen presented is the default start screen (Level 1), which includes options such as **Play** and **Controls**.

![Main Menu](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/main.png)

We experimented by **deleting the original `Level 1` files** and **renaming `Level 2` files to `Level 1`**, then re-launching the game. This resulted in the game immediately loading what used to be Level 2 and showing a **“You Lose”** screen.

![Game Over](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/lose.png)

---

### Dynamic Level Loading

This behavior indicates that the game dynamically loads content based on file names, particularly looking for a level named `level1`. By renaming different levels to `level1`, we can manipulate the game into loading them at startup. This insight can be leveraged for debugging, testing different states, or skipping levels.

---

### Extracting the Flag

Following this logic:

1. **Original setup**:

   * `level1` → Main menu
   * `level2` → Game over screen
   * `level3` → Flag

2. We renamed `level2` to `level1` → Game loads "You Lose" screen.

3. Then we renamed `level3` to `level1` and launched the game again.

This time, instead of a losing screen, the game revealed the **flag**, confirming that `level3` is the final level.

![Flag Captured](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/flag.png)

The Nitro Nexus game engine loads the file named `level1` as the starting point, regardless of its original identity. By iteratively renaming levels and observing outcomes, we successfully identified the final level containing the flag. This approach showcases a simple yet effective exploitation of a game’s dynamic content loading mechanism.


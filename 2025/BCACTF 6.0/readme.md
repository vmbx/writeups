### Reverse - Game Nitro Nexus

```css
Challenge Description:
I couldn't afford the new Mario Kart game, so my friend gave me a copy of Nitro Nexus (a VERY buggy game). I'm a GOD at racing games, but theres only one problem... I can't get past the first level. The builds can be found here
```

The method computes a `level 2` collation weight for a Unicode character by handling special extender cases, using custom tables for CJK characters, falling back to default values if needed, and optionally remapping the result for cultural accuracy like a `“game over”` level screen where all character comparison rules are finalized and locked in for precise sorting.

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/dn.png)

When launching the game, `Level 1` acts as the main homepage, presenting the player with essential options such as 'Play' to start the game and 'Controls' to view how to play. This screen sets the starting point before any gameplay begins.

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/main.png)

After deleting the original `Level 1` files and renaming the Level 2 files to Level 1, the game produces the following output.
This behavior suggests that the game dynamically loads content based on file naming conventions. By `renaming Level 2 to Level 1`, we essentially trick the system into treating Level 2 as the starting level. This can be useful for debugging, modding, or skipping ahead in gameplay.

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/lose.png)



After observing the game's behavior, we discovered that when we rename a level to `level1` and press the **Play** button, the game automatically loads the level named `level1` as the starting point. In the previous step, we had renamed what was originally `level2` to `level1`, and upon launching it, we were shown a "You Lose" screen. This confirms that `level2` is a game over or fail state level. 

Given this pattern, we can conclude that the actual flag must be located in the final level, which is `level3`. To trigger this, we need to delete the currently renamed `level1` which is the old `level2` and then rename `level3` to `level1`. When we press the **Play** button after this change, the game launches what was originally `level3` as the first level, and this time it reveals the **flag** instead of a losing screen. 

This means the game engine always loads `level1` as the entry point, and the renaming trick allows us to choose which actual level it loads by sequentially testing renamed levels, we can identify which contains the flag. 

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/BCACTF%206.0/images/flag.png)


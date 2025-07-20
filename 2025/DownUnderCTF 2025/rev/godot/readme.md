# Godot Challenge
```
Vladimir and Estragon converse on various topics while they wait for a man named Godot. While they wait, Pozzo is on his way to the market to sell his slave, Lucky.
```

### Files provided

- `ductf_2025_godot_encrypted.exe`  
- `ductf_2025_godot_encrypted.pck`

---

### Initial research

After looking into Godot, I found a way to extract the encrypted key from the program’s bytes. This video helped a lot:  
https://www.youtube.com/watch?v=fWjuFmYGoSY



Firstly lookup in strings "Condition \"fae.is_null()\" is true. Returning: false", and select length 52. After wait until anylsis is fully complete. 

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/gh.png)

Open the function with decompile and look for `uVar1 = (&DAT_143f78540)[lVar9];`, the encryption key is inside "DAT_143f78540". After we can copy the hex bytes.
`52d066de1115fc479e53fcf821715ad7db73e12df7e557833712136b4ff7529e`. 

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/gh1.png)

Following the steps, the encrypted key showed up as hex bytes. Using the tool [gdsdecomp](https://github.com/GDRETools/gdsdecomp), I input the encrypted key along with the executable to decompile the game scripts.  

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/go1.png)

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/go2.png)

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/go3.png)

After that, I installed Godot Engine and imported the game files to explore the project.

### Shops Showcase:
![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/shop.png)


---

### Game analysis

Inside the game files, there’s a shop with a timer for unlocking. Here’s a snippet from the script:

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/shop1.png)

Solution:

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/shop3.png)

```gdscript
extends Area2D

@onready var godotSprite = $AnimatedSprite2D

var godot = false

func _ready() -> void:
	godot = true
	godotSprite.show()

func _process(delta: float) -> void:
	# no need for any time check now
	pass

func _on_body_entered(body: Node2D) -> void:
	body.shop = true
	body.godot = godot

func _on_body_exited(body: Node2D) -> void:
	body.shop = false
````

---

### How to get the flag

![step](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/images/file1.png)

While playing, I went to the shop and found that pressing the `E` key twice quickly teleports you straight to the flag location.

![flag](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/goflag.png)

---

### Summary

* Extracted the encrypted key by analyzing the binary
* Used `gdsdecomp` to decompile Godot scripts
* Imported the project in Godot Engine for deeper inspection
* Found a shop with a timer lock in the code
* Double pressing `E` teleports to the flag and completes the challenge


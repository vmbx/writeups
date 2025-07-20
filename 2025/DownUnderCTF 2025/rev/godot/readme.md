# DUCTF 2025 — Godot Reverse Challenge Writeup
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

Following the steps, the encrypted key showed up as hex bytes. Using the tool [gdsdecomp](https://github.com/GDRETools/gdsdecomp), I input the encrypted key along with the executable to decompile the game scripts.  

After that, I installed Godot Engine and imported the game files to explore the project.

---

### Game analysis

Inside the game files, there’s a shop with a timer for unlocking. Here’s a snippet from the script:

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

While playing, I went to the shop and found that pressing the `E` key twice quickly teleports you straight to the flag location.

![flag](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/flag_go.png)

---

### Summary

* Extracted the encrypted key by analyzing the binary
* Used `gdsdecomp` to decompile Godot scripts
* Imported the project in Godot Engine for deeper inspection
* Found a shop with a timer lock in the code
* Double pressing `E` teleports to the flag and completes the challenge


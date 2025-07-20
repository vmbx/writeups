### godot - reverse
```
Vladimir and Estragon converse on various topics while they wait for a man named Godot. While they wait, Pozzo is on his way to the market to sell his slave, Lucky.
```

Absolutely! Here’s your enhanced write-up formatted nicely for a `README.md` file on GitHub, using Markdown syntax:



We are given two files:  
- `ductf_2025_godot_encrypted.exe`  
- `ductf_2025_godot_encrypted.pck`

---

## Overview

After some research into Godot's engine internals, I discovered a method to extract the encrypted key embedded in the program’s bytecode. A helpful guide can be found here:  
[YouTube Tutorial](https://www.youtube.com/watch?v=fWjuFmYGoSY)

By following the steps, the encrypted key is revealed as a series of hexadecimal bytes. Using the tool [gdsdecomp](https://github.com/GDRETools/gdsdecomp), we can input the encrypted key along with the executable to decompile the game scripts.  

Next, by installing Godot Engine, we can import the extracted game files and analyze the project directly.

---

## Analyzing the Game Files

Upon inspecting the imported Godot project, we discovered a shop mechanic that appears to have a timer-based unlock system. Below is the relevant GDScript code snippet:

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

## Exploit and Capture the Flag

By playing the game and entering the shop area, we noticed that double-pressing the `E` key teleports the player directly to the flag’s location.

![flag location](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/flag_go.png)

---

## Summary

* Extracted encrypted key via bytecode inspection
* Used `gdsdecomp` to decompile Godot scripts
* Imported game project into Godot Engine
* Analyzed shop system and bypassed timer by double-pressing a key
* Teleported to flag location and captured the flag

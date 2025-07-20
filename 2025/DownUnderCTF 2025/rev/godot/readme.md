### godot - reverse
```
Vladimir and Estragon converse on various topics while they wait for a man named Godot. While they wait, Pozzo is on his way to the market to sell his slave, Lucky.
```

We are giving two files, `ductf_2025_godot_encrypted.exe` and `ductf_2025_godot_encrypted.pck`.

After some researching about godot, i found a method to get encrypted key through bytes in the program.
https://www.youtube.com/watch?v=fWjuFmYGoSY

After Following through it showes ecrypted key in hex bytes. Using https://github.com/GDRETools/gdsdecomp we can input the encrypted key and attach the exe and decompile. After we can install godot and import the game file.

Going through the game file, we found out there is shop which has a timer until unlock.
```py
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

```

After we play the game and head to the shop and double pressing e, we teleport to the flag location.

![flag](https://github.com/vmbx/writeups/blob/main/2025/DownUnderCTF%202025/rev/godot/flag_go.png)

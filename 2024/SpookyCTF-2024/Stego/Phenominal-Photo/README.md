# Phenomenal-Photo

Use **Steghide** to extract hidden data from the image file.

![image](https://github.com/x03ee/SpookyCTF-2024/blob/main/Stego/Phenominal-Photo/boo.jpg)

---

### Ship#1 Folder: `Map.txt`

```
⋔⏃⌿: ⌰⟒⎎⏁, ⎍⌿, ⎅⍜⍙⋏, ⌰⟒⎎⏁, ⎅⍜⍙⋏, ⍀⟟☌⊑⏁, ⍀⟟☌⊑⏁, ⎅⍜⍙⋏, ⌰⟒⎎⏁, ⎍⌿, ⌰⟒⎎⏁, ⍀⟟☌⊑⏁, ⎍⌿

⍀⟒⋔⟟⋏⎅⟒⍀ ⏁⊑⏃⏁ ⍜⎍⍀ ☌⌿⌇ ⟟⌇ ⏃ ⌰⟟⏁⏁⌰⟒ ⎎⎍⋏☍⊬, ⟟⏁ ⍜⋏⌰⊬ ⏁⏃☍⟒⌇ ⏁⊑⟒ ⎎⟟⍀⌇⏁ ⌰⟒⏁⏁⟒⍀ ⍜⎎ ⟒⏃☊⊑ ⎅⟟⍀⟒☊⏁⟟⍜⋏ ⍙⟒ ⍙⏃⋏⏁ ⏁⍜ ☌⍜ (⌇⏁⎍⌿⟟⎅ ⋔⟒⋔⍜⍀⊬ ⋔⏃⋏⏃☌⟒⋔⟒⋏⏁)
```

#### Translation (via Alien Language Decoder):

```
MAP: LEFT, UP, DOWN, LEFT, DOWN, RIGHT, RIGHT, DOWN, LEFT, UP, LEFT, RIGHT, UP

REMINDER: OUR GPS IS A LITTLE FUNKY. IT ONLY TAKES THE FIRST LETTER OF EACH DIRECTION (STUPID MEMORY MANAGEMENT)
```

---

### Password for `gps.zip`

```
LUDLDRRDLULRU
```

Explanation: This password corresponds to the first letters of `LEFT, UP, DOWN, LEFT, DOWN, RIGHT, RIGHT, DOWN, LEFT, UP, LEFT, RIGHT, UP`.

---

### Contents of `gps.zip`

```
⋏⟟☊☊{⊑⟒⌰⌿_⋔⟒_⎎⟟⋏⎅_⏁⊑⟒_⌿⌰⏃⋏⟒⏁_⏚0⍜}
```

#### Translation (via Alien Language Decoder):

```
NICC{HELP_ME_FIND_THE_PLANET_B0O}
```

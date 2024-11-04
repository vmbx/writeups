# Web Challenge - No Paste

![Challenge](https://github.com/x03ee/H7CTF-Writeups/blob/main/web/No%20Paste/challenge.png)

### Challenge Overview:
In this challenge, the objective was to find a way to bypass a restriction on the web page that prevented users from pasting inputs. This restriction hinted at the need to examine the website’s source code for potential vulnerabilities or clues.

### Approach:
I started by inspecting the web page's elements and reviewing the JavaScript and CSS files to uncover any hidden logic. During this investigation, I discovered a JavaScript file named `scripts.js`. Upon closer inspection, I found a suspicious code snippet that validated input by checking whether it matched a hardcoded string, `bypass123`.

Here’s the relevant code fragment:
```js
if (input === 'bypass123') {
    console.log("Success!");
} else {
    console.log("Wrong input.");
}
```
This hardcoded value, `bypass123`, seemed to be the key to bypassing the input validation.

### Solution Execution:
After finding the suspicious string, I returned to the web form and manually entered `bypass123` into the input field. Upon submitting the form, the page responded successfully and revealed the hidden flag.

![Solution](https://github.com/x03ee/H7CTF-Writeups/blob/main/web/No%20Paste/solution.png)  
![Solution1](https://github.com/x03ee/H7CTF-Writeups/blob/main/web/No%20Paste/solution1.png)

### Final Flag:
```
H7CTF{h@ck_th3_sy$t3m}
```

![Flag](https://github.com/x03ee/H7CTF-Writeups/blob/main/web/No%20Paste/flag.png)

Copying the bot id then importing in this form:
`https://discord.com/oauth2/authorize?client_id=1301271615426007175&permissions=8&scope=bot`

Invite to your server then type the command: `!read_report` it says "You don't have permissions to run this command! If you are a triager, please contact IT to be assigned the **triage** role."

Role create triage then import to yourself. Typing `!read_report 1` we get a news letter id when try and error from 0 - 21, we find out first one showed us the flag.

```
Report 0 - INTIGRITI{4n07h3r_y34r_4n07h3r_7r1463_b07}
The product protects a primary channel, but it does not use the same level of protection for an alternate channel.
CWE
CWE-420: Unprotected Alternate Channel
CVSS Score
1337 (🚩)
```

Final Flag: `INTIGRITI{4n07h3r_y34r_4n07h3r_7r1463_b07}`

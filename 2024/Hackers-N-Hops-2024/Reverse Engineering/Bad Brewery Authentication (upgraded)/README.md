```js
function _0x5c49() {
  const _0x12410f = [
    "8060850mSYZgV",
    "node:readline",
    "6011032Zeqqob",
    "8RRNxFz",
    "8gtpnLG",
    "778898FTyrdX",
    "question",
    "stdout",
    "log",
    "Welcome,\x20Gargoyle!\x20Enjoy\x20your\x20free\x20beverage.\x20Thank\x20you\x20for\x20visiting\x20the\x20Haunted\x20Brewery!",
    "70260FPLLjQ",
    "120DeJGNm",
    "3608bdGxII",
    "Welcome\x20to\x20the\x20Haunted\x20Brewery.\x20We\x20have\x20updated\x20our\x20platform\x20to\x20be\x20more\x20secure\x20using\x20cutting-edge\x20technology.",
    "1142385LgiMtp",
    "9236955OAgtgP",
    "299605HqIJVe",
  ];
  _0x5c49 = function () {
    return _0x12410f;
  };
  return _0x5c49();
}
const _0x5d37f5 = _0x4d71;
(function (_0x292654, _0x20c546) {
  const _0x1b1b3f = _0x4d71,
    _0x2db0d1 = _0x292654();
  while (!![]) {
    try {
      const _0x2f7a7e =
        parseInt(_0x1b1b3f(0xfa)) / 0x1 +
        (parseInt(_0x1b1b3f(0xf9)) / 0x2) *
          (-parseInt(_0x1b1b3f(0x103)) / 0x3) +
        -parseInt(_0x1b1b3f(0xf7)) / 0x4 +
        (-parseInt(_0x1b1b3f(0x105)) / 0x5) *
          (-parseInt(_0x1b1b3f(0x100)) / 0x6) +
        -parseInt(_0x1b1b3f(0x104)) / 0x7 +
        (parseInt(_0x1b1b3f(0xf8)) / 0x8) * (parseInt(_0x1b1b3f(0xf5)) / 0x9) +
        (-parseInt(_0x1b1b3f(0xff)) / 0xa) *
          (-parseInt(_0x1b1b3f(0x101)) / 0xb);
      if (_0x2f7a7e === _0x20c546) break;
      else _0x2db0d1["push"](_0x2db0d1["shift"]());
    } catch (_0x507e15) {
      _0x2db0d1["push"](_0x2db0d1["shift"]());
    }
  }
})(_0x5c49, 0xcb1f9);
const readline = require(_0x5d37f5(0xf6));
function _0x4d71(_0x52c5b3, _0x147659) {
  const _0x5c49b9 = _0x5c49();
  return (
    (_0x4d71 = function (_0x4d7114, _0x4149ea) {
      _0x4d7114 = _0x4d7114 - 0xf5;
      let _0xd0315e = _0x5c49b9[_0x4d7114];
      return _0xd0315e;
    }),
    _0x4d71(_0x52c5b3, _0x147659)
  );
}
var hTierMem = Buffer["from"](
  "SG5Ie09iZnVzY2F0aW9uSXNBbHNvTm90RW5jcnlwdGlvbn0=",
  "base64"
);
const rl = readline["createInterface"]({
  input: process["stdin"],
  output: process[_0x5d37f5(0xfc)],
});
function awardBeer(_0x5065c1) {
  const _0x44f13e = _0x5d37f5;
  _0x5065c1 == hTierMem["toString"]()
    ? console[_0x44f13e(0xfd)](_0x44f13e(0xfe))
    : console["log"](
        "Welcome!\x20Please\x20enjoy\x20your\x20stay\x20at\x20the\x20Haunted\x20Brewery."
      );
}
console[_0x5d37f5(0xfd)](_0x5d37f5(0x102)),
  rl[_0x5d37f5(0xfb)](
    "Please,\x20scan\x20your\x20membership\x20card\x20to\x20gain\x20access\x20to\x20our\x20facilities.\x20Patrons\x20of\x20Gargoyle\x20tier\x20or\x20higher\x20will\x20receive\x20free\x20beverage\x20today.\x0a",
    (_0x3a588c) => {
      const _0x4adbf1 = _0x5d37f5;
      console[_0x4adbf1(0xfd)](awardBeer(_0x3a588c)), rl["close"]();
    }
  );

```

Deobfuscated: 

```js
const readline = require('node:readline')
var hTierMem = Buffer.from(
  'SG5Ie09iZnVzY2F0aW9uSXNBbHNvTm90RW5jcnlwdGlvbn0=',
  'base64'
)
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
})
function awardBeer(_0x5065c1) {
  _0x5065c1 == hTierMem.toString()
    ? console.log(
        'Welcome, Gargoyle! Enjoy your free beverage. Thank you for visiting the Haunted Brewery!'
      )
    : console.log('Welcome! Please enjoy your stay at the Haunted Brewery.')
}
console.log(
  'Welcome to the Haunted Brewery. We have updated our platform to be more secure using cutting-edge technology.'
)
rl.question(
  'Please, scan your membership card to gain access to our facilities. Patrons of Gargoyle tier or higher will receive free beverage today.\n',
  (_0x3a588c) => {
    console.log(awardBeer(_0x3a588c))
    rl.close()
  }
)
```

Decode Base64 `SG5Ie09iZnVzY2F0aW9uSXNBbHNvTm90RW5jcnlwdGlvbn0=`.

Flag: `HnH{ObfuscationIsAlsoNotEncryption}`

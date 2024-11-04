```js
const readline = require('node:readline');
var hTierMem = Buffer.from('SG5Ie0Jhc2U2NEVuY29kaW5nSXNudFNhZmVGMHJBdXRoZW50aWNhdGlvbn0=', 'base64'); 
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
function awardBeer(badge) {
    if (badge == hTierMem.toString() ) {
        console.log("Welcome, Gargoyle! Enjoy your free beverage. Thank you for visiting the Haunted Brewery!")
    } else {
        console.log("Welcome! Please enjoy your stay at the Haunted Brewery.")
    }
};
console.log('Welcome to the Haunted Brewery.');
rl.question(`Please, scan your membership card to gain access to our facilities. Patrons of Gargoyle tier or higher will receive free beverage today.\n`, badge => {
    console.log(awardBeer(badge)); 
    rl.close();
  });
  ```

Decode Base64 `SG5Ie0Jhc2U2NEVuY29kaW5nSXNudFNhZmVGMHJBdXRoZW50aWNhdGlvbn0=`

Flag: `HnH{Base64EncodingIsntSafeF0rAuthentication}`

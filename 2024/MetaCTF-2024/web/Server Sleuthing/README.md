# Web - Server Sleuthing Writeup

## Solution

This challenge involves using Burp Suite to uncover hidden server functionalities by manipulating HTTP requests.

## Step-by-Step Solution

1. **Setup Burp Suite:**
   - Install Burp Suite from the [official site](https://portswigger.net/burp).
   - Configure your browser to use Burp Suite as a proxy (default: `127.0.0.1:8080`).

2. **Capture Requests:**
   - With Burp Suite’s Intercept feature enabled, navigate the target web application in your browser.
   - Capture a GET request of interest and review it in Burp Suite.

3. **Modify Request Method:**
   - Send the GET request to the "Repeater" tab.
   - Change the request method to POST and modify the body if needed.
   - Send the POST request and analyze the response.

4. **Analyze and Document:**
   - Compare responses from GET and POST requests.
   - Document any new functionalities or server responses.

![Burp](https://github.com/x03ee/MetaCTF-WriteUps/blob/main/web/Server%20Sleuthing/images/Burp.PNG)

### Final Flag:
```
MetaCTF{i_am_running_python_flask}
```

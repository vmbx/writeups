1. **Connect to the Challenge**: Navigate to the URL: [https://hackersnhops-fcaptcha.chals.io](https://hackersnhops-fcaptcha.chals.io).

2. **Human Verification**: You will be prompted to verify if you are human. 

3. **Intercept Requests with Burp Suite**: 
   - Open Burp Suite and configure it to intercept the requests between your browser and the target website.
   - When you encounter a request that includes `authenticated=false`, change the value to `authenticated=true` to bypass the verification step.

![image](https://github.com/x03ee/Hackers-N-Hops-2024/blob/main/WEB/Anti-Spirit%20FCaptcha/s1.png)

4. **Process the Response**:
   - After changing the authentication status, submit the request.
   - You should receive a response containing a Base64-encoded image.

![image](https://github.com/x03ee/Hackers-N-Hops-2024/blob/main/WEB/Anti-Spirit%20FCaptcha/s2.png)

5. **Decode the Image**:
   - Copy the Base64 string from the response.
   - Use a Base64 decoder to decode the image.
   - Save the decoded image to your local machine.

![image](https://github.com/x03ee/Hackers-N-Hops-2024/blob/main/WEB/Anti-Spirit%20FCaptcha/s3.png)

6. **Retrieve the Flag**: 
   - Upon successfully saving the image, check its contents for the flag.

![image](https://github.com/x03ee/Hackers-N-Hops-2024/blob/main/WEB/Anti-Spirit%20FCaptcha/flag.png)

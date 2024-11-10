![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/s11.PNG)

1. **Go to the URL**:  
   Visit [https://cookie.cruxipher.crux-bphc.com](https://cookie.cruxipher.crux-bphc.com).

2. **Inspect the Source Code**:  
   View the page source, and you'll find the following comment:
   ```html
   <!-- test test@123 -->
   ```
   
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/s1.PNG)

3. **Initial Credentials**:
   - **Username**: test
   - **Password**: test@123

4. **JWT Cookie**:  
   The initial JWT cookie is:
   ```text
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.2bZHkT6VgGqelPzmQGEU8nLetZsvhkVV42bP2ybhi-Q
   ```
   ![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/s2.PNG)

5. **Modify the Username**:  
   Change the username in the JWT cookie from `test` to `admin`.

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/s3.PNG)

6. **Updated JWT Cookie**:  
   After modifying the cookie, the new JWT becomes:
   ```text
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.xLtLdUxXsGB7EqP49a8xQziqpjkVKeJ9o2nix4xLf5M
   ```

   ![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/s4.PNG)

7. **Access the Admin Page**:  
   With the updated JWT cookie, go to [https://cookie.cruxipher.crux-bphc.com/admin](https://cookie.cruxipher.crux-bphc.com/admin).

![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/cruXipher-2024/Web/Cookie/5.PNG)

8. **Retrieve the Flag**:  
   On the admin page, you’ll find the flag:
   ```text
   cruXipher{n0_p0int_l34v1ng_th3_k3y_1n_th3_l0ck}
   ```

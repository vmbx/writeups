### Git-Git

```
You have been hired as a security researcher for a company, tasked with investigating the security of the company GitHub repository.

According to insider information, there may be sensitive information or confidential content hidden within this public GitHub repository that should not be visible to external parties.

Can you leverage your technical skills to successfully recover these important clues?

Hint: try smartest, :DD
```

Repository: [https://github.com/UmmItC/gitgit](https://github.com/UmmItC/gitgit)

Navigating to the repository’s [activity page](https://github.com/UmmItC/gitgit/activity), we notice 6 changes. We can review these manually to identify anything suspicious.

By examining the following commit comparison:
[Compare Commits](https://github.com/UmmItC/gitgit/compare/d0fe54d3fccf7345555da3e791f5415e8875ac01...5dd233465d64bebed5b8755e5e081fe0653e0b9b),

![image](https://github.com/vmbx/CTF-Writeup/blob/main/2025/No%20Hack%20No%20CTF%202025/no-flag/p1.png)

we uncover the flag:

**`NHNC{Don7_tH!NK_foRCe_PU$H3d_CAn_HElp_YoU_hiD3_mE$s@6e!!!!-_0}`**


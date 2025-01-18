-- https://leetcode.com/problems/find-users-with-valid-e-mails
SELECT * FROM Users
WHERE mail ~ '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$'
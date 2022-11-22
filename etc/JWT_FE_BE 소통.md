# JWT 프론트 <-> 백엔드

### 1. 로그인

#### 1) 기본 로그인

- phone, password를 request body에 넣고 POST 요청을 보내면 token return

**ex**

- request

  ```
  {
    "phone": "01000000000",
    "password": "Password!@"
  }
  ```

- response

  ```
  HTTP Status: 201
  {
    "user": {
      "id": 1,
      "phone": "01000000000",
      "kakao_id": null
    },
    "token": {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MTQ0NTQzLCJpYXQiOjE2NjcxNDQ1NDAsImp0aSI6ImY3MjVkNDBkZDg5OTRmZDM4MGRhMTU1ZTJkZGQwMTcxIiwidXNlcl9pZCI6MX0.O_OcrOirF9he6jBPWsSJzqrbOwz72X7QEogQ9rVOdts",
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzE0NDk2MCwiaWF0IjoxNjY3MTQ0NTQwLCJqdGkiOiJkMjg3NDI5YjZmZmI0NmExOTg5N2U0ZjBiNmE3NjEwZiIsInVzZXJfaWQiOjF9.4ZK37ia7WSM4tN2_Lfy9lL9uLSo2vTt5iUHIBDfSVIA"
    }
  }
  ```

  

### 2. access token이 만료되었을 때, 인증이 필요한 url 접근 시

#### Backend의 응답 

```
HTTP Status: 401
{
  "detail": "이 토큰은 모든 타입의 토큰에 대해 유효하지 않습니다",
  "code": "token_not_valid",
  "messages": [
    {
      "token_class": "AccessToken",
      "token_type": "access",
      "message": "유효하지 않거나 만료된 토큰"
    }
  ]
}
```

#### 프론트에서 할 일 

- 401 에러일 경우 code가 있는지 확인 
- code가 있다면, token_not_valid인지 확인
- token_not_valid라면 `/accounts/token_refresh/`로 refresh_token을 담아 POST요청

```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzE0NDk2MCwiaWF0IjoxNjY3MTQ0NTQwLCJqdGkiOiJkMjg3NDI5YjZmZmI0NmExOTg5N2U0ZjBiNmE3NjEwZiIsInVzZXJfaWQiOjF9.4ZK37ia7WSM4tN2_Lfy9lL9uLSo2vTt5iUHIBDfSVIA"
}
```

#### 백엔드에 응답 

```
HTTP Status: 200
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3MTQ0NTY4LCJpYXQiOjE2NjcxNDQ1NDAsImp0aSI6IjQ2ZjM5ZjkyMWU3MTRhMmZiMmU1ZTM2MTI5ZjFmMzdkIiwidXNlcl9pZCI6MX0.D8VK53fqHLDWyN9SCyZtVHpfM8zxVRh43nd6tfRuBgo",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzE0NDk4NSwiaWF0IjoxNjY3MTQ0NTY1LCJqdGkiOiIxMDNjOTQ2NmMyNWI0MjI2YTQ0YTQyNzQ2ODM2ZGZjOSIsInVzZXJfaWQiOjF9.ee49gFY1iuYz3Vu7Bp5y7c3ZGts8S_Gn_GFnF3Qp5ck"
}
```

- 다시 프론트에서 담기 

### 3. refresh token도 만료되었을 때, 

#### 프론트가 만료된 refresh_token을 `/accounts/token_refresh/` 로 보낼 때 백엔드의 응답

```
HTTP Status: 401
{
  "detail": "유효하지 않거나 만료된 토큰",
  "code": "token_not_valid"
}
```

#### 클라이언트 역할

- local/session storage에 모든 JWT 관련 토큰을 제거하고 유저를 로그인 페이지로 redirect

**JWT 포함 시 login 등 다른 인허가 필요없는 URL에서도 401 에러 발생 **

### 정리

- User가 401이 뜨는 다양한 경우가 있으니, 클라이언트에서는 401응답 시, code가 있는지 확인해야함 
- code가 token_not_valid면 먼저 refresh_token을 `/acconts/token_refresh`로 보냄 
- `/accounts/token_refresh`에서도 401 응답이 오면 유저를 강제 로그아웃
  - 토큰을 날리고 로그인 페이지로 이동시킴 

### 3-1 

#### 토큰이 만료되었을 때, FE 에서 JWT 디코딩을 진행하고, 시간을 확인 후 바로 로그아웃 시킬수도 있음 ! 

https://www.npmjs.com/package/jwt-decode
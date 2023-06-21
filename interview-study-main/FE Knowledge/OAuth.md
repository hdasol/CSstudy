# OAuth

## 동현

### OAuth란 무엇인가요?

풀어 설명하면, 현재 서비스에서 다른 서비스에 보관된 회원 리소스에 접근할 수 있도록 권한을 넘겨주는 인증 방법입니다.

여기서, 우리가 접근하려는 회원 리소스를 가지고 있는 서비스를 Resource Server (보통 Google, Naver 같은 사이트)라고 부릅니다. 해당 서비스에 계정을 소유하고 있는 사용자를 Resource Owner라고 부르며, 이러한 정보를 필요로하는 사이트를 Client라고 정의합니다.
또한, 인증 정보를 관리하는 서버를 Authorization Server (Google, Naver...)라고 부릅니다. (Resource Server, Authorization Server)

### 동작 방식

Resource Owner는 해당 Client에서 자신의 정보를 사용할 수 있음을 알리도록 Resource Server로 client id와 자신의 회원 정보를 넘겨 authorization token을 client의 redirect url의 쿼리스트링으로 응답받습니다.  
(실제로는 client id, redirect url, scope 등을 넘기고, 서버에서 client id가 존재하는지, 존재한다면 redirect url도 일치하는지 등을 검증)

redirect된 주소에서는 다시 한 번 올바른 클라이언트인지 검증하기 위해 client id와 secret key, 발급된 authroization key를 서버로 넘겨 검증을 받습니다. 매칭되는 쌍이 존재한다면 Resource Server는 Access token을 발급합니다. 클라이언트는 해당 토큰을 저장 후, 데이터 요청이 필요할 때 마다 Access token을 함께 보냅니다.

### 참고 자료

- [OAuth 2.0이란?](https://doqtqu.tistory.com/295)
- [OAuth 개념 및 동작 방식 이해하기](https://tecoble.techcourse.co.kr/post/2021-07-10-understanding-oauth/)
- [갓고잉 생활코딩](https://www.youtube.com/playlist?list=PLuHgQVnccGMA4guyznDlykFJh28_R08Q-)

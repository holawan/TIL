# VS code로 편리하게 EC2 환경 사용하기 

### 1. Remote -SSH 설치

![image-20221020140434225](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020140434225.png)

### 2. 원격 ssh 설정

- vscode에서 `F1`을 누르고, ssh 검색 후 `원격-SSH: 새 SSH 호스트 추가` 클릭 

![image-20221020140750942](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020140750942.png)

- 연결할 username@ip 입력 

    ![image-20221020141049764](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141049764.png)

- SSH 구성 파일 선택 

    ![image-20221020141115785](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141115785.png)

- local에서 위 경로 중 한 곳으로 이동해, `config` 파일 수정 

     ![image-20221020141300255](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141300255.png)

- 발급받은 `.pem` 키 해당 경로로 이동 후, 경로 맞춰주기 

    ```
    Host k7b103.p.ssafy.io
      HostName k7b209.p.ssafy.io
      User ubuntu
      ForwardAgent yes
      IdentityFile ~/.ssh/K7b103.pem
    ```

![image-20221020141345431](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141345431.png)

### 3. 연결해보기 

- extension의 원격 탐색기 클릭

    ![image-20221020141426372](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141426372.png)

- 추가된 IP 우클릭 후 **현재 창에서 호스트에 연결** 또는 **새창에서 호스트에 연결** 클릭

    ![image-20221020141630088](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141630088.png)

= 

- 폴더 열기 

    ![image-20221020141714304](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141714304.png)

- 원하는 폴더 선택

    ![image-20221020141730205](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141730205.png)

- 확인 버튼을 누르면 빌린 EC2의 Linux 환경을 VScode에서 GUI를 활용하며 사용 가능 

    ![image-20221020141859783](VS code로 편리하게 EC2 환경 사용하기.assets/image-20221020141859783.png)
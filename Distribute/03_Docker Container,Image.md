# Docker Container,Image

## Docker GUI : Portainer

### Image와 Container

- Image에서 container를 만들 수 있고, 이는 Class와 Instance 관계와 유사하다.

- 그렇다면 Image를 어디에서 가져오는가?

  - **Docker Hub**
  - 전세계의 Docker 이미지를 업로드하고 다운로드 받는 곳 
  - Docker hub안에 어떠한 이미지든지 올리고 인터넷만 연결되어있다면, 인터넷을 연결해서 환경을 구축하는데 도움을 주는 Hub이다.
  - 우리가 올리는 Image 뿐 아니라, 여러 Software의 Image가 올라와있다.

  ![dockerhub](03_Docker Container,Image.assets/dockerhub.PNG)

- 따라서 우리는 Docker hub에서 Image를 받아서 Container를 만드는데 사용할 수 있는 것이다! 

### portainer Image

- Docker를 GUI로 바꿔주는 Software 

#### GUI vs CLI

- GUI(Graphic User Interface)

  - 그래픽적으로 작업하는 환경

  - 마우스로 조작하면서 작업한다.
  - CLI로 작업하기 어려운 초심자들에게 좋다! 

- CLI(Command Line Interface)
  - gitbash, terminal, cmd

### Portainer 설치

1. Docker Hub 접속 (https://hub.docker.com/)

2. Portainer 검색

3. portainer-ce 사용(https://hub.docker.com/r/portainer/portainer-ce)

   - portainer/portainer가 가장 위에 나오는데, 이는 사용하지 않는 버젼이고, portainer-ce라는 커뮤니티 에디션을 사용한다. 

4. Deploy Portainer 선택(https://docs.portainer.io/v/ce-2.9/start/install)

5. Docs에 요구되는 내용 넣어주기

   ```cmd
   docker volume create portainer_data
   ```

   ```
   docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
   ```

   - 첫 설치라면 해당 문구가 발견됨

     ```
     Unable to find image 'portainer/portainer-ce:latest' locally
     latest: Pulling from portainer/portainer-ce
     ```

     - 가상 서버 내에 있는 Docker 시스템에서 image를 찾지 못했기 때문에, Docker hub에서 image를 가져옴 

6. 설치 확인 

   ```
   root@vultr:~# docker container ls
   CONTAINER ID   IMAGE                    COMMAND        CREATED              STATUS              PORTS                                                           NAMES
   c9be01d36478   portainer/portainer-ce   "/portainer"   About a minute ago   Up About a minute   8000/tcp, 9443/tcp, 0.0.0.0:9000->9000/tcp, :::9000->9000/tcp   portainer
   ```

   - run 한 번만 했는데, 모든 시스템이 구축됐다..? 

### Portainer 실행 

1. 빌린 IP에 port를 추가해서 접속 

   - URL 창에 [IP]:9000

   ![접속결과](03_Docker Container,Image.assets/접속결과.PNG)

2. Username과 Password 설정 후 CreateUser 설정

   - 만약 timeout이 나온다면 

     ```
     docker restart portainer
     ```

3. Docker 사용 선택

4. 가상서버 내 Docker 시스템에 어떤 일이 벌어지는지 GUI로 확인 가능 

   ![portainer dashboard](03_Docker Container,Image.assets/portainer dashboard.PNG)

5. Container 확인해보기

   ![portainer run](03_Docker Container,Image.assets/portainer run.PNG)

   Portainer Image가 실행되고 있는 것을 확인할 수 있음

   - 즉, 아까 실행시킨 컨테이너로 portainer를 구동시킨 것이다. 

## Nginx container / What is Port?

### Port

- 서버와 통신할 때 사용하는 것 
- 컴퓨터와 다른 외부의 것과 통신할 때 사용하는것
- 서버는 1번부터 N까지 포트가 있다.
- 우리는 서버에서 특정 포트를 지정하고 해당 포트에 요청을 보내서 응답을 받는다.
- ex
  - python manage.py runserver 127.0.0.1:8000 에서 8000을 의미 

![PORT](03_Docker Container,Image.assets/PORT.PNG)

#### Docker 안의 Port

우리는 VULTR라는 가상 서버를 대여해서 이 안에 Docker라는 시스템을 구축해놓은 상태이다. VULTR라는 곳에서 빌린 서버 자체도 PORT가 존재하는 컴퓨터이지만, 이 안에 있는 Container 하나도 시스템이라고 볼 수 있다.

- 따라서 이 안에도 Port가 존재한다.
- 실제로 Portainer와 Browser 간 접속을 위해서는 가상서버의 Port와 Portainer의 Port를 연결시켜줘야한다. 
- Portainer를 설치할 때 9000:9000을 설치한 것도 일치를 위함! 

##### 잘 알려진 Port 

- HTTP protocol Port **80**
  - 아무런 Port 번호를 붙이지 않고 요청을 보내면 항상 80번 port로 연결이된다. 

### NGINX

- Portainer를 설치했기 때문에, 보다 쉽게 Image를 불러올 수 있다.

#### NGINX 설치 과정

1. Portainer의 Containers로 접속

2. Create container

   ![createcontainer](03_Docker Container,Image.assets/createcontainer.PNG)

3. 가상 서버의 port와 container port 연결

   - **Manual network port publishing**  클릭

   - Nginx는 웹 서버의 port로 기본적으로 사용하는 port가 80

   - 80-80으로 테스트 

     ![manual network port publishing](03_Docker Container,Image.assets/manual network port publishing.PNG)

 4. Deployment in Progress 선택 

 5. 설치 완료

    ![nginx설치](03_Docker Container,Image.assets/nginx설치.PNG)

6. IP로 접속 확인

   - 80 port이기 때문에 기본 IP만 입력

   ![IP 접속 테스트](03_Docker Container,Image.assets/IP 접속 테스트.PNG)


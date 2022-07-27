# 배포 과정

## Docker 설치

1. 도커를 조회하고 없다면 설치한다.

```
sudo docker
```

https://docs.docker.com/engine/install/ubuntu/

2. 리눅스 기본 패키지 업데이트

```
sudo apt-get update
```

3. 필요한 패키지 설치

    ```
    sudo apt-get install \
     apt-transport-https \
     ca-certificates \
     curl \
     gnupg-agent \
     software-properties-common
    ```

    - 에러가 발생하면
        - https://blog.cosmosfarm.com/archives/248/%EC%9A%B0%EB%B6%84%ED%88%AC-18-04-%EB%8F%84%EC%BB%A4-docker-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95/

    ```
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

4. Docker의 공식 GPG 키 추가

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

5. stable repository 설정

```
sudo add-apt-repository \
 "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
 $(lsb_release -cs) \
 stable"
```

6. apt update

```
sudo apt-get update
```

7. docker 엔진 설치

    ```
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```

8. 설치확인

    ```
    sudo docker
    ```

## Portainer 설치

```
sudo docker volume create portainer_data
```

```
sudo docker run -d -p 9000:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

```
sudo docker container ls
```



## Jenkins 설치

```
# apt/apt-get 업데이트
apt update
# java jdk 설치
sudo apt install openjdk-11-jdk
sudo apt install default-jdk
# java 설치 확인 
java -version
# jenkins debian 설치 
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get install jenkins
# 프론트엔드 관련 패키지 설치
sudo apt install nodejs
node -v
# jenkins 서비스 시작
service jenkins start
```

#### Jenkins 서비스 시작 시 credential을 요구할 때 

```
ubuntu@ip:~$ service jenkins start
==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentication is required to start 'jenkins.service'.
Authenticating as: Ubuntu (ubuntu)
Password:
```

```
#나의 계정 확인 
whoami
#패스워드 설정 경로
password ubuntu 
```

- passwd ubuntu로 이동해서 password 설정 후 인증하기

### jenkins로 접속

- ip:8080
- Credential 생성

### 필요 플러그인 설치

| Downloaded Successfully. Will be activated during the next boot |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Gitlab Merge Request Builder                                 | Downloaded Successfully. Will be activated during the next boot |
| Docker API                                                   | Downloaded Successfully. Will be activated during the next boot |
| Docker                                                       | Downloaded Successfully. Will be activated during the next boot |
| GitLab                                                       | Downloaded Successfully. Will be activated during the next boot |
| Docker Pipeline                                              | Downloaded Successfully. Will be activated during the next boot |
| docker-build-step                                            | Downloaded Successfully. Will be activated during the next boot |
| GitLab Authentication                                        | Downloaded Successfully. Will be activated during the next boot |
| Handy Uri Templates 2.x API                                  | Downloaded Successfully. Will be activated during the next boot |
| GitLab Branch Source                                         | Downloaded Successfully. Will be activated during the next boot |
| Docker API                                                   | Downloaded Successfully. Will be activated during the next boot |
| Jenkins 재시작                                               | Downloaded Successfully. Will be activated during the next boot |

### gitlab 연결

프로젝트명 : test_deploy


# AWS IaaS 를 활용한 CI/Cd

## Jenkins Pipeline 인프라 구축

### Overview

![image-20221023233116666](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023233116666.png)

- 개발자가 소스코드를 push 
- jenkins가 trigger를 받아 job을 실행
  - 도커 이미지 빌드, ec2 배포, 테스트 등 
- 작업 실패 시 slack notification 

#### Jenkins archi

![image-20221023233521491](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023233521491.png)

- AWS 단일 VPC를 Pubilc과 Private subnet으로 나누고, jenkins는 private에 위치 

#### Network Infra 

![image-20221023233528878](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023233528878.png)

- 단일 VPC의 public subnet은 vpc 대역 외에는 IGW(Internet GateWay)로 가도록 
- Private subnet은 vpc 대역 외에는 (Network Address Translation)으로 보내 인터넷 사용 가능하도록 



#### Bastion 

![image-20221023233817436](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023233817436.png)

- 개발자는 Bastion 서버의 Pubilc IP로 SSH 접근을 하고, Bastion 서버에서 Jenkins로 SSH 접근 
- Public에 Application LB를 설정해 다른 개발자 접근 가능 


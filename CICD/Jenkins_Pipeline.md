# AWS IaaS 를 활용한 CI/Cd

## Jenkins Pipeline

### 개념

- Jenkins Plugin의 묶음
- Jenkins 2버전 이후 부터 제대로 활용 가능 (1.642.3 버전에서 소개됨)
- Jenkins Pipeline Plugin 설치를 해야 활용 가능 
- CD를 support 하기 위해 나온 기능
- Pipeline을 코드로 작성 가능 (Jenkinsfile이라는 명세를 따름 ) 

![image-20221023231033273](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023231033273.png)

#### Scripted pipeline(script 형태)

- groovy script 작성 가능 
- Java API referencing으로 프로그래밍 
- 개발자들에게 자유도가 높지만, 프로그래밍이 복잡해서 작업 명세가 복잡해짐

```groovy
node {					#1
	stage('Build') { 	#2
	// 					#3
	}
    stage('Test') { 	#4
	// 					#5
	}
	stage('Deploy') {	#6
	// 					#7
	}
}
```



#### Declarative pipeline(선언적 형태 ) 

- Jenkins DSL 을 따름
- 복잡한 로직들을 Jenkins plugin으로 구분 

```groovy
pipeline{
	agent any 			#1
	stages {
		stage('Build') { #2
		steps {
				//		#3
			}
        }
        stage('Test') {	#4
        	steps{
        		// 		#5
        	}
        }
        stage('Deploy') { #6
        	steps{
        		// 		 #7
        	}
        }
	}
	
}
```



### Jenkins pipleline(syntax)

#### Section

- agent
  - 위치에 따라 역할이 다름 
  - pipeline 바로 아래는 전체 일들이 어떤 node에서 실행될 지 지정
  - stage 안에 있을 때는, stage만 특정 agent node에 실행이 되라 
- stages
  - 순차적인 작업의 명세인 stage들의 묶음
- steps
  - stage 안에서의 실행되는 단계 
- post
  - 일련의 작업들이 끝난 후 일어나는 작업
  - 위치에 따라 stages들의 작업이 끝난 후 추가적인 steps 또는 stage에 steps들의 작업이 끝난 후 추가적인 step
  - condition 
    - always
    - changed
    - fixed
    - regression
    - aborted
    - failure
    - success
    - unstable
    - unsuccessful
    - cleanup

#### Directive

- stage
  - agent 설정 (optional)
  - steps들의 묶음 

- parameters
  - pipeline을 trigger 할 때 입력 받아야할 변수를 정의
  - Type
    - string
    - text
    - BooleanParam
    - choice
    - password
- environments
  - key = value
  - pipeline 내부에서 사용할 환경변수
  - credentials() 를 통해 Jenkins credential에 접근 가능
- when
  - stage를 실행할 조건 설정 

```groovy
pipeline{
    agent any
    
    parameters {
        string(name : 'BUILD_DOCKER_IMAGE', defaultValue: 'Y', description : 'BUILD_DOCKER_IMAGE')
        string(name: 'RUN_TEST', defaulValue : 'Y', description: 'RUN_TEST')
        string(name: 'PUSH_DOCKER_IMAGE', defaultValue : 'Y', description : 'PUSH_DOCKER_IMAGE')
    }
    
    environment {
        REGION = 'ap-northeast-2'
    }
    
    stages{
        stage('===========Build Docker Image ============'){
            agent {
                docker {image 'python:3.8'}
            }
            when {
                expression { return params.BUILD_DOCKER_IMAGE == 'Y'}
            }
            steps {
                echo "Stage Build"
            }
        }
    }
    stage('============ Run test code ============'){
        when {expression { return params.RUN_TEST == 'Y'}}
        steps{
            echo "Stage Test"
        }
    }
    
    stage('=========== Push Docker Image') {
        when { expression { return params.PUSH_DOCKER_IMAGE == 'Y'}}
        steps {
            echo "Stage Test"
        }
    }
    post {
        cleanup {
            echo "Post cleanup"
        }
    }
}

```

![image-20221023232413557](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023232413557.png)

```groovy
pipeline {
    agent { label 'service || batch'} # service 나 batch가 있는 라벨
    agent { label 'service && barch'} # 둘다 있는 라벨
    agent { label 'service'}		# service가 있는 라벨 
    agent { label 'batch'}			# batch가 있는 라벨 
}
```



### Overview

![image-20221023233116666](C:\Users\SAMSUNG\AppData\Roaming\Typora\typora-user-images\image-20221023233116666.png)

- 개발자가 코드를 push 
- jenkins가 trigger를 받아 job을 실행
  - 도커 이미지 빌드, ec2 배포, 테스트 등 
- 작업 실패 시 slack notification 
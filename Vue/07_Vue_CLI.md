## Vue CLI

- Vue.js 개발을 위한 표준 도구
- 프로젝트 구성을 도와주는 역할을 하며 Vue 개발 생태계에서 표준 tool 기준을 목표로 함
- 확장 플러그인, GUI, Babel 등 다양한 tool 제공



### Node.js

- 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경
  - 브라우저 밖을 벗어 날 수 없던 자바스크립트 언어의 태생적 한계를 해결
- Chrome V8 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
- 즉, 단순히 브라우저만 조작할 수 있던 자바스크립트를 SSR 아키텍처에서도 사용할 수 있도록 함
- 2009년 Ryan Dahl에 의해 발표

### NPM (Node Package Manage)

- 자바스크립트 언어를 위한 패키지 관리자
  - Python에 Pip가 있다면 Node.js에는 NPM
  - pip와 마찬가지로 다양한 의존성 패키지를 관리
- Node.js의 기본 패키지 관리자
- Node.js 설치 시 같이 설치됨



### Vue CLI Quick start

- 설치

```
$ npm install -g @vue/cli
```

- 버전 확인

```
$ vue --version
```

- 프로젝트 생성

```
$ vue create my-first-app
```

- npm 레지스트리 변경 (환경에 따라 나오지 않을 수 있음)

- Vue 2버전 선택

```
Vue CLI v5.0.4
? Please pick a preset : (Use arrow keys)
> Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
```

- 프로젝트 디렉토리 이동

```
$ cd my-first-app
```

- 서버 실행

```
$ npm run serve
```

## Babel & Webpack

### Babel

- JavaScript compiler
- 자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구
- 과거 자바스크립트의 파편화와 표준화의 영향으로 코드의 스펙트럼이 매우 다양
  - 이 때문에 최신 문법을 사용해도 이전 브라우저 혹은 환경에서 동작하지 않는 상황이 발생
- 원시 코드(최신 버전)을 목적 코드(구 버전)로 옮기는 번역기가 등장하면서 개발자는 더 이상 내 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있게 됨 

![babel](07_Vue_CLI.assets/babel.PNG)

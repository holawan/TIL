# PTJ 03



<div style="text-align: right"> 대전_3반_김동완</div>

## 이번 ptj를 통해 배운 내용

1. Bootstrap을 이용해 반응형 웹페이지를 만들 수 있었습니다.
2. navbar에 옵션을 설정해 정렬 및 반응형 네비게이션 바를 만들 수 있었습니다.
3. Modal과 form 기능을 이용해 같은 페이지 상의 로그인 창을 만들 수 있었습니다.
4. Carousel 컴포넌트를 이용해 이미지를 자동 전환할 수 있는 기능을 구현했습니다.
5. Container와 row-col 기능을 이용해 반응형 페이지의 크기에 따라 요소가 표시되는 방향을 변경할 수 있었습니다.
6. 카드 기능을 이용해 요소의 이미지와 설명을 나타내는 페이지를 구현할 수 있었습니다.
7. aside와 LIst 컴포넌트를 이용해를 통해 sidebar를 구현할 수 있었습니다.
8. d-block, d-none 기능을 이용해 반응형 페이지의 크기에 따라 다른 요소를 보일 수 있게 되었습니다.
9. 페이징 요소를 구현할 수 있었습니다.
10. 컴포넌트 및 그리드 시스템을 활용하여 커뮤니티 서비스의 반응형 레이아웃을 구현할 수 있었습니다.



### 프로젝트 목표

- HTML을 통한 웹 페이지 마크업 분석 
- CSS 라이브러리의 이해와 활용 
- 컴포넌트 및 그리드 시스템 활용 
-  커뮤니티 서비스 반응형 레이아웃 구성 



### 개발도구

- VSCode
- Google Chrome Browser
- Bootstrap v5

### 요구사항 

커뮤니티 서비스 개발을 위한 화면 구성 단계로, 유저가 보는 프론트 엔드를 개발합니다. 
아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다. 

## A. 01_nav_footer

1. 네비게이션 바는 스크롤을 하더라도 항상 상단에 고정되어 있습니다. 
2. 로고 이미지는 images 폴더 안의 logo.png파일을 사용합니다. 
3. 로고 이미지는 클릭이 가능한 링크이며, 해당 페이지(02_home.html)로 이동해야 합니다. 
4. 네비게이션 바 내부의 네비게이션 리스트(Home, Community, Login)는 ul과 li요소를 
사용합니다. 
5. 네비게이션 바 내부의 네비게이션 리스트(Home, Community, Login)는 오른쪽에 배치합
니다. 
6. 네비게이션 리스트의 각 항목들은 클릭이 가능한 링크이며, 해당 페이지(02_home.html, 
03_community.html, #)로 이동해야 합니다. 
7. Viewport의 가로 크기가 768px 미만일 경우에는 네비게이션 리스트(Home, Community, 
Login)가 햄버거 버튼으로 교체되며, 클릭했을 시 세부 항목을 볼 수 있습니다. 
8. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Home을 강조합니다. 
9. 네비게이션 리스트의 Login 항목은 클릭 시 요소가 Modal 컴포넌트를 통하여 나타납니다. 
(페이지 이동이 일어나지 않습니다.) 
10. Modal 컴포넌트 내부에는 form요소를 배치합니다. 
11. Modal 컴포넌트에서 form요소 내부의 비밀번호는 표시되지 않습니다. 

### 결과

- 문제 접근 방법 :Navigation bar 컴포넌트를 이용하여 navbar의 뼈대를 구축한 후 기본적인 footer와 로고를 입력한 후 스타일을 정렬하자! Modal도 bootstrap의 컴포넌트를 이용하자

- code

  ``` html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
  
    <title>Navbar Footer Test</title>
  </head>
  <body>
    <!-- 01_nav_footer.html -->
    <!-- 768px에 리스트 요소가 햄버거로 될 수 있도록 navbar-expand-lg를 md로 변경  -->
    <!-- 배경을 검은색으로 만들고 스크롤 해도 나오도록 상단에 고정 -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top ">
      <!-- navbar의 요소들을 flex와 justify-content-between를 이용해 양 끝에 정렬 -->
      <div class="container-fluid  d-flex justify-content-between ">
        <a class="navbar-brand" href="02_home.html">
          <img class="logo" src="images/logo.png" alt="logo">
        </a>
          <div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="03_community.html">Comunity</a>
                </lfixed-bootoom i>
                <!-- Modal을 이용해 login을 누르면 Modal창이 나오게 함  -->
                <li class="nav-item">
                  <a href="#"  class="nav-link" data-bs-toggle="modal" data-bs-target="#login" >Login</a>
                </li>
              </ul>
            </div>
          </div>
      </div>
    </nav>
    <!-- 지난 과제에 진행했던 요소들로 배경을 만듬 -->
    <header class="nav_header d-flex flex-column justify-content-center align-items-center text-white fw-bold">
      <div class="display-2 m-3">Cinema</div>
      <div class="display-2 m-3">Community</div>
      <a class="btn btn-primary btn-lg mt-5" href="#" role="button:">Let's Go</a>
  </header>    
    <!-- Modal -->
    <!-- id를 모달에서 타겟으로 했던 login과 맞춰줍니다.  -->
  <div class="modal fade" id="login" tabindex="-1" aria-labelledby="loginLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="loginLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <!-- form을 이용해 로그인 창을 만듭니다 container를 이용해 부트스트랩 레이아웃 형성 -->
        <form action='' class="container">
         <!-- 간격을 위한 마진과 br 태그 사용 -->
          <div class="mb-3 ">
            <!-- ID를 입력받을 input 태그 -->
            <label for="loginuserid">ID </label><br>
            <input type="text" id="loginuserid" placeholder="ID를 입력하세요" name="id">
          </div>
          <div class="mb-3">
            <!-- passwords는 type=password를 이용해 안보이게 입력받기 -->
            <label for="loginuserpwd">Password</label><br>
            <input type="password"  id="loginuserpwd" placeholder="패스워드를 입력하세요" name="password">
          </div>
        <!-- Modal 하단에는 취소하는 창과 submit을 만들어 Login 버튼을 클릭하면 정보가 서버로 넘어오게 하기 -->
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="submit" class="btn btn-primary">Login</button>
          </div>
        </form>
      </div>
    </div>
  </div>
  <!-- 푸터 만들기 -->
    <footer class="fixed-bottom d-flex justify-content-center align-items-center bg-dark">
      <div class="text-center p-2 text-white">Web-bootstrap PJT, by김동완</div>
    </footer>
  
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
  </body>
  </html>
  
  ```

  ```css
  /* 01_nav_footer.css */
  /* 아래에 코드를 작성해 주세요. */
  .logo{
    width: 150px;
  }
  
  
  .nav_header {
    height: 700px;
    background-image: url('images/header.jpg');
    background-size: cover;
  }
  
  ```

- 해결 방식 

  1. Navbar 컴포넌트를 이용해 네비게에션 바의 뼈대를 구축했습니다.
  2. navbar 내부를 컨테이너로 만들고 d-flex 내부 요소를 이용해 양 끝에 요소를 정렬했습니다. 
  3. 각 리스트 요소에 href로 하이퍼링크를 줘 페이지가 전환되게 했습니다.
  4. Modal 컴포넌트를 이용해서 로그인 창을 구현하려고 했습니다.
  5. Form 요소를 이용해 로그인 창을 구현했습니다. 

- 이 문제에서 어려웠던 점 

  - 네비게이션 바는 과제 때 많이 만들어봐서 엄청 힘들지는 않았지만, Modal을 만드는데 문제가 많이 발생했습니다. 로그인 창이 닫히지 않았고, 정보가 어디로 가는지도 잘 몰랐습니다.
  - Modal footer를 form안에 넣지 않아서 문제가 발생했고, 안에 넣으니 문제가 해결되었습니다. 
  - 그리고 form에 action을 어떻게 주는지에 따라 url이 변경된다는 것을 다시 알았습니다.

- 내가 생각하는 이 문제의 포인트

  - Bootstrap 에 접근하여 자신이 원하는 컴포넌트 양식을 잘 찾아 적용하는 능력
  - flex를 이용하는 능력
  - Modal을 이용해 form을 만들 수 있는 것
  - 반응형 웹에 따라 요소를 다르게 보이게 하는 것 
  - Footer와 Navbar를 상/하단에 고정하고 스크롤을 해도 나오게 할 수 있는 것
  - 리스트에서 active한 페이지를 강조하는 것 

- 이 문제의 느낀점

  - Bootstrap요소의 의미를 잘 이해해야하는데, 그러지 못해서 계속 지웠다썼다 삽질을 했습니다. 더 공부를 해서 내가 가져오려는 컴포넌트를 손으로 직접 쓰는데는 힘이 들어도, 가져온 컴포넌트의 각 의미는 알 수 있게 노력해야겠다고 생각했습니다.

## B. 02_home

#### 요구사항 : 홈페이지 만들기

i. 네비게이션 바(Navigation Bar) 및 페이지 구성 
1. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Home을 강조합니다. 
(active) 
2. Home 페이지는 크게 상단 Header와 하단 Section요소로 이루어져 있습니다. 
ii. 헤더(Header) 
1. Header는 Carousel 컴포넌트로 구성합니다. 이미지는 최소 3장이며, 자동으로 전환됩니다. 
(images/ 폴더 안의 header 이미지들을 사용합니다.) 
iii. 섹션(Section) 
1. Box Office 문구는 자유롭게 스타일링 합니다. 
2. Section은 컨테이너 내부에 위치합니다. 
3. Section 내부의 개별 요소(article)들은 이미지, 제목, 설명을 포함하는 Card 컴포넌트로
구성합니다. (이미지는 images 폴더의 포스터 이미지를 사용합니다. (총6개)) 
4. 각 요소들은 좌우 일정한 간격으로 떨어져 있습니다. (간격은 자유롭게 설정 가능합니다.) 
5. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px미만일 경우에는 한 행
(row)에 1개씩 표시됩니다. 
6. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px이상일 경우에는 한 행
(row)에 2개 이상 자유롭게 표시합니다. 
7. 위에 명시된 내용 이외에는 자유롭게 작성합니다.

### 결과

- 문제 접근 방법 : Header를 구성할 carosuel 컴포넌트는 자동으로 넘어가야 하니까, 검색할 때 Auto를 추가로 검색해보자. 섹션을 구성할 때는 지난번에 했던 삼성 버즈 판매 페이지 구현을 참고하자. row-col을 이용해 반응형 웹페이지를 펴니하게 구현하자. 

  ``` html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
    <link rel="stylesheet" href="02_home.css">
    
    <title>Home</title>
  </head>
  <body>
  
    <!-- 01_nav_footer.html -->
    <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top ">
      <div class="container-fluid  d-flex justify-content-between ">
        <a class="navbar-brand" href="02_home.html">
          <img class="logo" src="images/logo.png" alt="logo">
        </a>
          <div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="03_community.html">Comunity</a>
                </lfixed-bootoom i>
                <li class="nav-item">
                  <a href="#"  class="nav-link" data-bs-toggle="modal" data-bs-target="#login" >Login</a>
                </li>
              </ul>
            </div>
          </div>
      </div>
    </nav>
    <!-- 02_home.html -->
    <!-- Modal -->
    <div class="modal fade" id="login" tabindex="-1" aria-labelledby="loginLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="loginLabel">Login</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <form action='' class="container">
            <div class="mb-3 ">
              <label for="loginuserid">ID </label><br>
              <input type="text" id="loginuserid" placeholder="ID를 입력하세요" name="id">
            </div>
            <div class="mb-3">
              <label for="loginuserpwd">Password</label><br>
              <input type="password"  id="loginuserpwd" placeholder="패스워드를 입력하세요" name="password">
            </div>
          
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary">Login</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <!-- header -->
    <!-- carosel 컴포넌트를 가져와서 각 이미지를 입력한다. data-vs-interval을 이용해 페이지 전환 속도를 조절한다. -->
    <header>
      <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active" data-bs-interval="2000">
            <img src="images/header1.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" data-bs-interval="2000">
            <img src="images/header2.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item" data-bs-interval="2000">
            <img src="images/header3.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
        <!-- 버튼을 클릭하면 위치에 따라 이전, 이후 사진으로 이동한다.  -->
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    </header>
    <!-- Boxoffice는 배경을 검은색으로 주고 텍스트를 중앙으로 정렬해서 강조한다. -->
    <h1 class="my-2 text-center text-white bg-dark p-2">Boxoffice</h1>
    <!-- div를 컨테이너로 선언 -->
    <div class="container">
      <section>
        <!-- class = row로 주고, 화면이 sm이하일 때는 1개만 lg 이하일때는 2개 lg 이상일때는 3개가 보이게함  -->
        <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3">
          <article>
            <!-- card 컴포넌트를 이용해 영화 사진, 제목, 설명 구현 -->
            <div class="card">
              <img src="images/movie1.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">쇼생크 탈출</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
          <article>
            <div class="card">
              <img src="images/movie2.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">죽은 시인의 사회</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
          <article>
            <div class="card">
              <img src="images/movie3.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">다크 나이트 라이즈</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
          <article>
            <div class="card">
              <img src="images/movie4.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">그랜드 부다페스트 호텔</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
          <article>
            <div class="card">
              <img src="images/movie5.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">Her</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
          <article>
            <div class="card">
              <img src="images/movie6.jpg" class="img-fluid rounded-start" alt="...">
            </div>
              <div class="card-body">
                <h5 class="card-title">위대한 쇼맨</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          </article>
        </div>
      </section>
    </div>
    <!-- 01_nav_footer.html -->
    <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->
    <footer class="fixed-bottom d-flex justify-content-center align-items-center bg-dark">
      <div class="text-center p-2 text-white">Web-bootstrap PJT, by김동완</div>
    </footer>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
  </body>
  </html>
  ```

- 해결 방식 

  1.  Bootstrap에 Carousel 컴포넌트를 찾고, 자동으로 넘어갈 수 있는 요소를 찾은 결과 구현이 가능한 기능을 찾아 적용했습니다.
  2. 카드가 들어갈 화면에는 .row-cols를 이용해 반응형 웹에 따라 보이는 카드의 수가 다르게 구현했습니다.
  3. card 컴포넌트를 이용해 영화 사진, 제목, 설명 구현을 했습니다.
  6. 성공

- 이 문제에서 어려웠던 점 

  - row-col을 구현할 때 처음 헷갈려 다시 지난 수업을 돌아봤습니다. 
  - carousel item을 순회하는 시간을 잘 알지 못했습니다. 
  
- 내가 생각하는 이 문제의 포인트

  - Crousel 활용을 할 수 있는 것
  - 반응형 웹에 따라 나타나는 요소의 수를 다르게 출력할 수 있는 것
  - Card 컴포넌트를 이용해 요소의 이미지와 제목, 설명을 구현하는 것

- 이 문제의 느낀점

  - row-col을 이용하면 반응형 웹페이지의 요소를 비교적 쉽게 구현할 수 있다.
  - 1번을 구현하니, 2번이 매우 어렵지는 않았다. 시작을 잘 구성하는 것이 중요하다고 생각되었다.



## C.  03_community 

#### 요구사항 : 커뮤니티 페이지 만들기 

i. 네비게이션 바(Navigation Bar) 및 페이지 구성 
1. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Community를 
강조합니다. (active) 
2. Community 페이지는 크게 게시판 목록, 게시판으로 이루어져 있습니다. 
3. 게시판 목록과 게시판은 div.main 요소로 둘러 쌓여 있습니다. 
4. 게시판 목록과 게시판, 게시글 페이징은 모두 컨테이너 내부에 위치합니다. 
ii. 게시판 목록 
1. 게시판 목록은 aside 요소로 이루어져 있습니다. 
2. 게시판 목록 내부의 각 항목(Boxoffice, Movies, Genres, Actors)은 List group 
컴포넌트를 활용합니다. 
3. 게시판 목록 내부의 각 항목은 클릭이 가능한 링크이지만, URL은 별도로 없이 #으
로 지정합니다. 
4. Viewport의 가로 크기가 992px 이상일 경우에는 게시판 목록 내부의 항목
(Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 좌측 1/6 만큼
의 너비를 가집니다. 
5. Viewport의 가로 크기가 992px 미만일 경우에는 게시판 목록 내부의 항목
(Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 전체만큼의 너
비를 가집니다. 
iii. 게시판 
1. 게시판은 Viewport의 가로크기에 따라 전혀 다른 요소를 표시합니다. 
A. Viewport의 가로 크기가 992px 이상일 경우에는 게시글이 표(table) 요소로 
표시되며, div.main영역의 내부에서 우측 5/6 만큼의 너비를 가집니다. 
B. Viewport의 가로 크기가 992px 미만일 경우에는 게시글이 글(article) 요소들
의 집합으로 표시되고 가로선으로 구분합니다(스타일링은 자유롭게 진행합니
다). div.main영역의 내부에서 전체만큼의 너비를 가집니다. 
2. 게시글은 글 제목, 영화 제목, 사용자 id, 작성시간으로 구성되어 있습니다. 
3. 테스트 게시글의 개수와 내용은 2개 이상으로 자유롭게 구성할 수 있습니다. 
4. 게시글 페이징(paginator)은 게시판 아래에 위치하며, 너비는 자유롭게 합니다. 
5. 게시글 페이징(paginator)은 자신의 영역 안에서 좌우 중앙 정렬되어 있습니다. 
6. 게시글 페이징(paginator) 내부의 요소들은 클릭이 가능한 링크이며, URL은 별도
로 없이 #으로 지정합니다. 

### 결과

- 문제 접근 방법 : Aside 바를 먼저 만들고 table을 만들어 서로 정렬이 되는지 확인하가. 페이지네이션 만들기, 반응형에 따라 테이블 없애기. article 만들기 

  ``` html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Custom CSS -->
    <link rel="stylesheet" href="01_nav_footer.css">
    <link rel="stylesheet" href="03_community.css">
  
    <title>Community</title>
  </head>
  <body>
  
    <!-- 01_nav_footer.html -->
    <!-- 01_nav_footer 에서 완성한 Navigation bar 코드를 붙여넣어 주세요. -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top ">
      <div class="container-fluid  d-flex justify-content-between ">
        <a class="navbar-brand" href="02_home.html">
          <img class="logo" src="images/logo.png" alt="logo">
        </a>
          <div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <li class="nav-item">
                  <a class="nav-link"  href="02_home.html">Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="03_community.html">Comunity</a>
                </lfixed-bootoom i>
                <li class="nav-item">
                  <a href="#"  class="nav-link" data-bs-toggle="modal" data-bs-target="#login" >Login</a>
                </li>
              </ul>
            </div>
          </div>
      </div>
    </nav>
    <!-- 02_home.html -->
    <!-- Modal -->
  	<div class="modal fade" id="login" tabindex="-1" aria-labelledby="loginLabel" aria-hidden="true">
  		<div class="modal-dialog">
  			<div class="modal-content">
  				<div class="modal-header">
  					<h5 class="modal-title" id="loginLabel">Login</h5>
  					<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
  				</div>
  				<form action='' class="container">
  					<div class="mb-3 ">
  						<label for="loginuserid">ID </label><br>
  						<input type="text" id="loginuserid" placeholder="ID를 입력하세요" name="id">
  					</div>
  					<div class="mb-3">
  						<label for="loginuserpwd">Password</label><br>
  						<input type="password"  id="loginuserpwd" placeholder="패스워드를 입력하세요" name="password">
  					</div>
  				
  					<div class="modal-footer">
  						<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
  						<button type="submit" class="btn btn-primary">Login</button>
  					</div>
  				</form>
  			</div>
  		</div>
  	</div>
    <!-- 03_community.html -->
    <div class=" main container">
  		<!-- 커뮤니티 페이지 -->
      <h1 class="text-center my-5 mx-5">Community</h1>
      <!-- Sidebar -->
  		<!-- side bar 옵션을 화면이 lg 이상일때는 2칸만 차지하게 하고, 아닐때는 전부를 차지하게 함 -->
  		<div class="row">
  			<aside class="col-12 col-lg-2">
  				<!-- a 태그를 사용해 클릭이 가능하게 만들고 text-decoration을 없앰  -->
  				<ul class="list-group ">
  					<li class="list-group-item"><a class="text-decoration-none" href="#">Boxoffice</a></li>
  					<li class="list-group-item"><a class="text-decoration-none"href="#">Movies</a></li>
  					<li class="list-group-item"><a class="text-decoration-none"href="#">Genres</a></li>
  					<li class="list-group-item"><a class="text-decoration-none"href="#">Actors</a></li>
  				</ul>
  			</aside>
  <!-- Custom content-->
  			<!-- Board -->
  			<!-- aside가 lg 이상일때는 2칸을 차지하기 때문에, 테이블은 lg이상일때는 10칸을 차지하게 합니다. -->
  			<section class ="col-lg-10">
  				<!-- 테이블 요소가 lg보다 작으면 숨기고, lg이상이되면 나오게합니다. -->
  				<div class="d-none d-lg-block"> 
  					<table class="table table-striped table-hover ">
  						<thead>
  							<tr class="bg-dark text-white">
  								<th>영화 제목</th>
  								<th>글 제목</th>
  								<th>작성자</th>
  								<th>작성 시간</th>
  							</tr>
  						</thead>
  						<tbody>
  							<tr>
  								<th>쇼생크 탈출</th>
  								<th>너무 흥미진진</th>
  								<th>Rabbit</th>
  								<th>1 minutes ago</th>
  							</tr>
  							<tr>
  								<th>킹스맨</th>
  								<th>매너 메잌스 맨</th>
  								<th>king</th>
  								<th>1 minutes ago</th>
  							</tr>
  							<tr>
  								<th>모가디슈</th>
  								<th>구교환 잘생겼따</th>
  								<th>moga</th>
  								<th>2 minutes ago</th>
  							</tr>
  							<tr>
  								<th>스파이더맨</th>
  								<th>거미줄 슉슉슈슈슉</th>
  								<th>spyder</th>
  								<th>5 minutes ago</th>
  							</tr>
  							<tr>
  								<th>어벤져스</th>
  								<th>역시 마블</th>
  								<th>ironman</th>
  								<th>10 minutes ago</th>
  							</tr>
  							<tr>
  								<th>7번방의 기적</th>
  								<th>눈물 광광</th>
  								<th>잼민이</th>
  								<th>17 minutes ago</th>
  							</tr>
  							<tr>
  								<th>엑시트</th>
  								<th>킬링타임</th>
  								<th>김빵빵</th>
  								<th>20 minutes ago</th>
  							</tr>
  							<tr>
  								<th>지금 우리 학교는</th>
  								<th>좀비물 최고</th>
  								<th>zombi</th>
  								<th>30 minutes ago</th>
  							</tr>
  						</tbody>
  		
  					</table>
  				</div>
  			</div>
  <!-- lg이하가 되면 나오는 리스트 그룹입니다.. -->
        <div class="my-5">
  				<!-- 웹 크기가 lg이상이 되면 나오지 않게 합니다. -->
          <article class=" d-lg-none">
  					<!-- list group으로 클래스를 만듭니다. -->
  					<div class="list-group">
  						<a href="#" class="list-group-item list-group-item-action active" aria-current="true">
  							<div class="d-flex w-100 justify-content-between">
  								<h5 class="mb-1">너무 흥미진진</h5>
  								<small>Rabbit</small>
  							</div>
  							<p class="mb-1">쇼생크 탈출</p>
  							<small>1 minutes ago</small>
  						</a>
  						<a href="#" class="list-group-item list-group-item-action">
  							<div class="d-flex w-100 justify-content-between">
  								<h5 class="mb-1">매너 메잌스 맨</h5>
  								<small class="text-muted">king</small>
  							</div>
  							<p class="mb-1">킹스맨</p>
  							<small class="text-muted">1 minutes ago</small>
  						</a>
  						<a href="#" class="list-group-item list-group-item-action">
  							<div class="d-flex w-100 justify-content-between">
  								<h5 class="mb-1">moga</h5>
  								<small class="text-muted">3 days ago</small>
  							</div>
  							<p class="mb-1">모가디슈</p>
  							<small class="text-muted">2 minutes ago</small>
  						</a>
  					</div>
  				</article>
        </div> 
  			<!-- Paginator를 구현하고 예제 코드에 있는 disable요소를 없앱니다. -->
  			<nav aria-label="Page navigation example">
  				<!-- 중앙에 paginator를 정렬합니다.  -->
  				<ul class="pagination justify-content-center">
  					<li class="page-item ">
  						<a class="page-link" href="#">Previous</a>
  					</li>
  					<li class="page-item"><a class="page-link" href="#">1</a></li>
  					<li class="page-item"><a class="page-link" href="#">2</a></li>
  					<li class="page-item"><a class="page-link" href="#">3</a></li>
  					<li class="page-item">
  						<a class="page-link" href="#">Next</a>
  					</li>
  				</ul>
  			</nav>
      </section>
    </div>
  
    <!-- 01_nav_footer.html -->
    <!-- 01_nav_footer 에서 완성한 Footer 코드를 붙여넣어 주세요. -->
    <footer class="fixed-bottom d-flex justify-content-center align-items-center ">
      <div class="text-center p-2 text-dark">Web-bootstrap PJT, by김동완</div>
    </footer>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>  
  </body>
  </html>
  ```

- 해결 방식 

  1. aside 바를 만들고, href를 만들어 클릭이 가능하게 합니다.
  2. asidebar의 옵션을 설정해서 화면이 lg 이상일때는 2칸만 차지하게 하고, 아닐때는 전부를 차지하게 합니다. 
  2. 리스트를 sorted(x,reverse=True) 함수를 이용해 역정렬합니다. 
  2. 테이블을 만들고 요소들을 입력합니다.
  2. aside가 lg 이상일때는 2칸을 차지하기 때문에, 테이블은 lg이상일때는 10칸을 차지하게 합니다.
  3. block, none을 이용하여 테이블 요소가 lg보다 작으면 숨기고, lg이상이되면 나오게합니다.
  3. 테이블이 사라지면 나타나게 할 새로운 리스트 그룹을 만듭니다.
  3. 작은 화면에 노출할 리스트는 lg 이상이 되면 사라지게 하고, 그 미만이면 나타나게 합니다. 

- 이 문제에서 어려웠던 점 

  - block/ none을 이용할 때 어려웠습니다. 어떤 div에 넣어야할지 헷갈렸습니다.

- 내가 생각하는 이 문제의 포인트

  - 리스트 그룹 핸들링
  - aside 정렬
  - 반응형 웹에 따른 요소를 숨기고 나오게 하기 
  - 반응형 웹에 따라 크기 조절 

- 이 문제의 느낀점

  - 연습을 해도 너무 어렵다.
  - 아직 웹에 대한 이해가 부족한 것 같다.

### 후기

- 결과적으로 유사하게 페이지를 잘 구현한 것 같아서 좋았습니다.
- 각 요소에 어떤 클래스를 주어야 원하는대로 구현되는지 지식이 조금 부족합니다.
- 직접 페이지를 만들다보니, 페이지로 넘어오는 정보도 수집해서 핸들링해보고 싶습니다.
- d-flex와 컨테이너, 부트스트랩 다양한 요소에 대해 더 공부해야할 것 같습니다.
- 삽질을 하지 않기 위해 기록을 잘 해놓고 같은 실수를 반복하지 않고 싶습니다.
- 코드 리뷰를 통해 다른 사람의 코드를 보고 수정해봐야 할 것 같습니다. 
- 감사합니다 ! 






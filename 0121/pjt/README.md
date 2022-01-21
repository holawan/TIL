# PTJ 01



<div style="text-align: right"> 대전_3반_김동완</div>

## 이번 ptj를 통해 배운 내용

1. 딕셔너리에 대해서 자세히 공부하지 않고, 대부분 리스트를 이용해서 문제를 해결했어야 하는데, 실전에서는 딕셔너리가 중요하고, 웹 개발자가 되기에 필수적으로 익혀야할 항목이라 생각했습니다.
2. 여러 파일을 건너는 코드를 작성할 수 있었고, 접근에 대한 자신감이 생겼습니다.





## A. 제공되는 영화 데이터의 주요내용 수집 

#### 요구사항 :  샘플 영화데이터가 주어집니다. 이중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다.

#### 1. 제공된 데이터에서 id, title, poster_path, vote_average, overview, genre_ids 키에 해당하는 정보만 가져옵니다

#### 2. 가져온 정보를 새로운 dictionary로 반환하는 함수 movie_info를 완성합니다.

### 결과

- 문제 접근 방법 : 원하는 정보를 가져오기 위한 key 리스트를 만들고, 반복문으로 정보를 추출한다.  따라서, 데이터의 구조를 잘 살펴보고 내가 가져와야할 key 및 value의 구조에 대해서 파악한다.

- code

  ``` python
  import json
  from pprint import pprint
  
  
  def movie_info(movie):
      my_select = ['genre_ids','id','overview','poster_path','title','vote_average']
      result={}
      for key in my_select :
          result[key] = movie[key]
      return result
  
      # 여기에 코드를 작성합니다.    
      
  if __name__ == '__main__':
      movie_json = open('data/movie.json', encoding='UTF8')
      movie_dict = json.load(movie_json)
      
      pprint(movie_info(movie_dict))
  ```

- 해결 방식 

  1. my_select라는 리스트에 문제에서 요구되는 'key'를 넣어, 리스트를 생성했습니다.
  2. 새로운 dictionary를 만들기 위해 빈 dictionary를 만들었습니다.
  3. 반복문을 통해 새로운 result dictionary에 my_select의 'key'를 하나씩 대입하고 그에 따른 value를 movie의 value로 사용했습니다.
  4. 성공

- 이 문제에서 어려웠던 점 

  - 딕셔너리를 컨트럴 할 때 초기에 dict.keys(), dict.items(), dict.values() 등 다양한 함수를 시도했는데, 초기에는 빈 딕셔너리를 만들 생각을 못했습니다. 하지만, 문제를 자세히 읽고 생각이 바뀌어서 해결할 수 있었습니다.

- 내가 생각하는 이 문제의 포인트

  - 딕셔너리를 인덱싱 할 수 있는 능력
  - 빈 딕셔너리에 값을 추가할 수 있는 능력

- 이 문제의 느낀점

  - 문제를 잘 풀려면 문제를 잘 읽어야한다.

## B. 제공되는 영화 데이터의 주요내용 수정

#### 요구사항 :  이전단계에서 만들었던 데이터 중 genre_ids를 genre_names로 바꿔 반환하는 함수를 완성합니다. 완성된 함수는 다음 문제의 기본기능으로 사용됩니다. 

#### 1. 제공되는 movie.json, genres.json 파일을 활용합니다.

#### 2. movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.

#### 3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

### 결과

- 문제 접근 방법 : movie정보가 있는 json에서, 다른 json에 있는 장르이름을 가져오려면 나머지는 A문제와 똑같이 하고, if 문을 이용해서 key = genre_ids 일때의 경우에 따로 함수를 실행시키자

- code

  ``` python
  import json
  from pprint import pprint
  
  
  def movie_info(movie, genres): 
      my_select = ['genre_ids','id','overview','poster_path','title','vote_average']
      result={}
      for key in my_select :
          if key == 'genre_ids' :
              key = 'genre_names' ; val = []
              for j in range(2) :
                 for i in range(len(genres)) :
                     if movie['genre_ids'][j] == list(genres[i].values())[0] :
                           val.append(list(genres[i].values())[1])
                           result[key] = sorted(val)
          else :
              result[key] = movie[key]
              
      return result
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movie_json = open('data/movie.json', encoding='UTF8')
      movie = json.load(movie_json)
  
      genres_json = open('data/genres.json', encoding='UTF8')
      genres_list = json.load(genres_json)
  
      pprint(movie_info(movie, genres_list))
  
  
  ```

- 해결 방식 

  1. genre_ids가 아닌 다른 key들은 A문제의 해결방식과 같기 때문에 if-else문을 이용해 genre_ids가 key 일때를 따로 처리하게 합니다. 
  2. (if문 )genre_ids를 대체하고 새로운 key인 genre_names를 key로 선언하고, genre_names를 담을 val이라는 리스트를 만듭니다. 
  3. genre_ids의 value 는 2개의 항목으로 이루어진 리스트이기 때문에, 두 항목을 대체하기 위해 for j in range(2)라는 반복을 실행합니다. 
  4. for j in range(2)안에서 for i in rnage(len(genres))를 추가로 돌려, genre_ids가  genres.json의 id와 같으면 val에 genre_name의 value(장르 이름)을 추가하는 구문을 넣습니다.
  5. 최종적으로 key가 genre_ids일 경우 key를 genre_names로 바꾸고, genre_names의 value를 return 하는 구문을 만듭니다. 
  6. 성공

- 이 문제에서 어려웠던 점 

  - 반복문을 많이 썼는데 이렇게 하는게 맞는가 싶었습니다.
  - dictonary를 컨트럴 할 때, 값이 list의 형태가 아닌, items, values 등으로 나와서 추가적인 변환을 했는데, 접근 방식이 맞는지 모르겠습니다.
  - 반복문을 여러개 돌리다 보니 코드의 가독성이 낮은 것 같습니다. 

- 내가 생각하는 이 문제의 포인트

  - 딕셔너리를 인덱싱 할 수 있는 능력
  - 다른 json에 있는 정보를 key를 통해 가져오는 능력 
  - if else문으로 경우를 나누는 능력

- 이 문제의 느낀점

  - 반복문을 3개나 쓰고 조건문을 2개 사용했는데, 가독성이 너무 떨어진다. 상호 코드리뷰를 통해 보완하고 싶다. 
  - 그래도 해결해서 기분이 너무 좋았다.





## C. 다중 데이터 분석 및 수정

#### 요구사항 :  TMDB기준 평점이 높은 20개의 영화데이터가 주어집니다. 이 중 서비스 구성에 필요한 정보만 뽑아 반환하는 함수를 완성합니다. 완성된 함수는 향후 커뮤니티 서비스에서 제공되는영화 목록을 제공하기 위한 기능으로 사용됩니다

#### 1. 제공되는 movies.json, genres.json 파일을 사용합니다.

#### 2. movies.json은 영화 전체 정보를 가지고 있습니다.

#### 3. genres.json은 장르의 id, name 정보를 가지고 있습니다.

### 결과

- 문제 접근 방법 : movie.json은 movie들로 이루어진 list라서 간단히 반복문을 추가하면 쉽게 해결되겠다. 

- code

  ``` python
  import json
  from pprint import pprint
  
  
  def movie_info(movies, genres): 
      second_result = []
      for movie in movies :
          my_select = ['genre_names','id','overview','poster_path','title','vote_average'] #추출하고 싶은 key를 list에 담기 
          result={} #결과를 담을 딕셔너리 
          for key in my_select : #반복문을 통해 key를 순회 
              
              if key == 'genre_names' :#key가 장르 아이디이면 
                  val = []#key를 장르 이름으로 변경 
                  for j in range(len(movie['genre_ids'])) :
                      for i in range(len(genres)) :
  
                          if movie['genre_ids'][j] == list(genres[i].values())[0] :
                              val.append(list(genres[i].values())[1])
                              result[key] = sorted(val)
              else :
                  result[key] = movie[key]
          second_result.append(result)
  
      return second_result
          # 여기에 코드를 작성합니다.  
          
          
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='UTF8')
      movies_list = json.load(movies_json)
  
      genres_json = open('data/genres.json', encoding='UTF8')
      genres_list = json.load(genres_json)
  
      pprint(movie_info(movies_list, genres_list))
  ```
  
- 해결 방식 

  1. 결과를 담을 second_result를 만듭니다.
  2. movies는 movie들로 이루어진 리스트이기 때문에, for문을 통해서 B에서 해결했던 방식대로 movie들의 정보를 변경합니다. 
  3. 성공

- 이 문제에서 어려웠던 점 

  - 데이터를 자세히 살펴보지 않아 장르의 수가 위에 쇼생크 탈출처럼 2개라고 간과했습니다. 그래서 index 에러가 나왔고, 처음에는 코드를 계속 살펴봤지만, 문제를 알 수 없었습니다.
  - 추후에 데이터를 살펴본 결과 장르의 개수는 영화마다 다르다는 것을 알 수 있었습니다. 

- 내가 생각하는 이 문제의 포인트

  - 딕셔너리로 이루어진 리스트를 순회하는 능력

- 이 문제의 느낀점

  - 데이터의 구조를 잘 확인해야한다. 
  - 파이썬에서 지적한 에러를 직관적으로 확인하자. 
  - 리스트의 길이와 같은 수치를 선택할 때 직관에 의존하지 말고 그 변수의 최대 길이로 설정하는 것이 안정적이다. 

  

## D. 알고리즘을 통한 데이터 출력 

#### 요구사항 :  세부적인 영화 정보 중 수익 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을 낸영화를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니티 서비스에서 메인 페이지 기본정보로 사용됩니다. 

#### 1. movies.json과 movies폴더 내부의 파일들을 사용합니

#### 2. movies.json은 영화 전체 데이터를 가지고 있습니다

#### 3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.

#### 4. movies 폴더의 파일의 이름은 영화의 id로 구성되어 있습니다.
아래는 13번 id를 가지고 있는 영화의 상세정보입니다.

### 결과

- 문제 접근 방법 : 아래 코드를 참고해서 새로운 json을 open하고 for문을 돌려 수익(revenue)들을 compare라는 list에 담는다.
  그 후, max(compare)의 idx를 찾아 그 movies의 해당 index의 타이틀을 추출한다. 

- code

  ``` python
  import json
  def my_max(nums) :
      result = 0 
      for num in nums:
          if result < num:
              result = num
      return result
  def dir (id) :
      url = 'data/movies/'+str(id)+'.json'
      return url
  def max_revenue(movies):
      compare = []
      for movie in movies :
          movie_info = open(dir(movie['id']),encoding= 'UTF8')
          movie_list = json.load(movie_info)
          compare.append(movie_list['revenue'])
      idx = compare.index(my_max(compare))
      return movies[10]['title']
  
  
  
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='UTF8')
      movies_list = json.load(movies_json)
      
      print(max_revenue(movies_list))
  
  
  ```

- 해결 방식 

  1. url을 만들 dir이라는 함수를 작성합니다.(확인용)
  2. json을 열고, movies 안에 있는 movie들을 돌며 revenue를 compare라는 list에 담습니다.
  3. compare의 최대값이 있는 index를 추출합니다.
  4. movies 리스트에 최대값이 있었던 index에 접근하고 ['title']을 추출합니다.
  5. 성공

- 이 문제에서 어려웠던 점 

  - url 만들기에서 오류가 2번정도 생겼습니다.

- 내가 생각하는 이 문제의 포인트

  - json에 접근할 수 있게 함수를 수정하는 능력
  - 비교를 위한 새로운  list를 만드는 능력 
  - max index를 찾는 것 

- 이 문제의 느낀점

  - JSON에 접근하는 것에 자신감이 생겼다. 

  

## E. 알고리즘을 통한 데이터 출력 

#### 요구사항 :  세부적인 영화 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개봉 한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 데이터는 향후 커뮤니티서비스에서 추천기능의 정보로 사용됩니다

#### 1. movies.json과 movies폴더 내부의 파일들을 사용합니

#### 2. movies.json은 영화 전체 데이터를 가지고 있습니다

#### 3. movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.

#### 4. movies 폴더의 파일의 이름은 영화의 id로 구성되어 있습니다.
아래는 13번 id를 가지고 있는 영화의 상세정보입니다.

### 결과

- 문제 접근 방법 : movie_info에 접근하여 release_date를 확인한다. 날짜의 형식이 YYYY-MM-DD 형태이므로 월을 슬라이싱 하려면 x[5:7]로 할 수 있다. if문으로 12월이면 december라는 list에 담자 

- code

  ``` python
  import json
  
  def dir (id) :
      url = 'data/movies/'+str(id)+'.json'
      return url
  
  
  def dec_movies(movies):
      december = []
      for movie in movies :
          movie_info = open(dir(movie['id']),encoding= 'UTF8')
          movie_list = json.load(movie_info)
          mon_info = movie_list['release_date'][5:7]
          if int(mon_info) == 12 :
              december.append(movie['title'])
      return december
      # 여기에 코드를 작성합니다.  
          
  
  # 아래의 코드는 수정하지 않습니다.
  if __name__ == '__main__':
      movies_json = open('data/movies.json', encoding='UTF8')
      movies_list = json.load(movies_json)
      
      print(dec_movies(movies_list))
  ```

- 해결 방식 

  1. url을 만들 dir이라는 함수를 작성합니다.
  2. 개봉월을 확인하기 위해 가져온 'release_date'를 슬라이싱하고 월 정보를 추출합니다.
  3. 조건문을 통해 12월인 경우에만 영화의 제목을 담습니다.
  4. 성공 ! 

- 이 문제에서 어려웠던 점 

  - movies.json과 movies 폴더를 말씀해주셧지만 헷갈려서 점검할 때 처음에 놀랐습니다.
  - 개봉월을 확인할 때 datetime을 import 해야하나 해서 포맷팅 방식에 어려움을 겪엇지만, 슬라이싱으로 해결할 수 있다는 것을 깨닫고, 해결할 수 있었습니다. 

- 내가 생각하는 이 문제의 포인트

  - json에 접근할 수 있게 함수를 수정하는 능력
  - 날짜를 슬라이싱할 수있는 역량 

- 이 문제의 느낀점

  - 날짜를 슬라이싱 할 때에는 형식이 잘 되어 있다면 문자열 슬라이싱 방식으로 쉽게 할 수 잇다.

  

  ### 후기

  - 첫 코드가 나중의 기반이 되기 때문에 잘 짜는 것이 중요한 것 같습니다.
  - 데이터의 구조를 잘 확인할 수 있었습니다.
  - 고수가 되기 위해서는 열심히 매진하고 다양한 자료구조를 잘 이해해야할 것 같습니다.
  - 무엇보다 시간내에 해결했다는 것이 좋았습니다. 
  - 코드 리뷰를 통해 다른 사람의 코드를 보고 수정해봐야 할 것 같습니다. 
  - 감사합니다 ! 






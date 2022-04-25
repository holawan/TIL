# PTJ 02



<div style="text-align: right"> 대전_3반_김동완</div>

## 이번 ptj를 통해 배운 내용

1. 웹 크롤링을 통해 직접 최신화된 데이터를 가져오고, 다룰 수 있었습니다. 
2. 파이썬 기초 문법 및 메소드를 이용할 수 있었습니다.
2. requests를 실행 시 발생하는 타입에 따른 에러와 API 컨트럴 지식을 얻을 수 있었습니다. 
2. 요청과 응답에 대해 이해할 수 있었습니다. 



### 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 영화 데이터를 수집하는 과정입니다. 아래 기술된 사항은 필수적으로 구현해야 하는 내용입니다. 완성된 기능들은, 향후 커뮤니티 서비스에서 활용할 수 있습니다. 

## A. 인기영화 조회

#### 요구사항 :  인기 영화의 개수를 출력합니다.

#### 1. requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.

#### 2. popular를 기준으로 받아온 데이터에서 영화 리스트의 개수를 계산합니다.

#### 3. 계산한 정보를 반환하는 함수 popular_count를 완성합니다.

### 결과

- 문제 접근 방법 : API를 이용하여 데이터 베이스에 요청한 결과를 얻은 후 인기 영화의 정보에 대해 얻으려 했습니다. 

- code

  ``` python
  import requests
  from pprint import pprint
  
  def popular_count():
      BASE_URL = 'https://api.themoviedb.org/3'
      path = '/movie/popular'
      params = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'region' : 'KR',
          'language' : 'ko'
      }
      response = requests.get(BASE_URL + path, params = params).json()
      cnt = 0
      for movie in response['results'] :
          cnt += 1
      return cnt
      # 여기에 코드를 작성합니다.  
  
  
  if __name__ == '__main__':
      """
      popular 영화목록의 개수 출력.
      """
      print(popular_count())
      # => 20
  
  ```

- 해결 방식 

  1. API를 발급받고, developers.themoviedb.org를 이용해 요구되는 api_key, 한국 지역과 언어를 설정했습니다. 
  2. 서버에 요청한 결과를 json 형태로 받아와 저장했습니다. 
  3. api에 접근한 결과, 영화 정보가 'result'에 있는 것을 확인하고 result에 있는 value를 for문을 이용해 순회했습니다.
  3. 해결 

- 이 문제에서 어려웠던 점 

  - 처음에 예제와 똑같이 입력했다고 생각했지만 404에러가 계속 나와서 당황했습니다. 
  - 확인해본 결과, 슬래시가 두개 들어가있었던 것을 확인해서 해결했습니다. 

- 내가 생각하는 이 문제의 포인트

  - 딕셔너리를 컨트럴 할 수 있는 능력

  - api를 통해 DB에 접근하는 능력 

- 이 문제의 느낀점

  - 잘 안될 땐 ,결과마다 프린트 해서 뭐가 잘못되었는지 확인해야겠다고 생각했습니다. 

## B. 특정 조건에 맞는 인기 영화 조회 I 

#### 요구사항 :  popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력합니다. 

#### 1. requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.

#### 2. 받아온 데이터에서 vote_average를 기준으로 점수가 8 이상인 영화들의 목록을
리스트로 반환하는 함수 vote_average_movies를 완성합니다.

### 결과

- 문제 접근 방법 : 영화의 목록을  A와 같은 형식으로 추출합니다. response['results'] 리스트를 순회하며, 해당 리스트 내 요소가 딕셔너리 형태이므로 해당 딕셔너리의 ['vote_average'] 를 key로 value가 8이상인 영화 목록을 출력합니다.  

- code

  ``` python
  import requests
  from pprint import pprint
  
  
  def vote_average_movies():
      BASE_URL = 'https://api.themoviedb.org/3'
      path = '/movie/popular'
      params = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'region' : 'KR',
          'language' : 'ko'
      }
      response = requests.get(BASE_URL + path, params = params).json()
      
      good_movies = []
      
      for movie in response['results'] :
          if movie['vote_average']>= 8 :
              good_movies.append(movie)
      
      return good_movies
      # 여기에 코드를 작성합니다.  
  
  if __name__ == '__main__':
      """
      popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
      """
      pprint(vote_average_movies())
      # => 영화정보 순서대로 출력
  
  ```
  
- 해결 방식 

  1.  A와 같은 방식으로 영화 목록을 response['results']로 인식하였습니다. 또한 정답을 담을 good_moive라는 이름의 빈 리스트를 생성했습니다. 
  2. response['results']를 순회하며, 해당 리스트 내 원소 중 'vote_average'를 키로 가지는 value의 값이 8이상이면 good_movies리스트에 추가합니다. 
  3. 리스트를 출력합니다. 
  6. 성공

- 이 문제에서 어려웠던 점 

  - 없었습니다. 
  
- 내가 생각하는 이 문제의 포인트

  - 딕셔너리를 인덱싱 할 수 있는 능력
  - 딕셔너리 내 리스트 내부 딕셔너리를 순회할 수 있는 직관 
  - for - if 문을 이용한 평점 8이상 영화 추출 

- 이 문제의 느낀점

  - 일단 정보를 가져오기만 하면, 딕셔너리와 리스트 메소드를 통해 다양한 문제를 해결하고 인사이트를 얻을 수 있다. 



## C. 특정 조건에 맞는 인기 영화 조회 II 

#### 요구사항 :  영화목록을 평점순으로 출력하는 함수를 완성합니다. 해당 기능은 향후 커뮤니티 서비스에서기본으로 제공되는 영화 정보로 사용됩니다. 

#### 1.  requests를 이용하여 인기 영화 정보(Get Popular)에 요청을 보냅니다.

#### 2. 받아온 데이터 중 평점이 높은 영화 다섯개의 정보를 리스트로 반환하는 함수
ranking을 완성합니다.

### 결과

- 문제 접근 방법 : 영화의 평점에 따라 데이터를 리스트에 입력해야겟다고 생각했습니다. 따라서, 영화목록을 저장하고, 영화 평점을 담을 빈 리스트를 만들었습니다. 해당 리스트에 영화 평점을 반복문을 통해 입력하고, 역정렬 후 영화 평점리스트의 원소가 영화 정보 내부의 'vote_average'와 일치하면 순서대로 5개를 입력하게 했습니다. 

  ``` python
  import requests
  from pprint import pprint
  
  
  def ranking():
      BASE_URL = 'https://api.themoviedb.org/3'
      path = '/movie/popular'
      params = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'region' : 'KR',
          'language' : 'ko'
      }
      response = requests.get(BASE_URL + path, params = params).json()
      movies = response['results']
      movies_vote = []
      for movie in movies :
          movies_vote.append(movie['vote_average'])
          
      movies_vote = sorted(movies_vote, reverse=True)
      
      movie_rank = []
      
      for i in range(5) :
          for movie in movies :
              if movie['vote_average'] == movies_vote[i] :
                  movie_rank.append(movie)
                  break    
      
      return movie_rank
      # 여기에 코드를 작성합니다.  
  
  
  if __name__ == '__main__':
      """
      popular 영화목록을 정렬하여 평점순으로 5개 영화.
      """
      pprint(ranking())
      # => 영화정보 순서대로 출력
  
  ```

- 해결 방식 

  1. 영화 평점을 담을 movie_vote리스트를 만듭니다. 
  2. 영화 정보를 순회하며, 각 영화의 평점들만 movie_vote 리스트에 담습니다.
  2. 리스트를 sorted(x,reverse=True) 함수를 이용해 역정렬합니다. 
  2. 평점이 높은 순서대로 영화 정보를 저장할 movie_rank 리스트를 만듭니다.
  2. 문제에서 요구하는 5개만큼 영화정보와 평점 리스트를 순회하며, 평점 리스트의 원소와 영화 정보의 평점이 일치하면 순차적으로 append합니다. 
  3. 성공

- 이 문제에서 어려웠던 점 

  - 영화 정보가 담긴 리스트 자체에서, vote_average key의 value를 기준으로 역정렬 할 수 있을까라는 생각을 했지만, 함수에 대해 컨트럴을 하지 못해 코드가 길어졌습니다. 

- 내가 생각하는 이 문제의 포인트

  - sorted 함수를 이용한 정렬

- 이 문제의 느낀점

  - 딕셔너리 value 기준 역정렬 할 수 있는 방법을 알아보고 싶다. 
  - for문에 대한 레벨이 조금 늘어난 것 같다. 
  - 


## D. 특정 영화 추천 영화 조회

#### 요구사항 :  제공된 영화 제목을 기준으로 추천영화 목록을 출력합니다. 

#### 1. requests를 이용하여 영화 검색(Search Movies) 요청을 보냅니다.

#### 2. 응답 받은 결과를 바탕으로 id를 찾아 추천영화 목록 조회 (Get Recommendations) URL을 생성합니다.

#### 3. requests를 이용하여 URL에 요청을 보냅니다

### 결과

- 문제 접근 방법 : 영화 검색을 도와주는 DB에 접근하여 함수에 input인 title을 검색합니다. 영화 검색 결과 results가 없으면 잘못된 입력이라고 판단하고, None을 반환합니다. results와 id가 있다면 해당 id로 추천영화 id에 접근하여 추천 영화 리스트에 제목을 입력합니다. 
  
- code

  ``` python
  import requests
  from pprint import pprint
  
  
  def recommendation(title):
      BASE_URL = 'https://api.themoviedb.org/3'
      path = '/search/movie'
      params = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'region' : 'KR',
          'language' : 'ko',
          'query' : title
      }
      response = requests.get(BASE_URL + path, params = params).json()
      if response['results'] == [] :
          return None
      # 여기에 코드를 작성합니다. 
      movie_id = response['results'][0]['id'] 
  
      BASE_URL_2 = 'https://api.themoviedb.org/3'
      path_2 = f'/movie/{movie_id}/recommendations'
      params_2 = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'language' : 'ko'
      }
      response2 = requests.get(BASE_URL_2 + path_2, params = params_2).json()
      # 여기에 코드를 작성합니다.  
      recommend = response2['results']
      recommend_list = []
      for movie in recommend :
          recommend_list.append(movie['title'])
  
      return recommend_list
  
  if __name__ == '__main__':
      """
      제목에 해당하는 영화가 있으면
      해당 영화의 id를 기반으로 추천 영화 목록 구성.
      추천 영화가 없을 경우 [].
      영화 id검색에 실패할 경우 None.
      """
      pprint(recommendation('기생충'))
      # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
      pprint(recommendation('그래비티'))
      # []  => 추천 영화 없음
      pprint(recommendation('검색할 수 없는 영화'))
      # => None
  
  ```

- 해결 방식 

  1. 영화 검색 DB에 접근하여 함수에 입력된 영화로 검색합니다. 
  2. 영화 검색 결과가 없으면 None을 반환합니다.
  2. 영화의 id를 movie_id로 저장합니다. 해당 id로 영화 추천 db에 접근합니다. 
  4. 빈 영화 추천 리스트를 만듭니다.
  4. 추천 영화 정보에서 for문을 돌며 영화 제목에만 영화 추천 리스트에 저장합니다.
  4. 반환합니다. 
  5. 성공

- 이 문제에서 어려웠던 점 

  - f스트링 없이 movie_id를 넣으려 해서 에러가 났습니다.
  - 처음에 필수적으로 요구되는 query를 넣지 않아 에러가 났습니다. 

- 내가 생각하는 이 문제의 포인트

  - 처음 api를 통해 DB에서 가져온 정보를 이용해 다른 api에 즉시 접근할 수 있는 프로그래밍 능력 
  
- 이 문제의 느낀점

  - 그냥 안정적으로 하려면 결과 나올때마다 프린트를 해보는 것도 오히려 시간을 아끼는 전략이 되지 않을까 생각했습니다. 

  

## E. 배우, 감독 리스트 출력 

#### 요구사항 :  영화에 출연한 배우들과 감독의 정보가 저장된 딕셔너리를 출력합니다.

#### 1. requests를 이용하여 영화 검색(Search Movies) 요청을 보냅니다.

#### 2. 응답 받은 결과를 바탕으로 id를 찾아 크레딧 조회 (Get Credits) URL을
생성합니다.

#### 3. requests를 이용하여 URL에 요청을 보냅니다.

#### 4. cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장합니다.

#### 5. department 값이 Directing인 감독의 이름을 리스트에 저장합니다.

#### 6. 반환되는 딕셔너리는 cast, crew 두개의 key를 가지고 각각 배우리스트와 감독리스트를 value로 갖습니다.

#### 7.  완성된 딕셔너리를 반환하는 함수 credits을 완성합니다. 



### 결과

- 문제 접근 방법 :함수에 입력된 영화 제목으로 검색을 진행하고 DB내에서 id를 통해 해당 영화의 credit 정보에 접근합니다. cast 를 키로 가지는 리스트는 cast로 crew를 key로 가지는 리스트는 crew로 저장합니다. 

- 해당 리스트를 각각  순회하며 cast_id가 10 미만인 정보를 찾고, 역할이 Directing인 정보를 찾아 각각 lst1과 lst2에 저장하고 빈 딕셔너리에 cast와 crew를 key로 lst1과 lst2를 벨류로 추가합니다.  

- code

  ``` python
  import requests
  from pprint import pprint
  
  
  def credits(title):
      BASE_URL = 'https://api.themoviedb.org/3'
      path = '/search/movie'
      params = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'region' : 'KR',
          'language' : 'ko',
          'query' : title
      }
      response = requests.get(BASE_URL + path, params = params).json()
      if response['results'] == [] :
          return None
      # 여기에 코드를 작성합니다. 
      movie_id = response['results'][0]['id'] 
  
      BASE_URL_2 = 'https://api.themoviedb.org/3'
      path_2 = f'/movie/{movie_id}/credits'
      params_2 = {
          'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
          'language' : 'ko'
      }
      response2 = requests.get(BASE_URL_2 + path_2, params = params_2).json() 
      result = {}
  
      cast = response2['cast']
      lst1 = [] ; lst2 = [] 
      crew = response2['crew']
      for actor in cast :
          if actor['cast_id'] < 10 :
              lst1.append(actor['name'])
      for krew in crew :
          if krew['department'] == 'Directing' :
              lst2.append(krew['name'])
      result['cast'] = lst1
      result['crew'] = lst2
  
      return result
      # 여기에 코드를 작성합니다.  
  
  
  if __name__ == '__main__':
      """
      제목에 해당하는 영화가 있으면
      해당 영화 id를 통해 영화 상세정보를 검색하여
      주연배우 목록(cast)과 제작진(crew).
      영화 id검색에 실패할 경우 None.
      """
      pprint(credits('기생충'))
      # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
      pprint(credits('검색할 수 없는 영화'))
      # => None
  
  ```

- 해결 방식 

  1. API를 이용해 받아온 영화 제목으로 검색을 진행합니다. 
  2. 검색 후 id를 찾아 해당 id로  credit에 접근합니다. 
  3. cast 정보가 있는 리스트를 cast 리스트에 저장하고, crew 정보가 있는 리스트는 crew 리스트에 저장합니다.
  3. 결과를 반환할 빈 dictionary를 준비합니다.
  3. 반복문을 통해 cast리스트에서 cast_id가 10 미만이면 lst1에 저장합니다. 반복문을 통해 crew 리스트에서 department가 directing이면 lst2에 저장합니다.
  3. lst1,lst2를 cast key, crew key로 빈 딕셔너리에 집어넣습니다. 
  4. 성공 ! 

- 이 문제에서 어려웠던 점 

  - 반복문을 많이 썼는데 차선책이 있을 것 같습니다. 
  - 딕셔너리와 리스트가 중첩되어 있을 때 원하는 정보에  접근이 어려웠습니다.

- 내가 생각하는 이 문제의 포인트

  - 딕셔너리를 자유자재로 접근하는 것
  - 반복문 사용으로 원하는 정보만 추출 

- 이 문제의 느낀점

  - 연습만이 살길이다. 다양한 케이스를 연습해서, 원하는 정보를 가져오고 제공하는데 노력해야겠다. 

  ## F. 특정 영화 배우, 감독 리스트 조회 (선택) 

  ``` python
  import requests 
  import re 
  from pprint import pprint
  def title(genre) :
      id = 'a_N77ZgBkxVXP0wtJyrZ'
      password = 'yrmkUF3R6v'
      params = {'X-Naver-client-Id':id,
      'X-Naver-Client-Secret':password
      }
      BASE_URL = f'https://openapi.naver.com/v1/search/movie.json?query={genre}&genre=5&display=100'
      result = requests.get(BASE_URL,headers=params).json()['items']
      movie_title = []
      for movie in result :
          title = movie['title']
          r_title = re.sub('<b>|</b>','',title)
          movie_title.append(r_title)
      return result
  
  
  def title_actor(genre) :
      id = 'a_N77ZgBkxVXP0wtJyrZ'
      password = 'yrmkUF3R6v'
      params = {'X-Naver-client-Id':id,
      'X-Naver-Client-Secret':password
      }
      BASE_URL = f'https://openapi.naver.com/v1/search/movie.json?query={genre}&genre=5&display=100'
      result = requests.get(BASE_URL,headers=params).json()['items']
      movie_info = {}
      for movie in result :
          actor = movie['actor']
          r_actor = re.sub('<b>|</b>|\|',',',actor)
          director = movie['director']
          r_director = re.sub('\|',',',director)
          movie_info[r_actor] = r_director
      return movie_info
  
  
  
  if __name__ == '__main__':
      """
      로맨스 장르의 영화 제목 추출 
      """
      pprint(title('드라마'))
      """
      로맨스 장르의 영화 배우와 감독 추출 
      """
      pprint(title_actor('로맨스'))
  
  ```
  
  해결 방식 
  
  1. 네이버 API를 이용해 영화 장르를 입력하여 json에 접근합니다. 
  2. 검색 후 title과 배우를 찾아 새로운 리스트에 저장합니다. 
  3. <b></b>와 같은 Html 태그를 re.sub()함수를 이용해 제거합니다. 
  4. 결과를 반환할 빈 dictionary를 준비합니다.
  5. 영화 배우를 key로 감독을  value로 리스트를 구성합니다. 
  
  ### 후기
  
  - API로 실제 데이터에 접근해본 것이 너무 재밌었습니다.
  - 데이터의 구조를 잘 확인할 수 있는 json viewer로 나중에 실제 프로젝트를 할 때도 도움이 될 것 같습니다. 
  - sort함수의 람다를 이용하는 방법에 대해 처음에 몰랐지만 알게 되어서 좋았습니다. 
  - 무엇보다 시간내에 해결했다는 것이 좋았습니다. 
  - 코드 리뷰를 통해 다른 사람의 코드를 보고 수정해봐야 할 것 같습니다. 
  - 감사합니다 ! 






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

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

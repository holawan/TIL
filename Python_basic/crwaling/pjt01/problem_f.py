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
    로맨스 장르의 영화배우와 감독 추출
    """
    pprint(title_actor('로맨스'))

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

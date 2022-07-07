from django.shortcuts import render
import requests
import random
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
    
    for i in range(6) :
        for movie in movies :
            if movie['vote_average'] == movies_vote[i] :
                info = info = [movie['title'],movie['vote_average'],movie['release_date'],movie['overview'],movie['poster_path'],movie['id'],movie['backdrop_path']]
                movie_rank.append(info)
                break    
    

    return movie_rank

def movie_recommendation(title):
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
        info = [movie['title'],movie['vote_average'],movie['release_date'],movie['overview'],movie['poster_path'],movie['id']]
        recommend_list.append(info)

    return recommend_list

# Create your views here.
def index(request) :


    return render(request,'index.html')


def recommendations(request) :
    rec = random.choice(movie_recommendation('쇼생크 탈출'))
    context = {
        'title' : rec[0],
        'vote_average' : round(rec[1],1),
        'release_date' : rec[2],
        'overview' : rec[3],
        'poster' : rec[4],
        'id' : rec[5]
    }
    return render(request,'recommendations.html',context)
import json
from pprint import pprint


def movie_info(movie, genres): 
    my_select = ['genre_ids','id','overview','poster_path','title','vote_average'] #추출하고 싶은 key를 list에 담기 
    result={} #결과를 담을 딕셔너리 
    for key in my_select : #반복문을 통해 key를 순회 
        if key == 'genre_ids' :  #key가 장르 아이디이면 
            key = 'genre_names' ; val = [] #key를 장르 이름으로 변경 
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


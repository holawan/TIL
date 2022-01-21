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
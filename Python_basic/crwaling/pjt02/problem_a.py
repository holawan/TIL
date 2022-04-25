
import json
from pprint import pprint


def movie_info(movie):
    my_select = ['genre_ids','id','overview','poster_path','title','vote_average'] #추출하고 싶은 key를 list에 담기 
    result={} #결과를 담을 딕셔너리 만들기
    for key in my_select : #반복문을 통해 key를 순회하며, 리스트에 있는 key와 movie.json에 있는 key가 일치하면 result 딕셔너리에 추가 
        result[key] = movie[key]
    return result

    # 여기에 코드를 작성합니다.    
    
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
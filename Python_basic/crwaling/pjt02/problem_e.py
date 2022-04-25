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
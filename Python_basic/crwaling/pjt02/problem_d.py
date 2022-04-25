import json
def my_max(nums) :
    result = 0 
    for num in nums: 
        if result < num:
            result = num
    return result
def dir (id) :
    url = 'data/movies/'+str(id)+'.json'
    return url
def max_revenue(movies):
    compare = []
    for movie in movies :
        movie_info = open(dir(movie['id']),encoding= 'UTF8')
        movie_list = json.load(movie_info)
        compare.append(movie_list['revenue'])
    idx = compare.index(my_max(compare))
    return movies[10]['title']



if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

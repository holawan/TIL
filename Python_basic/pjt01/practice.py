import requests
BASE_URL = 'https://api.themoviedb.org/3/'
path = '/movie/popular'
params = {
    'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
    'region' : 'KR',
    'language' : 'ko'
}


response = requests.get(BASE_URL+path, params = params)
print(response)
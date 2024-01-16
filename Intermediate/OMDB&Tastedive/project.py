import requests_with_caching
import json
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

def get_movies_from_tastedive(movie_name: str)->str:
    param_dic = {}
    param_dic["q"] = movie_name
    param_dic["type"] = "movies"
    param_dic["limit"] = "5"
    response_object = requests_with_caching.get("https://tastedive.com/api/similar", params = param_dic)
    return response_object.json()

result = get_movies_from_tastedive("Black Panther")
result2 = get_movies_from_tastedive("Bridesmaids")
print(result)
print(result2)

"""
Please copy the completed function from above into this active code window. 
Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive.
Call it extract_movie_titles.
"""
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))
def get_movies_from_tastedive(movie_name: str)->str:
    param_dic = {}
    param_dic["q"] = movie_name
    param_dic["type"] = "movies"
    param_dic["limit"] = "5"
    response_object = requests_with_caching.get("https://tastedive.com/api/similar", params = param_dic)
    return response_object.json()

def extract_movie_titles(json_result: str)->list:
    lst = []
    for dic in json_result["Similar"]["Results"]:
        lst.append(dic["Name"])
    return lst
    
result = get_movies_from_tastedive("Black Panther")
result2 = get_movies_from_tastedive("Tony Bennett")

movie_lst = extract_movie_titles(result)
print(movie_lst)
movie_lst = extract_movie_titles(result2)
print(movie_lst)

"""
------------Understand->Extract->Repeat process---------------
print(result2)
print(type(result2))
print(result2.keys())

similar = result2["Similar"]
print(similar)
print(type(similar))
print(similar.keys())

similar = result2["Similar"]["Results"]
print(similar)
print(type(similar))

similar = result2["Similar"]["Results"][0]
print(similar)
print(type(similar))
print(similar.keys())

similar = result2["Similar"]["Results"][0]["Name"]
print(similar)
"""

"""
Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. 
It takes a list of movie titles as input. 
It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
"""

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])


def get_movies_from_tastedive(movie_name: str)->str:
    param_dic = {}
    param_dic["q"] = movie_name
    param_dic["type"] = "movies"
    param_dic["limit"] = "5"
    response_object = requests_with_caching.get("https://tastedive.com/api/similar", params = param_dic)
    return response_object.json()

def extract_movie_titles(json_result: str)->list:
    lst = []
    for dic in json_result["Similar"]["Results"]:
        lst.append(dic["Name"])
    return lst

def get_related_titles(title_lst: list)->list:
    lst_so_far = []
    
    for item in title_lst:
        result = get_movies_from_tastedive(item)
        movie_lst = extract_movie_titles(result)
        for item2 in movie_lst:
            if item2 not in lst_so_far:
                lst_so_far += [item2]
    return lst_so_far
    
finallst = get_related_titles(["Black Panther", "Captain Marvel"])
print(finallst)

"""
Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. 
You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache
"""
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")

def get_movie_data(title:str)->dict:
    params_dic = {}
    params_dic["t"] = title
    params_dic["r"] = "json"
    baseurl = "http://www.omdbapi.com/"
    response_obj = requests_with_caching.get(baseurl, params = params_dic)
    return response_obj.json()
    
result = get_movie_data("Venom")
print(result)
print(type(result))

"""
Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. 
It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. 
For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0
"""
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

def get_movie_data(title:str)->dict:
    params_dic = {}
    params_dic["t"] = title
    params_dic["r"] = "json"
    baseurl = "http://www.omdbapi.com/"
    response_obj = requests_with_caching.get(baseurl, params = params_dic)
    return response_obj.json()

def get_movie_rating(result: dict)->int:
    for dic in result["Ratings"]:
        if dic["Source"] == "Rotten Tomatoes":
            value = dic["Value"]
            lst = value.split("%")
            rating = int(lst[0])
            return rating
    return 0


rating = get_movie_rating(get_movie_data("Deadpool 2"))

"""
Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. 
Define a function get_sorted_recommendations. It takes a list of movie titles as an input. 
It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. 
The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. 
Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’
"""

def get_movies_from_tastedive(movie_name: str)->str:
    param_dic = {}
    param_dic["q"] = movie_name
    param_dic["type"] = "movies"
    param_dic["limit"] = "5"
    response_object = requests_with_caching.get("https://tastedive.com/api/similar", params = param_dic)
    return response_object.json()

def extract_movie_titles(json_result: str)->list:
    lst = []
    for dic in json_result["Similar"]["Results"]:
        lst.append(dic["Name"])
    return lst

def get_related_titles(title_lst: list)->list:
    lst_so_far = []
    
    for item in title_lst:
        result = get_movies_from_tastedive(item)
        movie_lst = extract_movie_titles(result)
        for item2 in movie_lst:
            if item2 not in lst_so_far:
                lst_so_far += [item2]
    return lst_so_far

def get_movie_data(title:str)->dict:
    params_dic = {}
    params_dic["t"] = title
    params_dic["r"] = "json"
    baseurl = "http://www.omdbapi.com/"
    response_obj = requests_with_caching.get(baseurl, params = params_dic)
    return response_obj.json()

def get_movie_rating(result: dict)->int:
    for dic in result["Ratings"]:
        if dic["Source"] == "Rotten Tomatoes":
            value = dic["Value"]
            lst = value.split("%")
            rating = int(lst[0])
            return rating
    return 0

def get_sorted_recommendations(title_lst:list)->list:
    rating_lst = []
    rating_dic = {}
    for movie in title_lst:
        rating = get_movie_rating(get_movie_data(movie))
        if movie not in rating_dic:
            rating_dic[movie] = 0
        rating_dic[movie] = rating
    sorted_lst = sorted(rating_dic.items(), key = lambda tup: (tup[1], tup[0]), reverse = True)
    for key,val in sorted_lst:
        rating_lst.append(key)
    return rating_lst

recommendations = get_sorted_recommendations(get_related_titles(["Bridesmaids", "Sherlock Holmes"]))
print(recommendations)  
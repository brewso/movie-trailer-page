import media
import fresh_tomatoes
import urllib.request
import re
import requests

# search movie trailer on youtube return first result
def find_video(title):
    raw_string = title + " trailer"
    query_string = raw_string.replace(" ", "+")
    html_content = urllib.request.urlopen("http://www.youtube.com/results?search_query=" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return("http://www.youtube.com/watch?v=" + search_results[0])

# use omdb to get information about movie
def omdbapi(title, year):
    key = '6879b5a5'
    search = title.replace(" ","+")
    url = "http://www.omdbapi.com/?t="+search+"&y="+year+"&apikey="+key
    response = requests.get(url)
    return(json.loads(response.text))


toy_story_omdb = omdbapi("toy story", "1995")
toy_story = media.Movie(toy_story_omdb["Title"],
                        toy_story_omdb["Plot"],
                        toy_story_omdb["Poster"],
                        find_video("Toy Story"))

pulp_fiction_omdb = omdbapi("pulp fiction", "1994")
pulp_fiction = media.Movie(pulp_fiction_omdb["Title"],
                            pulp_fiction_omdb["Plot"],
                            pulp_fiction_omdb["Poster"],
                            find_video("Pulp Fiction"))

good_will_hunting_omdb = omdbapi("good will hunting", "1997")
good_will_hunting = media.Movie(good_will_hunting_omdb["Title"],
                                good_will_hunting_omdb["Plot"],
                                good_will_hunting_omdb["Poster"],
                                find_video("Good Will Hunting"))

star_wars_omdb = omdbapi("star wars", "1977")
star_wars = media.Movie(star_wars_omdb["Title"],
                        star_wars_omdb["Plot"],
                        star_wars_omdb["Poster"],
                        find_video("Star Wars: A New Hope"))

fast_and_furious_omdb = omdbapi("The Fast and the Furious", "2001")
fast_and_furious = media.Movie(fast_and_furious_omdb["Title"],
                        fast_and_furious_omdb["Plot"],
                        fast_and_furious_omdb["Poster"],
                        find_video("The Fast and the Furious"))

gladiator_omdb = omdbapi("gladiator", "2000")
gladiator = media.Movie(gladiator_omdb["Title"],
                        gladiator_omdb["Plot"],
                        gladiator_omdb["Poster"],
                        find_video("Gladiator"))

movies = [gladiator,fast_and_furious,star_wars,toy_story,good_will_hunting,pulp_fiction]
fresh_tomatoes.open_movies_page(movies)

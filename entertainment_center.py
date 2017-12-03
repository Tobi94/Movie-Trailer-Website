"""Stores information of movies and displays them on a website."""

import media
import fresh_tomatoes

def main():
    """Creates Tree Movie objects and initializes them"""
    toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "1996")
    star_wars = media.Movie("Star Wars: The Force Awakens", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/2/20/Das_erwachen_der_macht_logo.svg", "https://www.youtube.com/watch?v=0IjOPqiyVik", "2015")
    transformers = media.Movie("Transformers: The Last Knight", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/4/49/Transformers_5_El_%C3%9Altimo_caballero.png", "https://www.youtube.com/watch?v=R4nrFuJedyk", "2016")


    # Store movies in array
    movies = [toy_story, star_wars, transformers]

    # Open website in browser
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()

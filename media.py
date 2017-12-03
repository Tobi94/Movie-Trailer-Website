"""Defines the Movie class"""
import webbrowser


class Movie():
    """This class stores movie related data

    Attributes:
        title: A string to store the title
        storyline: A string to store the storyline
        poster_image_url: A string to store the URL of the poster image
        trailer_youtube_url: A string to store the URL of the trailer on youtube
        release_date: A string to store the release year of the movie
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_release):
        """Initialises Movie class instance variables."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release

    def show_trailer(self):
        """Plays the movie trailer"""
        webbrowser.open(self.trailer_youtube_url)

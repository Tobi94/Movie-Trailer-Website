import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
toy_story2 = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
toy_story3 = media.Movie("Toy Story", "A Story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Toy_Story_logo.svg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [toy_story, toy_story2, toy_story3]
fresh_tomatoes.open_movies_page(movies)

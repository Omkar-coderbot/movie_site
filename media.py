import webbrowser


# movie class holds the movie info we need.
class Movie():
    # this is where we initiate all the titles, storylines, posters, and trailers.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show_trailer method opens youtube video in browser.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

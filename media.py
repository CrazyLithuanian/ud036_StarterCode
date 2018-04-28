import webbrowser
class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        """ The initializer initializes movie title, storyline,
        poster image url and trailer url from youtube,
            these must be supplied while initializing the class"""
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # ================ These functions are mostly used for debugging purposes =
    def print_title(self):
        """Prints the title of the movie"""
        print(self.title)

    def print_storyline(self):
        """Print the storyline"""
        print(self.storyline)

    def show_poster(self):
        """Opens poster in the browser"""
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        """Opens trailer in the browser"""
        webbrowser.open(self.trailer_youtube_url)
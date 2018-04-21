import webbrowser
class Movie():
    def __init__(self, title, storyline, poster_image, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def print_title(self):
        print(self.title)

    def print_storyline(self):
        print(self.storyline)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
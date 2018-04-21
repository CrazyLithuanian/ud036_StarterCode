# Fresh tomatoes movie site
## Introduction
The python script here creates a HTML file, that contains list of my favorite movies. There are their posters
as well as youtube trailers of each movie.
## Requirements
* Python (tested on 3.6, may work on other versions)
* Web Browser (to run HTML)
* Internet connection
## Installing and running
1. Download or clone this repository
2. Launch 'entertainment_center.py' (make sure it is in the same folder as 'media.py' as well as 'fresh_tomatoes.py'
3. The movie site will be generated and opened in the browser.
4. After script have generated 'fresh_tomatoes.py' file, if can be opened any time without running the script.
## Known issues
### Page design is not responsive
Since the page is using external libraries like jquery and bootstrap if these are not in catch you may need internet connection.
JavaScript should also be enabled for full functionality
### Posters and trailers aren't shown
This usually happens when there is no internet connection. Although the output itself, an HTML file can be viewed offline,
if will not work as supposed to unless it can access internet.
## Modifying the movie list.
The movie list is located in 'entertainment_center.py' file. Each movie entry is located in it's own line, it can be modified
or deleted. If it is deleted it supposed to be removed from movies array. To add a movie, first of all it needs to create
an instance of movie class `(media.Movie())`. Movie class accepts four parameters 'title', 'story', 'poster' and 'youtube_trailer'
first two supposed to be simple string variables, while poster should contain url of an image and youtube_trailer link to youtube
video respectively. This instance should also be added to movies array.

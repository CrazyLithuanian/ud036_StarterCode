import media
import fresh_tomatoes

# =============== Movie list ==================================================
# Creating instance of movie "The Matrix"
matrix = media.Movie('The Matrix', 'In near future people are plugged into'
                                   ' virtual reality machine, some of them'
                                   ' escaped and helping others escape',
                     'http://www.impawards.com/1999/posters/matrix_ver2.jpg',
                     'https://www.youtube.com/watch?v=m8e-FF8MsqU')
# Creating instance of movie "A.I. Artificial intelligence"
ai = media.Movie('A.I. Artificial Intelligence',
                 'A boy robot wants to become a human',
                 'http://www.impawards.com/2001/posters/'
                 'ai_artificial_intelligence_ver5.jpg',
                 'https://www.youtube.com/watch?v=_19pRsZRiz4')
# Creating instance of movie "Inception"
inception = media.Movie('Inception',
                        'Dreams are used to influence subconscious',
                        'http://www.impawards.com/2010/posters/'
                        'inception.jpg',
                        'https://www.youtube.com/watch?v=YoHD9XEInc0')
# Creating instance of movie "Clockwork Orange"
clockwork_orange = media.Movie('Clockwork Orange',
                               'A deviant teen, gets transformed by '
                               'psychological conditioning',
                               'http://retromovieposter.com/wp-content/uploads'
                               '/2015/03/1971-A-Clockwork-Orange-small'
                               '.jpg',
                               'https://www.youtube.com/watch?v=vN-1Mup0UI0')
# Creating instance of movie "The Birds"
birds = media.Movie('The Birds', 'Birds begins attacking people',
                    'http://www.impawards.com/1963/posters/birds_ver3_xlg.jpg',
                    'https://www.youtube.com/watch?v=towd2xnkd9U')
# Creating instance of movie "Night of the Living Dead"
living_dead = media.Movie('Night of the Living Dead',
                          'Dead comes to life to kill and ead the living',
                          'https://s3.amazonaws.com/'
                          'criterion-production/shop_product_images/771'
                          '-9f3e4755c8585f0bbd196b303d7306ed/CTA1145_original.jpg',
                          'https://www.youtube.com/watch?v=0TAGtIQvebs')
# Creating instance of movie "8 Mile"
mile8 = media.Movie('8 Mile', 'Talented rapper finds himself in'
                              ' dead-end job, homeless, working his way out',
                    'https://pre00.deviantart.net/39ab/th/pre/i/2015/364/3/e/'
                    '8_mile_fan_poster_by_krisiskiller105-d9m1jkw.png',
                    'https://www.youtube.com/watch?v=axGVrfwm9L4')

# Adding all the instances into single array
movies = [matrix, ai, inception, clockwork_orange, birds, living_dead, mile8]
fresh_tomatoes.open_movies_page(movies)

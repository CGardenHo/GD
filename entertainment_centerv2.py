# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 10:33:11 2017

@author: garde
"""
import fresh_tomatoes
import media
Transforms = media.Movie("Transforms",
                        "The Last Knight",
                        "https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg",
                        "https://www.youtube.com/watch?v=6Vtf0MszgP8")

Pirates_of_the_Caribbean = media.Movie("Pirates of the Caribbean",
                     "Dead Men Tell No Tales",
                     "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                     "https://www.youtube.com/watch?v=KpFMVcZ4o7U")

Spider_Man = media.Movie("Spider Man", 
                             "Homecoming",
                             "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                             "https://www.youtube.com/watch?v=39udgGPyYMg")

Star_war = media.Movie("Star War", 
                          "The last Jedi",
                             "https://upload.wikimedia.org/wikipedia/en/7/7f/Star_Wars_The_Last_Jedi.jpg",
                             "https://www.youtube.com/watch?v=Q0CbN8sfihY")

Wonder_Woman = media.Movie("Wonder Woman", 
                                "Diana then leaves her home in order to end the conflict",
                             "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                             "https://www.youtube.com/watch?v=VSB4wGIdDwo")

Coco = media.Movie("Coco", 
                   "Desperate to prove his talent, Miguel finds himself in the stunning and colorful Land of the Dead following a mysterious chain of events",
                             "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
                             "https://www.youtube.com/watch?v=zNCz4mQzfEI")

movies = [Transforms, Pirates_of_the_Caribbean, Spider_Man, Star_war, Wonder_Woman, Coco ]
fresh_tomatoes.open_movies_page(movies)

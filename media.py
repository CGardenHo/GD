# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 10:34:41 2017

@author: garde
"""
import webbrowser
class Movie():
    """ This class provides a way to sotre movie related information """
    
    #valid_ratings = ["G", "PG", "PG-13", "R"]
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        #udacity.title = movie_title
        self.storyline = movie_storyline
        #udacity.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #udacity.poster_image_url = poster_image
        #udacity.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
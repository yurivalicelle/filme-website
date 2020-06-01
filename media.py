# -*- coding: utf-8 -*-
"""This module provides a way to store related information."""
import webbrowser


class Movie:
    """This class provides a way to store related information."""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """
        Initialize self.  See help(type(self)) for accurate signature.

        Args:
            movie_title (str): Movie title.
            movie_storyline (str): Movie storyline.
            poster_image (str): URL for to the movie poster image.
            trailer_youtube (str): URL for the movie trailer on YouTube.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Display URL for the movie trailer on YouTube using the default browser."""
        webbrowser.open(self.trailer_youtube_url)

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:07:32 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

def top_tracks(artist, country, number_of_tracks):
    """ Get Spotify catalog information about an artist’s top 10 tracks by country.

    Parameters
    ----------
    artist : str
        uri/url/ID of the objective artist.
    country : str
        ex. 'US' in order to list the top tracks limiting the response to one particular country

    Returns
    -------
    None.

    """
    print('The objective aritst is: '+sp.artist(artist)['name'],'\n')
    
    for i in range(number_of_tracks):
        print('({}):'.format(i+1),sp.artist_top_tracks(artist,country=country)['tracks'][i]['name'])
        print('album: {}'.format(sp.artist_top_tracks(artist,country=country)['tracks'][i]['album']['name']))
        print('--------------\n')
        
    return None

# arctic example
top_tracks('spotify:artist:7Ln80lUS6He07XvHI8qqHH', 'IT', 5)


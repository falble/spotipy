# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:52:40 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# import pandas as pd


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))


def list_album_tracks(uri):
    """ List all the tracks for an album

    Parameters
    ----------
    uri : str
        uri/url of the album
        'spotify:artist:INSERT_HERE_SPECIFIC_URI_CODE'

    Returns
    -------
    None.

    """
    album = sp.album(uri)

    print('ALBUM NAME: ',album['name'])
    print('ARTIST: ',album['artists'][0]['name'])
    print('TYPE: ',album['album_type'])
    print('RELEASE DATE: ',album['release_date'])
    print('POPULARITY: ',album['popularity'],'\n')
    
    album_tracks = sp.album_tracks(uri)
    
    print('TRACKS: \n')
    
    for i in range(len(album_tracks['items'])):
        print('({}):'.format(i+1),album_tracks['items'][i]['name'])
     
    print('\n---------------------------------------------------------------------------------\n')   
     
    return None

# Whatever People Say I Am, That's What I'm Not example
list_album_tracks('https://open.spotify.com/album/50Zz8CkIhATKUlQMbHO3k1')



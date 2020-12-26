# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:53:59 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))


def list_single(uri):
    """ Listing all the online singles for an URI
    
    Parameters
    ----------
    uri : str
        uri of the artist
        'spotify:artist:INSERT_HERE_SPECIFIC_URI_CODE'

    Returns
    -------
    None.
    
    """
    artist = sp.artist(uri)
    print('ARTIST: ',artist['name'])
    print('GENRES: ',artist['genres'])
    print('POPULARITY: ',artist['popularity'])
    print('ACTUAL FOLLOWERS: ',artist['followers'])
    print('uri: ',artist['uri'])
    print('external_urls: ',artist['external_urls'],'\n')
    
    results = sp.artist_albums(uri, album_type='single')
    albums = results['items']
    name = []
    release_date = []
    total_tracks = []
    
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])
    
    print('SINGLES UPLOADED:\n')
    
    for album in albums:
        name.append(album['name'])
        release_date.append(album['release_date'])
        total_tracks.append(album['total_tracks'])
    
    col = ['name','release_date','total_tracks']
    df = pd.DataFrame(list(zip(name,release_date,total_tracks)),columns=col).drop_duplicates(subset='name')
    print(df)
    
    print('\n---------------------------------------------------------------------------------\n')
        
    return None

# arctic example
list_single('spotify:artist:7Ln80lUS6He07XvHI8qqHH')


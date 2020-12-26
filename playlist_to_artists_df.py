# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 02:10:45 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))


def playlist_to_artists_df(uri):
    """ transforming a playlist into a df of artists and uris (max 595 songs)
    

    Parameters
    ----------
    uri : str
        uri/url of the album
        'spotify:artist:INSERT_HERE_SPECIFIC_URI_CODE'

    Returns
    -------
    df : pd.DataFrame
        DataFrame of the playlist in order to perform some actions

    """
    playlist_1 = sp.playlist(uri)
    playlist_2 = sp.playlist_items(uri,limit=None,offset=0)
    playlist_3 = sp.playlist_items(uri,limit=None,offset=99)
    playlist_4 = sp.playlist_items(uri,limit=None,offset=198)
    playlist_5 = sp.playlist_items(uri,limit=None,offset=297)
    playlist_6 = sp.playlist_items(uri,limit=None,offset=396)
    playlist_7 = sp.playlist_items(uri,limit=None,offset=495)
    
    all_playlist = [playlist_2, playlist_3, playlist_4, playlist_5, playlist_6, playlist_7]
    
    print('name: ', playlist_1['name'])
    print('public: ',playlist_1['public'])
    print('collaborative: ',playlist_1['collaborative'])
    print('description: ',playlist_1['description'])
    print('followers: ', playlist_1['followers']['total'])
    print('\n---------------------------------------------------------------------------------\n')
    
    artist_name = []
    uris = []
    col = ['artist','uri']
    
    for playlist in all_playlist:
        if playlist != 0:
            for i in range(len(playlist['items'])):
                artist_name.append(playlist['items'][i]['track']['artists'][0]['name'])
                uris.append(playlist['items'][i]['track']['artists'][0]['uri'])
        else:
            pass
    

    df = pd.DataFrame(list(zip(artist_name,uris)), columns=col).drop_duplicates(subset=['uri'],keep='first')
    
    print('<DataFrame completed>')
    print('\n---------------------------------------------------------------------------------\n')
        
    return df

# the adults are talking example
df_1 = playlist_to_artists_df('https://open.spotify.com/playlist/2rQTtxMfmdrQOWHeEbStwM')
print(df_1)
print('Number of different artists: ',len(set(df_1.artist)))
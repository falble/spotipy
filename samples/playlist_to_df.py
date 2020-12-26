# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 17:12:06 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                            client_secret="YOUR_APP_CLIENT_SECRET"))


def playlist_to_df(uri):
    """ transforming a playlist into a df (max 595 songs)
    

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
    album_name = []
    track_name = []
    track_number = []
    popularity = []
    uris = []
    col = ['artist','album','track_name','track_number','popularity','uri']
    
    for playlist in all_playlist:
        if playlist != 0:
            for i in range(len(playlist['items'])):
                artist_name.append(playlist['items'][i]['track']['artists'][0]['name'])
                album_name.append(playlist['items'][i]['track']['album']['name'])
                track_name.append(playlist['items'][i]['track']['name'])
                track_number.append(playlist['items'][i]['track']['track_number'])
                popularity.append(playlist['items'][i]['track']['popularity'])
                uris.append(playlist['items'][i]['track']['artists'][0]['uri'])
        else:
            pass
    

    df = pd.DataFrame(list(zip(artist_name,album_name,track_name,track_number,popularity,uris)), columns=col)
    
    print('<DataFrame completed>')
    print('\n---------------------------------------------------------------------------------\n')
        
    return df

# pyhton example
df_1 = playlist_to_df('https://open.spotify.com/playlist/4KVBI6CgDDldQGlQ5BihaU')
print(df_1)
print('Number of different artists: ',len(set(df_1.artist)))
df_1_artists = list(set(df_1.artist))
df_1_artists.sort(reverse=False)
print('List of artists: ',df_1_artists)
print('\n---------------------------------------------------------------------------------\n')

# save a txt file in the same folder with these information, it can be used for playlist description
with open('playlist_df_1.txt','w',encoding="utf-8") as txt:
    txt.write('Number of different artists: '+str(len(set(df_1.artist)))+'-------- \n')
    for element in df_1_artists:
        txt.write('%s'%element+'/')


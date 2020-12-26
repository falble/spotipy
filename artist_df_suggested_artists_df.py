# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 02:14:53 2020

@author: falble
"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

from playlist_to_artists_df import playlist_to_artists_df


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))


def artist_df_suggested_artists_df(df):
    """ From a df containing the information of a playlist, this function, suggests for the 15 most featured 
    artists a dataframe of related artists according to spotify.  similarity is based on analysis of the 
    spotify community’s listening history.

    df : pd.DataFrame (containing the columns 'artist' & 'uri')
        iterable containing the uris/urls of the artists
        'spotify:artist:INSERT_HERE_SPECIFIC_URI_CODE'

    Returns
    -------
    rel_df : pd.DataFrame
        DataFrame of the suggested artists in order to perform some actions

    """
    most_frequent = df['uri'].value_counts().head(15).to_frame('uri').index
    
    rel_name = []
    rel_genres = []
    rel_uri = []
    rel_pop = []
    rel_col = ['name','genres','uri','popularity']
    
    for uri in most_frequent:
        for i in range(len(sp.artist_related_artists(uri)['artists'])):
            rel_name.append(sp.artist_related_artists(uri)['artists'][i]['name'])
            rel_genres.append(sp.artist_related_artists(uri)['artists'][i]['genres'])
            rel_uri.append(sp.artist_related_artists(uri)['artists'][i]['uri'])
            rel_pop.append(sp.artist_related_artists(uri)['artists'][i]['popularity'])
            
    rel_df = pd.DataFrame(list(zip(rel_name,rel_genres,rel_uri,rel_pop)),columns=(rel_col)).drop_duplicates(subset=['name'],keep='first')
    
    print('<DataFrame completed>')
    print('\n---------------------------------------------------------------------------------\n')
        
    return rel_df


# the adults are talking example
df = playlist_to_artists_df('https://open.spotify.com/playlist/2rQTtxMfmdrQOWHeEbStwM')
rel_df = artist_df_suggested_artists_df(df)
print(rel_df)
# example only if popularity is >= 55 
print(rel_df[rel_df['popularity']>=55].sort_values('popularity',ascending=False))
# example only if popularity is <= 60 
print(rel_df[rel_df['popularity']>=60].sort_values('popularity',ascending=False))    
    
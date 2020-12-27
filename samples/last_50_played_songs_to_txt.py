# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:31:27 2020

@author: falble
"""

import spotipy
# authorized calls
from spotipy.oauth2 import SpotifyOAuth


def last_50_played_songs_to_txt(username,scope,redirect_uri,client_id,client_secret):
    """ This function creates a txt file containing the last 50 played songs of a user.
    
    Parameters
    ----------
    username : str
        YOUR_USERNAME.
    scope : str
        'user-read-recently-played user-top-read user-read-playback-position'.
    redirect_uri : str
        ex. http://localhost:8888/callback/.
    client_id : str
        YOUR_APP_CLIENT_ID.
    client_secret : str
        YOUR_APP_CLIENT_SECRET.

    Returns
    -------
    None.

    """
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                                client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=redirect_uri,
                                                username = username
                                                ))
    
    with open('last_50_played_songs.txt','w',encoding="utf-8") as txt:
        txt.write('Listing the last ({}) played songs:'.format(len(sp.current_user_recently_played()['items']))+'\n')
        txt.write('-------------------------------------------------------'+'\n')
        txt.write('-------------------------------------------------------'+'\n')
        for i in range(len(sp.current_user_recently_played()['items'])):    
            txt.write('artist(s): '+str(sp.current_user_recently_played()['items'][i]['track']['artists'][0]['name'])+'\n')
            txt.write('song title: '+str(sp.current_user_recently_played()['items'][i]['track']['name'])+'\n')
            txt.write('album: '+str(sp.current_user_recently_played()['items'][i]['track']['album']['name'])+'\n')
            txt.write('popularity: '+str(sp.current_user_recently_played()['items'][i]['track']['popularity'])+'\n')
            txt.write('href: '+str(sp.current_user_recently_played()['items'][i]['track']['href'])+'\n')
            txt.write('-------------------------------------------------------'+'\n')
            txt.write(str(sp.current_user_recently_played()['items'][i]['played_at'])+'\n')
            txt.write('-------------------------------------------------------'+'\n')
            txt.write(str(sp.current_user_recently_played()['items'][i]['context'])+'\n')
            txt.write('-------------------------------------------------------'+'\n')
      
    
    return None
    
    

username = 'YOUR_USERNAME'
scope_0 = 'user-library-read'
redirect_uri = "http://localhost:8888/callback/"
CLIENT_ID = 'YOUR_APP_CLIENT_ID'
CLIENT_SECRET = 'YOUR_APP_CLIENT_SECRET'

# this call is just to print the current user, can be commented or eliminated, i wrote this one just to show the difference in scope (scope_0 vs scope)
# i uploaded a txt containing the different scopes that can be used
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope_0, 
                                                client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=redirect_uri,
                                                username = username
                                                ))


print(sp.current_user())

scope = 'user-read-recently-played user-top-read user-read-playback-position'

last_50_played_songs_to_txt(username,scope,redirect_uri,CLIENT_ID,CLIENT_SECRET)

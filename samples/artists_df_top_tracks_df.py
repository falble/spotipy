import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
# only to execute the proposed example
from playlist_to_artists_df import playlist_to_artists_df

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))

def artists_df_top_tracks_df(df, country, number_of_tracks):
    """ From a df containing information of different artists, this function, suggests for every artist 
    dataframe of their top tracks according to spotify, limiting the response to one particular country.  
    
    Parameters
    ----------
    df : pd.DataFrame(containing the columns 'artist' & 'uri')
        iterable containing the uris/urls of the artists
        'spotify:artist:INSERT_HERE_SPECIFIC_URI_CODE'.
    country : str
        ex. 'US' in order to list the top tracks limiting the response to one particular country.
    number_of_tracks : int
        choose the number of top tracks to return for each artist.

    Returns
    -------
    top_tracks_df: pd.DataFrame
        DataFrame of the top tracks.

    """
    
    artist_name = []
    track_position = []
    track_name = []
    album_name = []
    col_name = ['artist','position','track','album']
    
    artist_to_analyze = df['uri']
    
    for uri in artist_to_analyze:
        for i in range(number_of_tracks):
            artist_name.append(sp.artist(uri)['name'])
            track_position.append('({})'.format(i+1))
            track_name.append(sp.artist_top_tracks(uri,country=country)['tracks'][i]['name'])
            album_name.append(sp.artist_top_tracks(uri,country=country)['tracks'][i]['album']['name'])
            
    top_tracks_df = pd.DataFrame(list(zip(artist_name, track_position, track_name, album_name)),columns=(col_name))
    top_tracks_df = top_tracks_df.drop_duplicates(subset=['track'],keep='first')
    
    
    print('<DataFrame completed>')
    print('\n---------------------------------------------------------------------------------\n')
        
    return top_tracks_df

# the adults are talking example
df = playlist_to_artists_df('https://open.spotify.com/playlist/2rQTtxMfmdrQOWHeEbStwM')
top_tracks_df = artists_df_top_tracks_df(df, 'IT', 3)

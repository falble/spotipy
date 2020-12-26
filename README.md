# spotipy
Spending definitely a lot of time on spotify, I decided to try using the API and the spotipy library.

- https://spotipy.readthedocs.io/en/2.16.1/

In order to be able to use spotipy is necessary to activate and start a project on https://developer.spotify.com/, to obtain the following info:
```python
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))
```
The repository is divided into two main folders. One contains the individual functions, the other contains small use cases. Both will be updated whenever I am bored. 
This repository is intended to be nothing more than a funny hobby. 

Here you can find a more structured repository for spotipy applications:

- https://github.com/plamere/spotipy

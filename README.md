# spotipy
Spending definitely a lot of time on spotify, I decided to try using the API and the spotipy library.

- https://spotipy.readthedocs.io/en/2.16.1/
- https://pypi.org/project/spotipy/

In order to be able to use spotipy is necessary to activate and start a project on https://developer.spotify.com/, to obtain the following info:
```python
import spotipy
# anonymous calls
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "YOUR_APP_CLIENT_ID"
CLIENT_SECRET = "YOUR_APP_CLIENT_SECRET"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                           client_secret=CLIENT_SECRET))
```
```python
# authorized calls
from spotipy.oauth2 import SpotifyOAuth

username = 'YOUR_USERNAME'
scope = 'ex. user-library-read'
redirect_uri = "ex. http://localhost:8888/callback/"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                                                client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri=redirect_uri,
                                                username = username
                                                ))

```
The repository is divided into two main folders. One contains the individual functions, the other contains small use cases.


Here you can find a more structured repository for spotipy applications:

- https://github.com/plamere/spotipy

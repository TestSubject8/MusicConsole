import sys
import spotipy
import spotipy.util as util
import secrets

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, secrets.scopes, client_id=secrets.client_id, client_secret=secrets.client_secret, redirect_uri=secrets.redirect_uri)

if token:
    try:
        sp = spotipy.Spotify(auth=token)
    #    results = sp.current_user_saved_tracks()
    #    for item in results['items']:
    #        track = item['track']
    #        print(track['name'] + ' - ' + track['artists'][0]['name'])
        results = sp.devices()
        for item in results['devices']: 
            print(item.get('name'), item.get('type'), item['id'])
        sp.transfer_playback(secrets.device)
    except Exception as e:
        print(e)
else:
    print("Can't get token for", username)

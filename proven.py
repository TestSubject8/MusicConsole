import sys
import spotipy
import spotipy.util as util
import secrets

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, secrets.scopes_all, client_id=secrets.cli_id, client_secret=secrets.cli_secret, redirect_uri=secrets.redir_uri)

if token:
    try:
        sp = spotipy.Spotify(auth=token)
    #    ============== To get all saved tracks =============================
    #    results = sp.current_user_saved_tracks()
    #    for item in results['items']:
    #        track = item['track']
    #        print(track['name'] + ' - ' + track['artists'][0]['name'])
    #    ====================================================================
    #   ============== To show all devices ( and transfer playback to stored id ) ================    
    #   +++++++++ TODO : Add menu to select device to transfer to ++++++++++++++++++++++++++++++++
    #     print("Devices: ")
    #     results = sp.devices()
    #     for item in results['devices']: 
    #         print(item.get('name'), item.get('type'), item['id'])
    #     sp.transfer_playback(secrets.dev_derputer)
    #   ==========================================================================================
    #
    #   ================= To show all saved albums ==================================================
    #     results = sp.current_user_saved_albums()['items']
    #     for al in results:
    #         print(al['album']['name'], list(artist['name'] for artist in al['album']['artists']))
    #   =============================================================================================
    #    Shows details of an album. Turns out various artists is listed on the album level
        print(sp.album('spotify:album:4FZ9s0pelFSliPWhVEWRcC')['artists'])
    except Exception as e:
        print(e)
else:
    print("Can't get token for", username)

import sys
import spotipy
import spotipy.util as util
import secrets

def debug(func):
    def debug_decor():
        func()
        return
    return debug_decor

def sp():
    token = util.prompt_for_user_token(secrets.username, secrets.scopes, client_id=secrets.cli_id, client_secret=secrets.cli_secret, redirect_uri=secrets.redir_uri)
    return spotipy.Spotify(auth=token)

@debug
def show_devices():
    dev = sp().devices()
    for d in dev['devices']:
        print(d['name'],' : ',d['volume_percent'])
    

def switch_device(dev_index):
    dev = sp().devices()
    dev_id = dev['devices'][int(dev_index)]['id']
    sp().transfer_playback(dev_id)


if __name__ == '__main__':
    option = 1
    while option != '0':
        option = input('''
        1. Show devices
        2. Play on x device
        3. Pause
                    Choice: ''')
        if option == '1':
            show_devices()
        elif option == '2':
            switch_device(input('Device index: '))
        elif option == '3':
            pass

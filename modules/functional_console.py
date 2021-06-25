import json, time
import spotipy
import spotipy.util as util
import secrets

def debug(func):
    def debug_decor():
        func()
        return
    return debug_decor

sp_driver = None

def sp():
    global sp_driver
    # add code to check for existing alive token 
    at = json.loads(open('.cache-'+secrets.username).read())
    if not sp_driver:
        print("token refreshed")
        if at['expires_at'] - int(time.time()) < 60:
            token = util.prompt_for_user_token(secrets.username, secrets.scopes, client_id=secrets.cli_id, client_secret=secrets.cli_secret, redirect_uri=secrets.redir_uri)        
        else:
            token = at['access_token']
        sp_driver = spotipy.Spotify(auth=token)
        return sp_driver
    else:
        print("token still alive")
        return sp_driver
    

# @debug
def show_devices():
    sptoken = sp()
    print(str(sptoken))
    dev = sptoken.devices()
    # index = 1
    # for d in dev['devices']:
    #     print(str(index),'. ',d['name'],' : ',d['volume_percent'])
    #     index = index + 1

    return dev

def switch_device(id):
    # dev = sp().devices()
    # dev_id = dev['devices'][int(input('Device index: '))-1]['id']
    sp().transfer_playback(id)

def get_playback():
    tk = sp()
    return tk.current_playback()

def plpause():
    tk = sp()
    info = get_playback()['is_playing']
    if info:
        tk.pause_playback()
    else:
        tk.start_playback()
    return info

def vol_change(num):
    tk = sp()
    tk.volume(num)

if __name__ == '__main__':
    option = 1

    while option != '0':
        option = input('''
        1. Show devices
        2. Play on x device
        3. Pause
                    Choice: ''')
        if option == '1':
            print(show_devices())
        elif option == '2':
            switch_device(input())
        elif option == '3':
            print(get_playback())

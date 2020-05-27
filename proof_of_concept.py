import spotipy
import spotipy.util as util
import requests,base64,json,time,shelve
import secrets

#now = int(time.time())
#if secrets.expires_at - now < 60:
#    secrets.access_token = refresh_token()

token_body = shelve.open('token_file',flag='c',writeback=True)

def refresh_token():
    global token_body
    print('Fetching token')
    url_auth = 'https://accounts.spotify.com/api/token'
    params_auth = {'grant_type': 'refresh_token', 'refresh_token': secrets.refresh_token}
    #params_auth = {'grant_type': 'refresh_token', 'refresh_token': token_body[secrets.username]['refresh_token']}
    auth_str = 'Basic ' + base64.b64encode(str(secrets.cli_id+':'+secrets.cli_secret).encode('ascii')).decode('ascii')
    heads = {"Content-type":'application/x-www-form-urlencoded', "Authorization":auth_str}
    res=requests.post(url_auth, headers=heads, data=params_auth)
    print('status:'+str(res))
    response = res.json()
    response['expires_at'] = time.time() + response['expires_in']
    token_body[secrets.username] = response
    token_body.sync()
    return response

def get_token():
    global token_body
    if token_body[secrets.username]['expires_at'] - time.time() <= 5:
        refresh_token()
    return token_body[secrets.username]['access_token'] 
        

if __name__ == '__main__':
    access_token = get_token()
    #print(access_token)
    
    auth_token = 'Bearer '+str(access_token)
    
    devices = requests.get('https://api.spotify.com/v1/me/player/devices',headers={'Authorization': 'Bearer '+str(access_token)}).json()
    
    choices = {}
    switch_choice = 0

    for dev in devices['devices']:
        print(str(switch_choice), ':', dev['name'])
        choices[switch_choice] = dev['id']
        switch_choice += 1

    switch_choice = input()
    
    dev_data = {"device_ids": [choices[int(switch_choice)]], "play": True}
    #print(json.dumps(dev_data,indent=4,sort_keys=True))
    #
    resp = requests.put('https://api.spotify.com/v1/me/player/',headers={'Authorization': auth_token, 'Content-type': 'application/json'},data=json.dumps(dev_data))
    #
    if not resp.status_code == 204:
        print(resp, resp.content)


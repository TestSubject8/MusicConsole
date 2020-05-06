import spotipy
import spotipy.util as util
import requests,base64,json,time
import secrets

#now = int(time.time())
#if secrets.expires_at - now < 60:
#    secrets.access_token = refresh_token()

def refresh_token():
    print('Fetching token')
    url_auth = 'https://accounts.spotify.com/api/token'
    params_auth = {'grant_type': 'refresh_token', 'refresh_token': secrets.refresh_token}
    auth_str = 'Basic ' + base64.b64encode(str(secrets.cli_id+':'+secrets.cli_secret).encode('ascii')).decode('ascii')
    heads = {"Content-type":'application/x-www-form-urlencoded', "Authorization":auth_str}
    res=requests.post(url_auth, headers=heads, data=params_auth)
    print('status:'+str(res))
    response = res.json()
    secrets.access_token = response['access_token']
    secrets.expires_at = response['expires_at']

access_token = secrets.access_token
#print(access_token)

auth_token = 'Bearer '+str(access_token)

#devices = requests.get('https://api.spotify.com/v1/me/player/devices',headers={'Authorization': auth_token}).json()

#for dev in devices['devices']:
#    print(dev['id'], dev['name'])

dev_data = {"device_ids": [secrets.dev_derputer], "play": True}
print(json.dumps(dev_data,indent=4,sort_keys=True))

resp = requests.put('https://api.spotify.com/v1/me/player/',headers={'Authorization': auth_token, 'Content-type': 'application/json'},data=json.dumps(dev_data))

print(resp, resp.content)

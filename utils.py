import requests
import base64

def API_GET(id: str):
    '''
    id: item id as string

    convert the id into base64 as the authentication,
    then make the request through the GET request.
    Return the payload if status code is 200.
    '''
    auth = base64.b64encode(id.encode('ascii')).decode('ascii')
    headers = {'authorization': auth}
    response = requests.get("https://eluv.io/items/id", headers=headers)
    if response.status_code == 200:
        return True, response.content
    else:
        return False, response.status_code
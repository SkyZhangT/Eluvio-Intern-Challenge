import requests
import base64

def API_GET(id: str):
    '''
    id: item id as string

    convert the id into base64 as the authentication,
    then make the request through the GET request.
    Return the payload if status code is 200.
    '''
    print("New thread started")
    auth = base64.b64encode(id.encode('ascii')).decode('ascii')
    headers = {'Authorization': auth}
    response = requests.get("https://eluv.io/items/" + id, headers=headers)
    response.close()

    if response.status_code == 200:
        return response.content
    else:
        return response.status_code

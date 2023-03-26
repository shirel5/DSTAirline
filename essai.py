import requests
import json

request = ('https://api.lufthansa.com/v1/operations/customerflightinformation/route/FRA/JFK/2023-03-26')
my_headers = {'Authorization' : 'Bearer zebxdrzh2p5fryfkchpbdkcb'}


r = requests.get(request, headers=my_headers)
if (r.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (r.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests
data = r.text
parse_json = json.loads(data)
print(parse_json)


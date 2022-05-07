import requests

ngrok_url = "https://661a-2a00-23c6-8902-5701-8d85-bd-88ef-2212.eu.ngrok.io"
endpoint = f"{ngrok_url}/box-office-mojo-scrapper"

r = requests.post(endpoint, json={})

print(r.json()["data"])

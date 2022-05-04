import requests
import pprint
import pandas as pd

api_key = "5e2ed25a11513df33bbd3c034cb866c6"
api_key_v4 = "<eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZTJlZDI1YTExNTEzZGYzM2JiZDNjMDM0Y2I4NjZjNiIsInN1YiI6IjYyNzIxOTAyY2FhY2EyMDA1MGE0MDlkNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.w1-8tA-YVc41t7v0NTx797S7Jq9a3RfO-MogIQ7fwQM>"
# HTTP request METHODS
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

# what's our endpoint (or a url)?

# what is the HTTP method that we need?


"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=075937068a3817fa489588e754320646
"""
movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&page=1"
print(endpoint)
# r = requests.get(endpoint) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)


# Using v4
movie_id = 501
api_version = 4
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}"
headers = {
    "Authorization": f"Bearer {api_key_v4}",
    "Content-Type": "application/json;charset=utf-8",
}
# r = requests.get(endpoint, headers=headers) # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)


api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
searh_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={searh_query}"
# print(endpoint)
r = requests.get(endpoint)
# pprint.pprint(r.json())
if r.status_code in range(200, 299):
    data = r.json()
    results = data["results"]
    if len(results) > 0:
        # print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result["id"]
            # print(result['title'], _id)
            movie_ids.add(_id)
        # print(list(movie_ids))
output = "movies.csv"
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)


df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)

print(len(res.text))
print(res.text[:500])

res.raise_for_status()
# badRes = requests.get('https://automatetheboringstuff.com/sacnalkcjac;as,xc')
# badRes.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

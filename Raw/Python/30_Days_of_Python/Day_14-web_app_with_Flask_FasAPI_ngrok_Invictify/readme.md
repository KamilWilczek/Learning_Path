# Usefull commands
- python -m http.server
http://localhost:8000
http://127.0.0.1:8000

- python -m pip install pipenv
    - pipenv shell --python 3.8

# On windows instead gunicorn in powershell
- """set FLASK_APP=server1.py
$env:FLASK_APP = "server1.py"
flask run"""uvi
then: 'python3 -m flask run'
- use waitress
- change your interpreter and use flask run command in place of gunicorn server-flask:app
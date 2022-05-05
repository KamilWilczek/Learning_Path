# Windows only
# gunicorn flask_server:app - not working on windows
# gunicorn flask_server:app --bind 127.0.0.1:8888
# flask run
flask run -h localhost -p 8888
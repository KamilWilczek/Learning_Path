from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world():
    return {"hello": "world"}


@app.get("/abc")
def abc_view():
    return {"data": [1, 2, 3]}

from fastapi import FastAPI


app = FastAPI()
#-- To start the local server => uvicorn main:app --reload

@app.get('/')
def index():
    return {'data': {"name": "Byom"}}

@app.get('/about')
def about():
    return {'data': "About Page"}

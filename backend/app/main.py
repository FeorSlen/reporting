from fastapi import FastAPI
from reporting.create_report import create_report
from config import DEBUG

app = FastAPI(debug=DEBUG)

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/api/")
def api_url():
    return create_report() # url, config

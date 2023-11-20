from fastapi import FastAPI
from starlette import status

app = FastAPI()

@app.get("/api/v1/hello-world-16", status_code=status.HTTP_200_OK)
def hello_world():
    return {"message": "Hello World 16"}

import uvicorn
from fastapi import FastAPI
from core.config import settings


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/")
def hello_api():
    return {'detail': 'Hello world!'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.SERVER_PORT)

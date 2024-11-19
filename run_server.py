import uvicorn

from api.app import app

uvicorn.Config(app=app, proxy_headers=True)


if __name__ == "__main__":
    uvicorn.run(app=app, port=8000, host="localhost", proxy_headers=True)
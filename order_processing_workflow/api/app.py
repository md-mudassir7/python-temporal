import routers
from fastapi import FastAPI

def main_app():
    app = FastAPI()

    app.include_router(routers.router)

    return app
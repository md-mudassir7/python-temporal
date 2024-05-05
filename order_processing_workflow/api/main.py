import uvicorn
from api.app import main_app

def main():
    """
    This function creates fastapi object,
    loads settings, adds api routers and certificate configuration
    """
    app = main_app()

    uvicorn.run(app, host="localhost", port="8000")


if __name__ == "__main__":
    main()
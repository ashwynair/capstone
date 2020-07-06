from app import create_app
from dotenv import load_dotenv

APP = create_app()
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)

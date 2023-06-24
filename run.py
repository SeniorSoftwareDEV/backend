from api.config import app
from api import auth, match, mttools

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

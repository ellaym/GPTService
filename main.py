# main.py
from app import create_app
from app.routes import main
from os import getenv

app, client = create_app()

# Pass the client to the route
main.client = client

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getenv('FLASK_PORT', 5500), debug=True)

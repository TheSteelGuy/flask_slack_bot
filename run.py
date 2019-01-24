import os
from src import create_app


app = create_app(os.getenv('APP_ENV'))

if __name__ == '__main__':
    app.run()

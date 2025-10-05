from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/')
def hello():
    return "Algorithmic Trading Backend"

if __name__ == '__main__':
    app.run(debug=True)

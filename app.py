from app import app
# from flask import Flask
import os

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return 'hello word'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True, use_reloader=True)
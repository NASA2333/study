# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run()

import requests
r= requests.get('http://127.0.0.1:5000/api/users')
print(r.text)
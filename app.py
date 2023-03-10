from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/test_function")
def test():
    a=5+6
    return"This is my first function in the flask {}".format(a)

@app.route("/request")
def request_input():
   data= request.args.get('x')
   return "This is my input from the url {}".format(data)
# https://red-pharmacist-cfifj.pwskills.app:5000/request?x=567

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World!1"

@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"


if __name__=="__main__":
    app.run(host="0.0.0.0")

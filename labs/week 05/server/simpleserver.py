# simple app server with flask that serves hello world

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
 return "Hello, World!"
if __name__ == '__main__' :
 app.run(debug=True)

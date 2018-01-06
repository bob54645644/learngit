from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app </span>"
@app.route('/user/<name>')
def user(name):
	return "hello,%s!"%name
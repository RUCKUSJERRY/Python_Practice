# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_root():
    return '<h1><a href="/test/admin">test</a></h1>'

@app.route('/test/<id>')
def hello_flask(id):
    return '<h1>Hello, ' + id + "</h1>"

if __name__ == '__main__':
    app.run()
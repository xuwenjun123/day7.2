from flask import Flask

from flask import request

from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/<method>/<int:a>/<int:b>')
def count(method,a,b):
    if method == 'add':
        c = a + b
    elif method == 'sub':
        c = a - b
    elif method == 'mul':
        c = a * b
    elif method == 'div':
        c = a / b
    else:
        c = 'unknow'
    return f'result = {c}' 

@app.route('/count')
def count2():
    method = request.args.get('method','')
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))

    if method == 'add':
        c = a + b
    elif method == 'sub':
        c = a - b
    elif method == 'mul':
        c = a * b
    elif method == 'div':
        c = a / b
    else:
        c = 'unknow'
    return f'result = {c}' 

@app.route('/count3', methods=('POST',))
def count3(): 
    method = request.form.get('method','')
    a = int(request.form.get('a', 1))
    b = int(request.form.get('b', 1))

    if method == 'add':
        c = a + b
    elif method == 'sub':
        c = a - b
    elif method == 'mul':
        c = a * b
    elif method == 'div':
        c = a / b
    else:
        c = 'unknow'
    return f'result = {c}'


@app.route('/render')
def render():
    return render_template('test.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

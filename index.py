#MorseLaw Search engin
from flask import Flask, escape, request, render_template

app=Flask(__name__)

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)
    # name = request.args.get("name", "World")
    # return f'Hello, {escape(name)}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
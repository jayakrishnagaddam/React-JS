from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def function():
    return render_template('login.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

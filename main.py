from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running!"

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return str(a + b)
    except:
        return "Error", 400

if __name__ == '__main__':
    app.run()

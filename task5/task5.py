from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def me():
    return "This is the about page"


@app.route('/goodbye')
def me():
    return "Goodbye see you soon!!!"

if __name__ == '__main__':
    app.run(debug=True)


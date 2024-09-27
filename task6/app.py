from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    name = "Huzaifa"
   
    return render_template('index.html',name=name)

@app.route('/fruit')

def homi():
    fruit = ['Apple','Bannana','Cherry']
    return render_template('app.html',fruits=fruit)

@app.route('/age')
def age():
    age = int(input("enter your age"))
    return render_template('age.html',age=age)

if __name__ == '__main__':
    app.run(debug=True)

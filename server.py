
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def chkbrd():
    return render_template('index.html', num1 = 8, num2 = 8, color_a = 'red', color_b = 'black')

@app.route('/<int:num1>')
def choose_num(num1):
    return render_template('index.html', num1 = num1, num2 = 8, color_a = 'red', color_b = 'black')

@app.route('/<int:num1>/<int:num2>/<string:color_a>/<string:color_b>')
def choose_all(num1, num2, color_a, color_b):
    return render_template('index.html', num1 = num1, num2 = num2, color_a = color_a, color_b = color_b)

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
from flask import Flask,request, url_for, redirect, render_template
import pickle

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("Assign.html")


if __name__ == '__main__':
    app.run(debug=True)








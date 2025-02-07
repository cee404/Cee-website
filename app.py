import os, 
from flask import Flask, render_template, redirect, url_for, 

app = Flask(__name__)

@app.route('/')
def home():
    # Debug line to check the template folder path
    print("Template folder path:", os.path.join(os.getcwd(), "Templates"))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

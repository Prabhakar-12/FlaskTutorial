
#importing the Flask class from flask module
from flask import Flask,render_template
#Creating the Flask Application
app=Flask(__name__)
#Defining the Route URL path
@app.route('/')
def home():
    return render_template('index.html')
#Another Route
@app.route('/about')
def about():
    return render_template('about.html')
#Another Route
@app.route('/sample')
def sample():
    return render_template('sample.html')
#Run the app
if __name__=="__main__":
    app.run()

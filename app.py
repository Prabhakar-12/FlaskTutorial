# import datetime
#
# #importing the Flask class from flask module
# from flask import Flask,render_template
# import datetime
# #Creating the Flask Application
# app=Flask(__name__)
# #Defining the Route URL path
# @app.route('/')
# def home():
#     return render_template('index.html')
# #Another Route
# @app.route('/about')
# def about():
#     return render_template('about.html')
# #Another Route
# @app.route('/sample')
# def sample():
#     return render_template('sample.html')
# #Run the app
# if __name__=="__main__":
#     app.run()
#importing the Flask class from flask module
from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('index.html')
@app.route('/about')
def About():
    return render_template('about.html')
@app.route('/sample')
def Sample():
    return render_template('sample.html')
if __name__=="__main__":
    app.run()
# from flask import Flask,render_template
# app=Flask(__name__)
# @app.route('/')
# def Home():
#     return render_template('a.html')
# @app.route('/about')
# def about():
#     return render_template('b.html')
# if __name__=="__main__":
#     app.run()
from flask import  Flask,render_template
app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('a.html')

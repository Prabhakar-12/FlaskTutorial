from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"
@app.route('/about')
def Hi():
    return "This is Prabhakar"
if __name__=="__main__":
    app.run(debug=True)
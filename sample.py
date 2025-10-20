from flask import Flask,render_template,request,redirect,url_for
App=Flask(__name__)
@App.route('/')
def Home():
    return render_template('a.html')
@App.route('/about')
@App.route('/submit_form',methods=['POST'])
def submit_form():
    if request.method=='POST':
        FirstName=request.form['name']
        LastName=request.form['name']
        return f'Firstname:{FirstName} and LastName:{LastName}'

    return redirect(url_for('about'))
def About():
    return render_template('b.html')
if __name__=="__main__":
    App.run()
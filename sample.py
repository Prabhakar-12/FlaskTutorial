from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def Home():
    return render_template('a.html')
@app.route('/about')
def About():
    items=[
        {'id':1,'name':'phone','barcode':'76355363536','price':500},
        {'id':2,'name':'Laptop','barcode':'2976378633','price':300},
        {'id':3,'name':'keyboard','barcode':'37635763','price':600}
    ]
    return render_template('b.html',items=items)
if __name__=="__main__":
    app.run()
from flask import Flask,render_template,request,redirect
from database import check,create
from func import recm,details
import joblib as jb
import numpy as np

# Model import code
model = jb.load('res/BookModel')
b_name = jb.load('res/BookName')
feature = jb.load('res/BookFeature')




app = Flask(__name__)

#Model page and code
@app.route('/model',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form["search"]
        num = int(request.form['no']) + 1
        r_name, r_link = recm(name, num, b_name, model,feature)
        return render_template("recm.html",name=r_name,link=r_link,r=len(r_name))
    return render_template("model.html",names=np.sort(b_name['NAME OF THE BOOK']))

@app.route('/',methods=['GET','POST'])
def sing():
    if request.method == 'POST':
        mb = request.form['mobile']
        pas = request.form['password']
        msg = check(mb,pas)
        if msg == 1:
            return redirect('/model')
        return render_template('log.html',msg=msg)
    return render_template("log.html")

@app.route('/signup',methods=['GET','POST'])
def sigup():
    if request.method == 'POST':
        mb = request.form['mobile']
        name = request.form['name']
        pas = request.form['password']
        msg = create(name,mb,pas)
        return render_template('create.html',msg=msg)
    return render_template('create.html')

@app.route('/product/<name>')
def product(name):
    detail = details(name, b_name)
    li_name, li_link = recm(name, 6, b_name, model,feature)
    return render_template('product.html', detl = detail, rec = [li_name,li_link,len(li_name)])

@app.route('/author')
def author():
    return render_template('author.html',names = np.sort(np.unique(b_name['NAME OF THE AUTHOR'])))

@app.route('/author/<name>')
def author_name(name):
    li = np.where(b_name['NAME OF THE AUTHOR'] == name)[0]
    return render_template('author_book.html',name = np.array(b_name.iloc[:,2:4]),ind = li,au = name)


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=5000)

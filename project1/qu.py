from flask import Flask, render_template, url_for, request, session, redirect
import requests
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import json
from plotly.offline import plot
from plotly.graph_objs import Scatter
app=Flask(__name__)
bcrypt = Bcrypt(app)
app.config['MONGO_DBNAME'] = 'quiz'
app.config['MONGO_URI'] = 'mongodb://ad:a123456@ds115543.mlab.com:15543/quiz'
mongo = PyMongo(app)
ca1=[]
ga1=[]
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['pass']).decode('utf-8')
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('cat'))
        
        return 'That username already exists!'
    return render_template('home.html')
@app.route('/login', methods=['GET','POST'])
def ito():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        pw_hash = login_user.password
        comfirm = bcrypt.check_password_hash(pw_hash, request.form['pass'])

        if comfirm == True:
            session['username'] = request.form['username']
            return redirect(url_for('cat'))

        # if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
        #     session['username'] = request.form['username']
        #     return redirect(url_for('cat'))

    return 'Invalid username/password combination'
@app.route('/categories',methods=['GET','POST'])
def cat():
    response=requests.get("https://opentdb.com/api_category.php",params=None)
    res=response.json()
    p=[]
    for i in range(0,len(res['trivia_categories'])):
        p.append(res['trivia_categories'][i]['name'])
    s='\n'.join(map(str,p))
    return render_template('cat.html',c=p) 
@app.route('/quiz01/<i>')
def quiz1(i):
    global ca1
    q=[]
    ca=[]
    wa=[]
    i=int(i)
    j=i+9
    k=str(j)
    #ca1.clear()
    #ga1.clear()
#list={'id':20}
    parameters={'category':k,'amount':10}
    response=requests.get("https://opentdb.com/api.php",params=parameters)
    res=response.json()
    for l in range(0,len(res['results'])):
        #print(res['results'][i]['question'])
        q.append(res['results'][l]['question'])
        ca.append(res['results'][l]['correct_answer'])
        wa.append(res['results'][l]['incorrect_answers'])
    os=[]
    for t in range(10):
        os.append([ca[t]])
        for k in range(3):
            os[t].append(wa[t][k])
    ca1=ca
    return render_template('quiz.html',sp=q,ot=os)

@app.route('/result',methods=['POST'])
def result():
    global ga1,ca1
    count=0
    ne=[]
    for i in range(10):
        ga1.append(request.form[str(i)])
        if request.form[str(i)]==ca1[i]:
            count=count+1
            ne.append(1)
        else:
            ne.append(0)
    ca1.clear()
    msg = ''
    if count<3:
        msg= "Poor Results"
    elif count>8:
        msg= "Excellent Results"
    else:
        msg = "NICE ONE"
    p = plot([Scatter(x=[1,2,3,4,5,6,7,8,9,10], y=ne )],output_type="div")
    return render_template('result.html',count=count,given=ga1,correct=ca1,msg=msg,div_placeholder=Markup(p))
if __name__=='__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
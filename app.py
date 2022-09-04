from flask import Flask, request, url_for, redirect, render_template
import numpy as np
import pickle
from flask_mysqldb import MySQL

app = Flask(__name__)

model = pickle.load(
    open('D:\Programs\Data_Hack_2022_Placement_Predictor\model.pkl', 'rb'))
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student_database'
mysql = MySQL(app)


def myFunc(val, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(val - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/form.html', methods=['POST', 'GET'])
def form():
    return render_template("form.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    msg = ''
    if request.method=='POST':
        cursor = mysql.connection.cursor()
        fname = request.form['fname']
        lname = request.form['lname']
        user = request.form['username']
        age = request.form['age']
        edu = request.form['eduQualification']
        mail = request.form['email']
        country = request.form['country']
        phone = request.form['phone']
        url = request.form['website']
        address = request.form['address']
        stream = request.form['stream']
        year = request.form['graduationYear']
        college = request.form['college']
        cgpa = request.form['cgpa']
        nonacdem = request.form['nonacadem']
        backlogs = request.form['backlogs']
        techlevel = request.form['techSkill']
        projects = request.form['projects']
        easyno = request.form['easyProjects']
        mediumno = request.form['mediumProjects']
        expertno = request.form['expertProjects']
        problemsolving = request.form['problemSolving']
        internships = request.form['internships']
        winner = request.form['winner']
        runner = request.form['runner']
        participant = request.form['participant']
        comm = request.form['comSkill']
        personality = request.form['personality']
        resume = request.form['resume']
        cursor.execute('insert into students values(1, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(fname,lname,user,age,edu,mail,country,phone,url,address))
        cursor.execute('insert into education values(1, %s, %s, %s, %s, %s, %s)',
                       (stream,year,college,cgpa,nonacdem,backlogs))
        cursor.execute('insert into techskills values(1, %s,%s,%s,%s,%s,%s)',(techlevel,projects,easyno,mediumno,expertno,problemsolving))
        cursor.execute('insert into workexp values(1, %s,%s,%s,%s)',
                       (internships,winner,runner,participant))
        cursor.execute('insert into comskills values(1, %s,%s,%s)',
                       (comm,personality,resume))
    intern = cursor.execute('select internships from workexp where studentID=1')
    cgp = cursor.execute('select cgpa from education where studentID=1')
    history = cursor.execute(
        'select backlogs from education where studentID=1')
    team = cursor.execute('select commlevel from comskills where studentID=1')
    prob = cursor.execute('select problemsolving from techskills where studentID=1')
    tec = cursor.execute('select techLevel from techskills where studentID=1')
    com = cursor.execute('select commlevel from comskills where studentID=1')
    res = cursor.execute('select resumelevel from comskills where studentID=1')
    eas = cursor.execute('select easyno from techskills where studentID=1')
    med = cursor.execute('select mediumno from techskills where studentID=1')
    har = cursor.execute('select expertno from techskills where studentID=1')
    adv = cursor.execute('select expertno from techskills where studentID=1')
    per = cursor.execute('select personality from comskills where studentID=1')
    win = cursor.execute('select winner from workexp where studentID=1')
    run = cursor.execute('select runner from workexp where studentID=1')
    par = cursor.execute('select participant from workexp where studentID=1')
    features = [int(internships),float(cgpa),int(backlogs),int(comm),int(problemsolving),int(techlevel),int(comm),int(resume),int(easyno),int(mediumno),int(expertno),int(expertno),int(personality),int(winner),int(runner),int(participant)]
    value = [np.array(features)]
    val = model.predict(value)
    for x in val:
        val = x
    out2 = myFunc(val/100, 0, 1, 0, 20)
    return render_template('index.html',result1=str(val),result2=str(round(out2,2)),result3=str(out2))

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
'''



from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import json
import os
 
app = Flask(__name__)
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/template')
app = Flask(__name__, template_folder=template_path)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'barber'
 
mysql = MySQL(app)
 
@app.route('/create-user')
def createUser1():
    if request.method == 'GET':
        pwd = request.args.get('pwd')
        ipAddr = request.args.get('ip')
        ipAddr = str(ipAddr)
        pwd = str(pwd)
        query = "INSERT INTO users values('','+" + ipAddr + "','"+ pwd + "')"
        print(query)
        cursor = mysql.connection.cursor()
        r = cursor.execute(query)
        print(r)
        mysql.connection.commit()
        cursor.close()
    
    return render_template('<p>Done</p>')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        #return "Login via the login Form"
        print('Hello')
     
    if request.method == 'GET':
        #name = request.form['name']
        ipAddr = request.args.get('ip')
        ipAddr = str(ipAddr)
        query = "SELECT * from users where ipaddr=" +"'"+ ipAddr+"'"
        #print(ipAddr)
        cursor = mysql.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        #print(row)
        data = {}
        for i in row:
            data['ipaddr'] = i[1]
            data['pwd'] = i[2]
            print(i[2])
        mysql.connection.commit()
        cursor.close()
        rows = json.dumps(row)
        print(type(rows))
        '''print(rows[0])
        data = {}
        data['ipaddr'] = rows[0][1]
        data['pwd'] = rows[0][2]
        data = json.loads(data)
        print((data))'''
        return data
 
#app.run(host='localhost', port=5000)
app.run(host='0.0.0.0', port=105)

import os
import mysql.connector
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

USER = os.getenv('MYSQL_USER')
PASSWORD = os.environ.get('MYSQL_PASSWORD')
HOST = os.environ.get('MYSQL_HOST')
DATABASE = os.getenv('MYSQL_DATABASE')

try:
    mydb = mysql.connector.connect(
    host=str(HOST),
    user=str(USER),
    passwd=str(PASSWORD),
    db = str(DATABASE),
    ssl_disabled = True
    )
    mycursor = mydb.cursor()
    print("Database successfully connected")
except Exception as e:
    print("could not connect to Database")
    print(str(e))

@app.route('/')
def home():
    response = 'Welcome to getCustomerList version 1'
    return response

@app.route('/customers',methods=['GET'])
def getCustomerList():
    sql = "select id, customerName from customer ORDER BY customerName, id"
    try:
        mycursor.execute(sql)
        columns = mycursor.column_names
        myresult = mycursor.fetchall()
        json_data=[]
        for result in myresult:
            json_data.append(dict(zip(columns,result)))

        print(json_data)
        response = jsonify(json_data)
        print("response: ")
        print(response)
        return response
    except Exception as e:
        return "Could not retrieve records from DB: " + str(e)


    



app.run("0.0.0.0","8080")

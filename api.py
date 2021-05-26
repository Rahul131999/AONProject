
from flask import Flask,render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import sqlite3
app = Flask(__name__)
import json
# get this object
from flask import Response
# change to name of your database; add path if necessary
db_name = 'sockmarket.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
conn = sqlite3.connect('database.db')
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

	
@app.route('/')
def testdb():
   
   

	conn = sqlite3.connect('database.db')
	print("Opened database successfully")
	conn.execute('DROP TABLE user')
	
	conn.execute('CREATE TABLE user (userId number, recipientId number, transactionId number,transactionDir string, transactionDate date, expiryDate date, amount number, description TEXT, status string,type string,direction text)')
	print("Table created successfully")
	conn.execute('INSERT INTO user VALUES(1,2,123456,"Received","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,2,123456,"Received","2004-02-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,2,123456,"SENT","2004-02-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,2,123456,"SENT","2005-05-25","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,2,123456,"SENT","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(2,3,123456,"SENT","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,3,123456,"SENT","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(3,1,123456,"SENT","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(3,2,123456,"Received","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	conn.execute('INSERT INTO user VALUES(1,4,123456,"Received","2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","Request","RIGHT")')
	print("registered")  
	print("here we are: " )
	print(request.args.get("userId"))  
	print("here we are : " + request.args.get("recipientId"))   
	query = "SELECT transactionId,transactionDate,expiryDate,type,amount,transactionDir,userId  from user where userId = "+ request.args.get("userId") + " AND recipientId=" + request.args.get("recipientId") + " ORDER BY transactionDate"
	socks = conn.execute(query).fetchall()
	print(socks)
	print("done")
	conn.close()
	try:
	    db.session.query(text('1')).from_statement(text('SELECT 1')).all()
	    return render_template('result.html', data=socks)
	except Exception as e:
	    error_text = "<p>The error:<br>" + str(e) + "</p>"
	    hed = '<h1>Something is broken.</h1>'
	    return hed + error_text
        

if __name__ == '__main__':
    app.run(debug=True)
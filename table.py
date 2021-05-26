import sqlite3

import enum



conn = sqlite3.connect('database.db')
print("Opened database successfully")
conn.execute('DROP TABLE user')
conn.execute('CREATE TABLE user (userId number, recipientId number, transactionId number, transactionDate date, expiryDate date, amount number, description TEXT, status string,type string,direction text)')
print("Table created successfully")
conn.execute('INSERT INTO user VALUES(1,2,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
conn.execute('INSERT INTO user VALUES(2,3,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
conn.execute('INSERT INTO user VALUES(1,3,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
conn.execute('INSERT INTO user VALUES(3,1,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
conn.execute('INSERT INTO user VALUES(3,2,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
conn.execute('INSERT INTO user VALUES(1,4,123456,"2004-01-22","2004-01-22",100,"lets pay", "CONFIRMED","PAY","RIGHT")')
print("registered")       
socks = conn.execute("SELECT * from user").fetchall()
print(socks)
print("done")
conn.close()
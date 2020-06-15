import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__) 

app.config["DEBUG"] = True


@app.route('/api/v2/employee',methods=['GET'])
def get_all():
	sql = '''select * from Employees'''
	res = db_connection(sql)
	return jsonify({'Details': res})

@app.route('/api/v2/employee',methods=['POST'])
def post():
	if not request.json and 'fname' not in request.json:
		abort(404)
	fname = request.json.get('fname', '')
	lname = request.json.get('lname', '')
	db_connection("INSERT INTO 'Employees'('fname','lname') VALUES (?,?)",(fname,lname))
	return jsonify({'Message': 'Data added successfully.'})

@app.route('/api/v2/employee/<int:idn>',methods=['PUT'])
def put(idn):
	if not request.json and 'fname' not in request.json:
		abort(404)
	fname = request.json.get('fname', '')
	lname = request.json.get('lname', '')
	sql = ''' UPDATE Employees
              SET fname = ? ,
                  lname = ? 
              WHERE id = ?'''
	db_connection(sql, (fname,lname,int(idn)))
	return jsonify({'Message': 'Data updated successfully.'})

@app.route('/api/v2/employee/<int:idn>',methods=['DELETE'])
def delete(idn):
	sql = ''' DELETE FROM Employees
              WHERE id = ?'''
	db_connection(sql, (int(idn),))
	return jsonify({'Message': 'Data deleted successfully.'})

def db_connection(sql, para=()):
	con = sqlite3.connect("employee.db")
	cur = con.cursor()
	cur.execute(sql,para)
	res = cur.fetchall()
	con.commit()
	return res

app.run()

# curl GET http://localhost:5000/api/v2/employee
# curl -i -H "Content-Type: application/json" -X POST -d "{\"fname\":\"book1\"}" http://localhost:5000/api/v2/employee
# curl -i -H "Content-Type: application/json" -X PUT -d "{\"fname\":\"book2\"}" http://localhost:5000/api/v2/employee/2
# curl -iX DELETE http://localhost:5000/api/v2/employee/3

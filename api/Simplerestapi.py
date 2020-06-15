import sqlite3
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__) 

app.config["DEBUG"] = True

tasks=[
	{
		'id' : 1,
		'name' : 'file1',
		'platform' : 'Linux1',
		'date' : '01/01/2011'

	}
]

@app.route('/api/v1/tasks')
def get_all():
	return jsonify({'tasks': tasks})

@app.route('/api/v1/tasks/<int:task_id>',methods=['GET'])
def get(task_id):
	task = [task for task in tasks if task['id'] == task_id]
	if not task:
		abort(404)
	else:
		return jsonify({'tasks': task})

@app.route('/api/v1/tasks',methods=['POST'])
def post():
	if not request.json and 'name' not in request.json:
		abort(404)
	task = {
		'id':tasks[-1]['id']+1,
		'name':request.json.get('name', ''),
		'platform': request.json.get('platform',''),
		'date': request.json.get('date','')
	}
	tasks.append(task)
	return jsonify({'tasks': task}),201

@app.route('/api/v1/tasks/<int:task_id>',methods=['PUT'])
def put(task_id):
	if not request.json and 'name' not in request.json:
		abort(404)
	task = [task for task in tasks if task['id'] == int(task_id)]
	if not task:
		abort(404)
	task[0]['name'] = request.json.get('name', task[0]['name'])
	task[0]['platform'] = request.json.get('platform', task[0]['platform'])
	task[0]['date'] = request.json.get('date', task[0]['date'])
	return jsonify({'task':task[0]})

@app.route('/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    task = [task for task in tasks if task['id'] == int(task_id)]
    if not task:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'response':'error'})



app.run()

# curl GET http://localhost:5000/api/v1/tasks
# curl -i -H "Content-Type: application/json" -X POST -d "{\"name\":\"book1\"}" http://localhost:5000/api/v1/tasks
# curl -i -H "Content-Type: application/json" -X PUT -d "{\"name\":\"book2\"}" http://localhost:5000/api/v1/tasks/2
# curl -iX DELETE http://localhost:5000/api/v1/tasks/3

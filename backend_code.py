
from flask import Flask,request,jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks",methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks",methods=["POST"])
def add_task():
    data = request.json
    task = {
        "id":len(tasks)+1,
        "task":data["task"],
        "status":"pending"
    }
    tasks.append(task)
    return jsonify(task)

app.run(host="0.0.0.0",port=5000)
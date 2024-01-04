from flask import Flask
import subprocess
import json

app = Flask(__name__)

@app.route("/service/latency_check", methods=['GET'])
def latency_check_status():
    result = subprocess.run(["systemctl", "status", "--user", "latency_check.service"], capture_output=True)
    if result.returncode != 0 and result.returncode != 3:
        obj = { "success": False, "message": result.stderr.decode("utf-8", "ignore") }
    else: 
        obj = { "success": True, "message": result.stdout.decode("utf-8", "ignore") }
    return json.dumps(obj, indent=4)


@app.route("/service/latency_check/start", methods=['GET'])
def latency_check_start():
    result = subprocess.run(["systemctl", "start", "--user", "latency_check.service"], capture_output=True)
    if result.returncode != 0:
        obj = { "success": False, "message": result.stderr.decode("utf-8", "ignore") }
    else: 
        obj = { "success": True, "message": result.stdout.decode("utf-8", "ignore") }
    return json.dumps(obj, indent=4)


@app.route("/service/latency_check/stop", methods=['GET'])
def latency_check_stop():
    result = subprocess.run(["systemctl", "stop", "--user", "latency_check.service"], capture_output=True)
    if result.returncode != 0:
        obj = { "success": False, "message": result.stderr.decode("utf-8", "ignore") }
    else: 
        obj = { "success": True, "message": result.stdout.decode("utf-8", "ignore") }
    return json.dumps(obj, indent=4)

from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/service/latency_check", methods=['GET'])
def latency_check_status():
    # result = subprocess.run(["systemctl", "status", "--user", "latency_check.service"], capture_output=True)
    result = subprocess.run(["ls", "-l", "/Users/martindubb/Desktop/playground/wiederholung/myproject"], capture_output=True)
    if result.returncode != 0 and result.returncode != 3:
        return '{ "success": false, "reason": "' + result.stderr.decode("utf-8") + '" }'
    return '{ "success": true, "stdout": "' + result.stdout.decode("utf-8") + '" }'


from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print("Received data:", data)  # <-- Add this line for debugging
    if data and "alerts" in data:
        for alert in data["alerts"]:
            if alert["labels"].get("alertname") == "NginxDown":
                print("NGINX is down! Running Ansible playbook...")
                subprocess.run(["ansible-playbook", "/root/restart_nginx.yml"])
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


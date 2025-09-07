Project_2_Self-Healing_Infrastructure-with_Prometheus_Alertmanager_-_Ansible

Introduction
This project demonstrates a **self-healing infrastructure** where system failures are detected and automatically fixed without manual intervention.  
It integrates **Prometheus Alertmanager**, a **Flask-based Webhook receiver**, and **Ansible** to restart services (like NGINX) whenever downtime is detected.

---

Features
- Automatic failure detection via **Prometheus Alertmanager**.
- Webhook receiver built with **Flask**.
- Automatic **NGINX restart** using **Ansible**.
- Extensible for other services (MySQL, Apache, custom apps).

---

Tools & Technologies Used
- **Prometheus Alertmanager** – to generate alerts.  
- **Flask (Python)** – to receive webhooks and trigger actions.  
- **Ansible** – to restart/repair failed services.  
- **NGINX** – as the monitored web service.

- 
Installation & Setup

Clone Repository
git clone https://github.com/your-username/self-healing-infra.git
cd self-healing-infra

2. Install Dependencies
cd webhook
pip install -r requirements.txt

4. Start Webhook Service
sudo python3 webhook.py

5. Configure Alertmanager
Update alertmanager/alertmanager.yml with webhook receiver:

yaml
Copy code
receivers:
  - name: 'webhook-receiver'
    webhook_configs:
      - url: 'http://127.0.0.1:5001/alert'
Then restart Alertmanager.

5. Trigger Test Alert
Send a manual alert to webhook:


curl -X POST -H "Content-Type: application/json" \
-d '{"alerts":[{"labels":{"alertname":"NginxDown"}}]}' \
http://127.0.0.1:5001/alert
✅ Expected Output
Alert received by webhook.

Webhook triggers Ansible playbook.

NGINX service automatically restarts.

Logs printed in terminal confirming recovery.

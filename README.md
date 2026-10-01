# 🛡️ Log Intelligence

### Intelligent Log Analysis & Security Monitoring Platform

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20App-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Regex-Log%20Parsing-4B8BBE?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Loguru-Logging-FF6B35?style=for-the-badge" />
</p>

<p align="center">
  <b>Turn thousands of raw log lines into meaningful security intelligence.</b>
</p>

---

## 🚀 Overview

**Log Intelligence** is a professional log-analysis and security-monitoring platform built with **Python, Flask, Pandas, Regex, and Loguru**.

Instead of manually reading hundreds or thousands of log lines, the system automatically:

* 📊 Parses structured and semi-structured logs
* 🔍 Extracts important security information
* 🚨 Detects suspicious activity
* 🌐 Identifies repeated activity from IP addresses
* 🔐 Detects possible brute-force authentication attempts
* ⚠️ Identifies critical and high-risk events
* 🧠 Finds security-related keywords
* 📈 Generates real-time statistics
* 🔎 Provides event search and filtering
* 📄 Exports analyzed data as CSV

The project is designed as a foundation for a future **AI-powered SOC / SIEM-style security platform**.

---

# ✨ Key Features

| Feature                  | Description                                                 |
| ------------------------ | ----------------------------------------------------------- |
| 📂 Log Upload            | Upload your own `.log` / `.txt` files                       |
| 🧩 Log Parsing           | Extract timestamp, level, IP, user and message              |
| 📊 Analytics             | Analyze event frequency and severity                        |
| 🚨 Anomaly Detection     | Identify suspicious patterns                                |
| 🔐 Brute-Force Detection | Detect repeated authentication failures                     |
| 🌐 IP Intelligence       | Find high-activity IP addresses                             |
| ⚠️ Critical Detection    | Detect CRITICAL and FATAL events                            |
| 🛡️ Security Detection   | Detect malware, ransomware, SQL injection, port scans, etc. |
| 🔎 Smart Search          | Search events by IP, user, message or level                 |
| 📑 CSV Reports           | Export complete analysis results                            |
| 🖥️ Web Dashboard        | Interactive browser-based monitoring                        |
| 🧪 Sample Logs           | Windows, Linux and application examples                     |

---

# 🧠 Detection Engine

The current system uses **explainable rule-based detection**.

This makes every alert understandable instead of producing a mysterious "AI score."

### 🔥 Detection Rules

#### 1. Repeated Error Detection

Detects multiple errors originating from the same IP address.

```text
ERROR Database timeout from 192.168.1.40
ERROR Database timeout from 192.168.1.40
ERROR Database timeout from 192.168.1.40
```

➡️ Result:

```text
Repeated errors from IP
```

---

#### 2. Brute-Force Detection

Detects repeated authentication failures.

```text
Failed login from 10.0.0.55
Failed login from 10.0.0.55
Failed login from 10.0.0.55
Authentication failed from 10.0.0.55
```

➡️ Result:

```text
Possible brute-force activity
```

---

#### 3. Critical Event Detection

Detects:

```text
CRITICAL
FATAL
```

Example:

```text
CRITICAL ransomware signature detected
```

➡️ Result:

```text
Critical event
```

---

#### 4. Security Keyword Detection

The engine searches for suspicious security-related patterns including:

```text
malware
ransomware
privilege escalation
port scan
SQL injection
unauthorized
denied
```

➡️ Result:

```text
Security keyword detected
```

---

#### 5. High Error Rate Detection

If a log contains an unusually high percentage of error events, the system flags the affected events for investigation.

---

# 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │     LOG SOURCES     │
                 │                     │
                 │ Windows / Linux /   │
                 │ Application Logs    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    LOG INGESTION    │
                 │                     │
                 │ Upload / File Read  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    LOG PARSER       │
                 │                     │
                 │ Regex + Extraction  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   DATA PROCESSING   │
                 │                     │
                 │       Pandas        │
                 └──────────┬──────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │     DETECTION ENGINE        │
              │                             │
              │ • Error Analysis            │
              │ • Brute Force Detection     │
              │ • IP Analysis               │
              │ • Security Keywords         │
              │ • Critical Events           │
              └──────────────┬──────────────┘
                             │
                             ▼
                 ┌─────────────────────┐
                 │ SECURITY DASHBOARD  │
                 │                     │
                 │ Statistics          │
                 │ Event Stream        │
                 │ IP Intelligence     │
                 │ Anomalies           │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   REPORT ENGINE     │
                 │                     │
                 │ CSV Export          │
                 └─────────────────────┘
```

---

# 🖥️ Dashboard

The dashboard provides a centralized view of the analyzed logs.

### Dashboard includes:

```text
┌──────────────────────────────────────────────────────────┐
│                    LOG INTELLIGENCE                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│ Total Events    Anomalies     Unique IPs       Log File │
│     120            14             8             app.log  │
│                                                          │
├────────────────────────┬─────────────────────────────────┤
│ Severity Breakdown     │ Top IP Addresses               │
│                        │                                 │
│ INFO       ████████    │ 192.168.1.40       14          │
│ WARNING    ███         │ 10.0.0.55          8           │
│ ERROR      █████       │ 172.16.2.44        5           │
│ CRITICAL   ██          │                                 │
├────────────────────────┴─────────────────────────────────┤
│ Event Stream                                             │
│                                                          │
│ Line | Time | Level | IP | User | Message | Anomaly    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

# 🛠️ Technology Stack

### Backend

```text
Python
Flask
Pandas
Regex
Loguru
```

### Frontend

```text
HTML5
CSS3
JavaScript
Fetch API
Responsive UI
```

### Data Processing

```text
Pandas DataFrames
Regex Pattern Matching
Frequency Analysis
Rule-Based Detection
```

---

# 📁 Project Structure

```text
Log-Intelligence/
│
├── 📄 app.py
├── 📄 log_engine.py
├── 📄 requirements.txt
├── 📄 README.md
├── 📄 .gitignore
│
├── 📂 sample_logs/
│   ├── sample_app.log
│   ├── linux_auth.log
│   └── windows_security.log
│
├── 📂 templates/
│   └── index.html
│
├── 📂 static/
│   ├── style.css
│   └── app.js
│
├── 📂 uploads/
│   └── .gitkeep
│
└── 📂 reports/
    └── .gitkeep
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Log-Intelligence.git
```

```bash
cd Log-Intelligence
```

---

## 2️⃣ Create Virtual Environment

### Windows

```powershell
py -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Application

```bash
python app.py
```

---

## 5️⃣ Open Dashboard

```text
http://127.0.0.1:5000
```

---

# 🧪 Test With Sample Logs

The project comes with three sample environments.

### 🖥️ Application Logs

```text
sample_logs/sample_app.log
```

Contains:

* Application events
* Database errors
* Authentication failures
* SQL injection detection
* Malware detection
* Payment-service errors

### 🐧 Linux Authentication Logs

```text
sample_logs/linux_auth.log
```

Contains:

* SSH events
* Failed authentication
* Unauthorized access
* Privilege escalation attempts

### 🪟 Windows Security Logs

```text
sample_logs/windows_security.log
```

Contains:

* Windows service events
* Administrator login failures
* Defender events
* Malware detection

---

# 🔍 Example Analysis

Input:

```text
2026-10-01 18:03:10 WARNING user=admin Failed login from 10.0.0.55
2026-10-01 18:03:12 WARNING user=admin Failed login from 10.0.0.55
2026-10-01 18:03:14 WARNING user=admin Failed login from 10.0.0.55
2026-10-01 18:03:16 ERROR user=admin Authentication failed from 10.0.0.55
```

The engine extracts:

```json
{
  "level": "ERROR",
  "ip": "10.0.0.55",
  "user": "admin",
  "anomaly": "Possible brute-force activity"
}
```

---

# 📊 Output

The platform generates:

### Event Statistics

```text
Total Events
Anomalies
Unique IP Addresses
Log File
```

### Severity Statistics

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
FATAL
```

### IP Intelligence

```text
IP Address → Event Count
```

### Event Intelligence

```text
Timestamp
Severity
IP
Username
Message
Anomaly
```

---

# 📄 Report Generation

After analysis, the dashboard allows the user to export the complete event stream.

Generated file:

```text
reports/log_intelligence_report.csv
```

Example:

```csv
line,timestamp,level,ip,user,message,anomaly
12,2026-10-01 18:03:10,WARNING,10.0.0.55,admin,Failed login,Possible brute-force activity
13,2026-10-01 18:03:12,WARNING,10.0.0.55,admin,Failed login,Possible brute-force activity
14,2026-10-01 18:03:14,WARNING,10.0.0.55,admin,Failed login,Possible brute-force activity
```

---

# 🔐 Security Considerations

This application is designed for **defensive log analysis**.

Uploaded files are treated as text and are not executed.

For production deployment, additional protections should be added:

* Authentication
* Authorization
* File-size limits
* MIME/type validation
* Rate limiting
* Secure upload storage
* HTTPS
* Access logging
* Database-backed audit trails
* Secret management

---

# 🧠 Why This Project Matters

Modern applications generate massive amounts of logs.

A security analyst cannot manually inspect every event.

Log Intelligence reduces that workload by transforming:

```text
RAW LOGS
   ↓
PARSING
   ↓
STRUCTURED DATA
   ↓
PATTERN ANALYSIS
   ↓
ANOMALY DETECTION
   ↓
SECURITY INTELLIGENCE
```

The project demonstrates practical knowledge of:

* Python development
* Data processing
* Regular expressions
* Backend development
* REST APIs
* Web dashboards
* Cybersecurity concepts
* Event analysis
* Defensive security automation

---

# 🚀 Future AI/ML Roadmap

The current version uses transparent rule-based detection.

The next generation can introduce machine learning.

### Phase 1 — Machine Learning

```text
Isolation Forest
        ↓
Unsupervised Anomaly Detection
```

Detect unusual:

* Login frequency
* IP behavior
* Error rates
* Request patterns
* Event sequences

---

### Phase 2 — Supervised Detection

Add:

```text
Scikit-learn
XGBoost
LightGBM
```

Possible classes:

```text
Normal
Brute Force
Port Scan
Malware
Privilege Escalation
Web Attack
Authentication Attack
```

---

### Phase 3 — NLP Log Intelligence

Use:

```text
TF-IDF
Sentence Transformers
Embeddings
NLP
```

Convert:

```text
Raw Log Message
       ↓
Text Embedding
       ↓
Similarity Search
       ↓
Related Incidents
```

---

### Phase 4 — AI Security Analyst

Future architecture:

```text
             LOG DATA
                │
                ▼
          ML DETECTION
                │
                ▼
        INCIDENT CORRELATION
                │
                ▼
          RISK ANALYSIS
                │
                ▼
        AI SECURITY ANALYST
                │
       ┌────────┴────────┐
       ▼                 ▼
   SUMMARY          RECOMMENDATION
```

The AI layer could generate human-readable incident summaries such as:

```text
Incident Detected

Severity: High

Source:
10.0.0.55

Observed Activity:
Multiple authentication failures within a short period.

Potential Category:
Authentication attack

Recommended Investigation:
Review authentication events and source-IP activity.
```

---

# 🛰️ Future SIEM Architecture

Long-term architecture:

```text
Windows ─────┐
             │
Linux ───────┤
             ▼
Applications → LOG COLLECTOR
             │
             ▼
       MESSAGE QUEUE
             │
             ▼
       LOG PROCESSOR
             │
       ┌─────┴─────┐
       ▼           ▼
     RULES         ML
       │           │
       └─────┬─────┘
             ▼
      INCIDENT ENGINE
             │
       ┌─────┴─────┐
       ▼           ▼
   DASHBOARD       AI
       │           │
       └─────┬─────┘
             ▼
        SOC ANALYST
```

Potential integrations:

```text
Elasticsearch
OpenSearch
Kafka
Redis
PostgreSQL
Docker
Kubernetes
MITRE ATT&CK
```

---

# 🎯 Learning Outcomes

By building this project, you practice:

### Python

* File handling
* Functions
* Regular expressions
* Data structures
* Exception handling
* Modular architecture

### Data Analysis

* Pandas
* Aggregation
* Frequency analysis
* Data transformation
* CSV processing

### Web Development

* Flask
* REST APIs
* HTML
* CSS
* JavaScript
* Fetch API

### Cybersecurity

* Log analysis
* Authentication monitoring
* IP analysis
* Threat indicators
* Anomaly detection
* Security event correlation

---

# 👨‍💻 Author

## Vansh Bakshi

**BCA | Full Stack Developer | Python Programmer | AI/ML & Cybersecurity Enthusiast**

```text
Python • AI/ML • Full Stack • Flutter • Cybersecurity
```

---

# ⭐ Project Vision

> **From raw logs to actionable intelligence.**

Log Intelligence is not just a log viewer.

It is the foundation for building an intelligent security-monitoring ecosystem capable of combining:

```text
Logs
+
Data Analytics
+
Machine Learning
+
NLP
+
Threat Intelligence
+
AI
=
Intelligent Security Operations
```

---

# 📜 License

This project is intended for **educational, research, and defensive cybersecurity purposes**.

---

<p align="center">
  <b>🛡️ Log Intelligence — Analyze. Detect. Understand.</b>
</p>

<p align="center">
  Built with Python 🐍 • Flask ⚡ • Pandas 📊 • Regex 🔎 • Loguru 📝
</p>

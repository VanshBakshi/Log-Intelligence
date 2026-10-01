# Log Intelligence

A practical log-analysis and monitoring dashboard built with Python, Flask, Pandas, Regex and Loguru.

## Features

- Parse Windows/Linux/application-style text logs
- Detect log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL, FATAL
- Extract timestamps, IP addresses and usernames
- Search and filter events in the browser
- Rule-based anomaly detection
- Detect repeated errors from an IP
- Detect possible brute-force authentication attempts
- Detect security-related keywords
- Detect critical/fatal events
- Calculate log statistics
- Show top IP addresses and repeated messages
- Export analyzed events to CSV
- Includes realistic sample logs
- Handles UTF-8 and malformed log characters safely

## Project structure

```text
Log-Intelligence/
├── app.py
├── log_engine.py
├── requirements.txt
├── README.md
├── sample_logs/
│   ├── sample_app.log
│   ├── linux_auth.log
│   └── windows_security.log
├── reports/
├── uploads/
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Run in VS Code

Open the project folder in VS Code.

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Use your own logs

Click **Upload Log File** and select a `.log`, `.txt`, or similar text log.

The parser does not execute the uploaded file; it reads it as text.

## Detection logic

The current engine uses explainable rules rather than pretending that simple rules are an ML model:

1. Repeated errors from the same IP
2. Multiple failed authentication events from the same IP
3. Critical/fatal events
4. Security keywords such as malware, ransomware, port scan, SQL injection, unauthorized and privilege escalation
5. High error-rate periods

This makes the project easy to explain in an interview and easy to extend with machine learning later.

## Future advanced extensions

- Isolation Forest anomaly detection
- XGBoost log classification
- Sentence-transformer embeddings
- LLM-powered incident summaries
- MITRE ATT&CK technique mapping
- Real-time file tailing
- Windows Event Log / EVTX ingestion
- Linux journald ingestion
- SIEM integration
- Alerting through email/Telegram/Slack
- Elasticsearch/OpenSearch storage

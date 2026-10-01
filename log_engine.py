from pathlib import Path
from datetime import datetime
import re
import pandas as pd
from loguru import logger

LEVEL_RE = re.compile(r"\b(DEBUG|INFO|NOTICE|WARNING|WARN|ERROR|CRITICAL|FATAL)\b", re.I)
DATE_PATTERNS = [
    re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})"),
    re.compile(r"(?P<date>\d{4}/\d{2}/\d{2}[ T]\d{2}:\d{2}:\d{2})"),
]
IP_RE = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
USER_RE = re.compile(r"\b(?:user|username|account)=([A-Za-z0-9_.@-]+)", re.I)

def parse_line(line, line_no):
    original = line.rstrip("\n")
    level_match = LEVEL_RE.search(original)
    level = level_match.group(1).upper() if level_match else "UNKNOWN"

    timestamp = None
    for pattern in DATE_PATTERNS:
        m = pattern.search(original)
        if m:
            timestamp = m.group("date").replace("/", "-")
            break

    ip_match = IP_RE.search(original)
    user_match = USER_RE.search(original)

    message = original
    if level_match:
        message = original[level_match.end():].lstrip(" :-\t")

    return {
        "line": line_no,
        "timestamp": timestamp or "",
        "level": level,
        "ip": ip_match.group(0) if ip_match else "",
        "user": user_match.group(1) if user_match else "",
        "message": message[:500],
    }

def detect_anomalies(df):
    if df.empty:
        return df

    df["anomaly"] = ""
    error_count = df["level"].isin(["ERROR", "CRITICAL", "FATAL"]).sum()

    # Rule 1: repeated errors from same IP
    if "ip" in df.columns:
        ip_errors = df[df["level"].isin(["ERROR", "CRITICAL", "FATAL"])]["ip"].value_counts()
        suspicious_ips = set(ip_errors[ip_errors >= 3].index) - {""}
        df.loc[df["ip"].isin(suspicious_ips), "anomaly"] = "Repeated errors from IP"

    # Rule 2: brute-force-like repeated authentication failures
    auth_mask = df["message"].str.contains(
        r"failed login|authentication failed|invalid password|login failed",
        case=False, regex=True, na=False
    )
    auth_ips = df.loc[auth_mask, "ip"].value_counts()
    brute_ips = set(auth_ips[auth_ips >= 3].index) - {""}
    df.loc[df["ip"].isin(brute_ips) & auth_mask, "anomaly"] = "Possible brute-force activity"

    # Rule 3: critical/fatal
    critical = df["level"].isin(["CRITICAL", "FATAL"])
    df.loc[critical, "anomaly"] = "Critical event"

    # Rule 4: suspicious security keywords
    security = df["message"].str.contains(
        r"malware|ransomware|privilege escalation|port scan|sql injection|unauthorized|denied",
        case=False, regex=True, na=False
    )
    df.loc[security, "anomaly"] = "Security keyword detected"

    # Rule 5: high error ratio
    if len(df) >= 10 and error_count / len(df) >= 0.30:
        df.loc[df["level"].isin(["ERROR", "CRITICAL", "FATAL"]), "anomaly"] = "High error-rate event"

    return df

def analyze_logs(path):
    path = Path(path)
    logger.info("Analyzing {}", path)

    if not path.exists():
        raise FileNotFoundError(path)

    records = []
    with path.open("r", encoding="utf-8", errors="replace") as f:
        for number, line in enumerate(f, start=1):
            if line.strip():
                records.append(parse_line(line, number))

    df = pd.DataFrame(records)
    if df.empty:
        return {
            "file": path.name, "total": 0, "levels": {}, "anomalies": 0,
            "ips": [], "top_messages": [], "events": []
        }

    df = detect_anomalies(df)

    level_counts = df["level"].value_counts().to_dict()
    anomaly_count = int((df["anomaly"] != "").sum())
    ips = df.loc[df["ip"] != "", "ip"].value_counts().head(10).to_dict()

    top_messages = (
        df["message"].value_counts()
        .head(10)
        .rename_axis("message")
        .reset_index(name="count")
        .to_dict(orient="records")
    )

    events = df.fillna("").to_dict(orient="records")

    return {
        "file": path.name,
        "total": int(len(df)),
        "levels": {str(k): int(v) for k, v in level_counts.items()},
        "anomalies": anomaly_count,
        "ips": [{"ip": k, "count": int(v)} for k, v in ips.items()],
        "top_messages": top_messages,
        "events": events,
    }

def export_report(events, output):
    df = pd.DataFrame(events)
    if df.empty:
        df = pd.DataFrame(columns=["line", "timestamp", "level", "ip", "user", "message", "anomaly"])
    df.to_csv(output, index=False)
    logger.info("Report written to {}", output)

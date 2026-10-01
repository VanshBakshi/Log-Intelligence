from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
from log_engine import analyze_logs, export_report

app = Flask(__name__)
BASE = Path(__file__).parent
UPLOADS = BASE / "uploads"
REPORTS = BASE / "reports"
UPLOADS.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def api_analyze():
    uploaded = request.files.get("logfile")
    sample = request.form.get("sample", "sample_app.log")

    if uploaded and uploaded.filename:
        safe_name = Path(uploaded.filename).name
        path = UPLOADS / safe_name
        uploaded.save(path)
    else:
        path = BASE / "sample_logs" / sample
        if not path.exists():
            return jsonify({"error": "Sample log not found"}), 404

    result = analyze_logs(path)
    return jsonify(result)

@app.route("/api/report", methods=["POST"])
def api_report():
    data = request.get_json(force=True)
    path = REPORTS / "log_intelligence_report.csv"
    export_report(data.get("events", []), path)
    return send_file(path, as_attachment=True, download_name=path.name)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

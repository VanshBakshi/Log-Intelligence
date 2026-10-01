let currentData = {events: []};

async function analyze() {
    const form = new FormData();
    const file = document.getElementById("file").files[0];
    form.append("sample", document.getElementById("sample").value);
    if (file) form.append("logfile", file);

    setMessage("Analyzing log file...");
    try {
        const response = await fetch("/api/analyze", {method:"POST", body:form});
        const data = await response.json();
        if (!response.ok) throw new Error(data.error || "Analysis failed");
        currentData = data;
        updateDashboard();
        setMessage(`Analysis complete: ${data.total} events inspected.`);
    } catch (e) {
        setMessage("Error: " + e.message);
    }
}

function setMessage(text) {
    document.getElementById("message").textContent = text;
}

function updateDashboard() {
    document.getElementById("total").textContent = currentData.total;
    document.getElementById("anomalies").textContent = currentData.anomalies;
    document.getElementById("uniqueIps").textContent = currentData.ips.length;
    document.getElementById("filename").textContent = currentData.file;
    renderLevels();
    renderIps();
    renderTable();
}

function renderLevels() {
    const box = document.getElementById("levels");
    box.innerHTML = "";
    const levels = currentData.levels || {};
    const max = Math.max(...Object.values(levels), 1);
    Object.entries(levels).forEach(([level, count]) => {
        const row = document.createElement("div");
        row.className = "bar-row";
        row.innerHTML = `<span>${escapeHtml(level)}</span>
            <div class="bar"><div class="fill" style="width:${count/max*100}%"></div></div>
            <strong>${count}</strong>`;
        box.appendChild(row);
    });
}

function renderIps() {
    const box = document.getElementById("ips");
    box.innerHTML = "";
    if (!currentData.ips.length) {
        box.innerHTML = "<p>No IP addresses detected.</p>";
        return;
    }
    currentData.ips.forEach(item => {
        const row = document.createElement("div");
        row.className = "ip-row";
        row.innerHTML = `<span>${escapeHtml(item.ip)}</span><strong>${item.count}</strong>`;
        box.appendChild(row);
    });
}

function renderTable() {
    const body = document.getElementById("events");
    const query = document.getElementById("search").value.toLowerCase();
    body.innerHTML = "";

    currentData.events
        .filter(e => JSON.stringify(e).toLowerCase().includes(query))
        .forEach(e => {
            const tr = document.createElement("tr");
            const cls = levelClass(e.level);
            tr.innerHTML = `
                <td>${e.line}</td>
                <td>${escapeHtml(e.timestamp)}</td>
                <td><span class="badge ${cls}">${escapeHtml(e.level)}</span></td>
                <td>${escapeHtml(e.ip)}</td>
                <td>${escapeHtml(e.user)}</td>
                <td>${escapeHtml(e.message)}</td>
                <td class="anomaly">${escapeHtml(e.anomaly)}</td>`;
            body.appendChild(tr);
        });
}

function levelClass(level) {
    if (["CRITICAL","FATAL"].includes(level)) return "critical";
    if (["ERROR"].includes(level)) return "error";
    if (["WARNING","WARN"].includes(level)) return "warn";
    return "info";
}

async function downloadReport() {
    if (!currentData.events || !currentData.events.length) {
        setMessage("Analyze a log first.");
        return;
    }
    const response = await fetch("/api/report", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({events:currentData.events})
    });
    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "log_intelligence_report.csv";
    a.click();
    URL.revokeObjectURL(url);
}

function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, ch => ({
        "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
    }[ch]));
}

window.addEventListener("load", analyze);

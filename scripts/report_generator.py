from parser import parse_log
from attack_detector import detect_sqli, detect_traversal
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

log_file = os.path.join(BASE_DIR, "data", "access.log")

html_report = os.path.join(BASE_DIR, "reports", "report.html")
excel_report = os.path.join(BASE_DIR, "reports", "report.xlsx")

df = parse_log(log_file)

sqli = detect_sqli(df)
traversal = detect_traversal(df)

score = (len(sqli) * 10) + (len(traversal) * 10)

if score <= 20:
    risk = "LOW"
elif score <= 40:
    risk = "MEDIUM"
elif score <= 60:
    risk = "HIGH"
else:
    risk = "CRITICAL"

top_ips = df["IP"].value_counts().head(10)

html = f"""
<html>
<head>
<title>Web Attack Investigation Report</title>
</head>
<body>

<h1>Web Attack Investigation Report</h1>

<h2>Summary</h2>

<ul>
<li>Total Requests: {len(df)}</li>
<li>Unique IPs: {df['IP'].nunique()}</li>
<li>SQL Injection Attempts: {len(sqli)}</li>
<li>Traversal Attempts: {len(traversal)}</li>
<li>Risk Score: {score}</li>
<li>Risk Level: {risk}</li>
</ul>

<h2>Top IPs</h2>

<pre>
{top_ips.to_string()}
</pre>

<h2>MITRE ATT&CK</h2>

<ul>
<li>T1190 - Exploit Public Facing Application</li>
</ul>

</body>
</html>
"""

with open(html_report, "w", encoding="utf-8") as f:
    f.write(html)

with pd.ExcelWriter(excel_report) as writer:

    df.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    sqli.to_excel(
        writer,
        sheet_name="SQLi",
        index=False
    )

    traversal.to_excel(
        writer,
        sheet_name="Traversal",
        index=False
    )

print("Relatórios gerados com sucesso.")
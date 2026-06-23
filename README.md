# Web Attack Investigator

Projeto desenvolvido para análise de logs Apache/Nginx com foco em Blue Team e SOC.

## Objetivos

- Detectar SQL Injection
- Detectar Directory Traversal
- Gerar relatórios automáticos
- Mapear técnicas MITRE ATT&CK
- Identificar Indicadores de Comprometimento (IOCs)

## Tecnologias

- Python
- Pandas
- Streamlit
- OpenPyXL
- Matplotlib

## Dashboard

![Dashboard](images/dashboard.png)

## Funcionalidades

- Top IPs
- HTTP Status Codes
- SQL Injection Detection
- Directory Traversal Detection
- Risk Score
- Excel Reports
- HTML Reports

## MITRE ATT&CK

| Técnica | Descrição |
|----------|----------|
| T1190 | Exploit Public Facing Application |

## Como executar

```bash
pip install -r requirements.txt
python scripts/report_generator.py
streamlit run dashboard.py
```

## Autor

Rodrigo Horvath Torbes
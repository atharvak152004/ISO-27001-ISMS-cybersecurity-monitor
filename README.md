# ISO-27001-ISMS-cybersecurity-monitor
An engineering-led ISO 27001:2022 ISMS framework for a health-tech environment, featuring structured risk management, compliance policies, and an automated Python log monitor for active security baseline enforcement.

# Zenith AI: Engineering-Led ISO 27001:2022 ISMS Implementation

An end-to-end, engineering-focused Information Security Management System (ISMS) designed for **Zenith AI** (a mock healthcare tech startup managing sensitive patient data and proprietary machine learning models). 

This project bridges traditional Governance, Risk, and Compliance (GRC) frameworks with automated security engineering by implementing an active Python-based log monitor alongside foundational compliance documentation.

## 🚀 Project Overview

Most ISMS implementations stop at policies and spreadsheets. This project goes a step further by treating compliance as a continuous, automated engineering function. 

### Key Highlights:
* **Context & Scope Defined:** Tailored specifically for a 100% remote, cloud-based health-tech organization (AWS Mumbai region) handling Indian DPDP Act requirements.
* **Risk-Based Approach:** Comprehensive Asset Inventory, Risk Assessments, and a Statement of Applicability (SoA) mapped to ISO 27001:2022 Annex A controls.
* **Automated Monitoring (Control A.8.16):** A functional Python Monitoring Engine that analyzes real-time simulated log streams using multivariate security baseline thresholds.
* **Incident Response Integration (Control A.5.24):** Automated warning mechanisms to detect system anomalies (e.g., brute-force attacks, DDoS, data exfiltration) and queue alerts.

---

## 📂 Repository Structure

```text
├── Documentation/
│   ├── Context and Scope.md          # Interested parties, expectations, and DPDP alignment
│   ├── Assets Inventory.csv          # Asset classification registry (AST-001 to AST-011)
│   ├── Risk Assessment & Treatment.csv# Threat modeling, inherent risk scores, and mitigations
│   └── Statement of Applicability.csv# Justification for 2022 Annex A control inclusions/exclusions
├── Policies/
│   └── Secure Coding Policy.md       # Developer guidelines for Control A.8.28 (Secrets management, SAST)
├── Scripts/
│   └── security_monitor.py           # Automated Control A.8.16 Monitoring Engine
└── README.md

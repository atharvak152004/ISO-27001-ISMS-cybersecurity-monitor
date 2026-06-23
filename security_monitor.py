import time
import random
from datetime import datetime

# --- ISO 27001 Configuration (Zenith AI) ---
# These are your 'Security Baselines'. If data goes above these, it triggers an ALERT.
THRESHOLDS = {
    'failed_logins': 5,          # Potential Brute Force Attack
    'api_calls': 300,            # Potential DDoS or Data Scraping
    'code_pushes': 4,            # Unusual Developer Activity
    'data_download_mb': 100,     # Potential Data Leak/Exfiltration
    'unauthorized_apps': 1       # Policy Violation (Access Control)
}

def get_live_metrics():
    """
    Simulates real-time 'Time Series' data logs from Zenith AI.
    """
    # Normal 'Healthy' system behavior
    metrics = {
        'failed_logins': random.randint(0, 2),
        'api_calls': random.randint(50, 150),
        'code_pushes': random.randint(0, 1),
        'data_download_mb': random.randint(1, 15),
        'unauthorized_apps': 0
    }
    
    # 10% chance to simulate a 'Security Incident' (Anomaly Detection Demo)
    if random.random() > 0.90:
        print("\n[!] --- WARNING: ANOMALY DETECTED IN LOG STREAM ---")
        metrics['failed_logins'] = 15
        metrics['api_calls'] = 850
        metrics['data_download_mb'] = 220
        
    return metrics

# --- Monitoring Engine ---
print(f"--- Zenith AI Security Monitor Initialized ---")
print(f"Targeting ISO 27001 Compliance: Control A.8.16 (Monitoring)\n")

try:
    while True:
        data = get_live_metrics()
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Check if any metric has violated the ISMS thresholds
        violations = []
        for key, value in data.items():
            if value >= THRESHOLDS[key]:
                violations.append(f"VIOLATION: {key} is {value} (Limit: {THRESHOLDS[key]})")

        # --- Alert System (Incident Response) ---
        if violations:
            print(f"⚠️  [{timestamp}] ALERT: SECURITY BASELINE BREACHED!")
            for v in violations:
                print(f"   -> {v}")
            print("   -> ACTION: Notification sent to Slack/Discord Bot (Control A.5.24)\n")
        else:
            print(f"✅ [{timestamp}] System Healthy. (Logins: {data['failed_logins']}, API: {data['api_calls']})")

        time.sleep(3) # Check the "Time Series" every 3 seconds

except KeyboardInterrupt:
    print("\n[!] Monitoring stopped by User.")
# SETTINGS for SCRAPING and STORING information
TRACK_TERMS = [
    "toscana", "tuscany",  # Regione Toscana
    "covid", "sars-cov-2",  # Covid
    "iit", "cnr",  # CNR terms
    "spoofing", "spam", "phishing", "cybersecurity", "trojan", "malware", "exploit", "ransomware", "hacker", "cracker",
    "CVE", "vulnerabilità", "cyber", "cyber terrorismo", "cyberbullismo", "virus"
]
CONNECTION_STRING = "sqlite:///db/{}.db"
CSV_NAME = "db/tweets.csv"
JSON_NAME = "db/tweets.json"
TABLE_NAME = "tweets"
LOG_FILE = "logs/{}.log"

try:
    from private import *
except Exception:
    print("KEYS for OAuth not found...")
    pass

# libraries
import json
import csv
import requests
import os
from datetime import datetime
# FETCH DATA (SAFE)
try:
    resp_BTC = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")
    resp_ETH = requests.get("https://api.coinbase.com/v2/prices/ETH-USD/spot")
    resp_LTC = requests.get("https://api.coinbase.com/v2/prices/LTC-USD/spot")
except requests.exceptions.ConnectionError:
    print("No internet connection. Please check your network.")
    exit()
# check status codes
if (resp_BTC.status_code != 200 or 
    resp_ETH.status_code != 200 or 
    resp_LTC.status_code != 200):
    print("Error fetching data from API")
    exit()
# PROCESS DATA
BTC_data = resp_BTC.json()
ETH_data = resp_ETH.json()
LTC_data = resp_LTC.json()
time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
record = {
    "time": time_now,
    "BTC": BTC_data["data"]["amount"],
    "ETH": ETH_data["data"]["amount"],
    "LTC": LTC_data["data"]["amount"]
}
fields = ["time", "BTC", "ETH", "LTC"]
# CSV HANDLING
if not os.path.exists("crypto_history.csv"):
    with open("crypto_history.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
with open("crypto_history.csv", "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writerow(record)
# JSON HANDLING
try:
    with open("crypto_history.json", "r") as f:
        json_history = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    json_history = []
json_history.append(record)
with open("crypto_history.json", "w") as f:
    json.dump(json_history, f, indent=2)
# OUTPUT
print(f"""===== Crypto Tracker =====
Time: {time_now}
BTC: {record['BTC']}
ETH: {record['ETH']}
LTC: {record['LTC']}
Total records saved: {len(json_history)}
==========================""")
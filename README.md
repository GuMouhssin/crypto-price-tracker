# Crypto Price Tracker 📈

A Python script that fetches live cryptocurrency prices 
from the Coinbase API and automatically saves them to 
both CSV and JSON files for historical tracking.

## What it does

- Fetches real-time prices for BTC, ETH and LTC
- Saves every run as a timestamped record
- Builds a price history automatically over time
- Handles network errors and API failures gracefully

## Technologies

- Python 3
- Requests
- Coinbase Public API
- CSV / JSON file handling

## How to run

1. Install dependencies:
pip install requests

2. Run the script:
python crypto_tracker.py

3. Check your data:
- crypto_history.csv
- crypto_history.json

## Sample output

===== Crypto Tracker =====
Time: 2024-11-01 14:32:10

BTC: $68943.21
ETH: $2451.10
LTC: $73.42

Total records saved: 12
==========================

## Use cases

- Monitor crypto prices over time
- Build datasets for analysis
- Foundation for price alert systems

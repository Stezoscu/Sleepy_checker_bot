import os
import time
import requests

API_KEY = os.getenv("TORN_API_KEY")
TRACKED_ITEM_IDS = [243, 244, 245]  # Example: Donator Pack, FHC, Xanax

def fetch_item_market(item_id):
    url = f"https://api.torn.com/torn/?selections=itemmarket&item={item_id}&key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("itemmarket", {})
    except Exception as e:
        print(f"Error fetching item {item_id}: {e}")
        return {}

while True:
    print("Polling item market...")
    for item_id in TRACKED_ITEM_IDS:
        market_data = fetch_item_market(item_id)
        print(f"Item {item_id}: {len(market_data)} listings found.")
    time.sleep(20)

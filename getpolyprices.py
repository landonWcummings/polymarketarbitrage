import requests
import json

# Fetch events from the Polymarket API
r = requests.get("https://gamma-api.polymarket.com/events?closed=false")
response = r.json()

# Filter events related to elections
events = {}
for event in response:
    if 'Election' in event['title']:
        events[event['id']] = event

def valid(a, b):
    return 0 < a < 1 and 0 < b < 1

# Initialize buy and sell sums
buysum = 0
sellsum = 0

# Check markets for specific questions
for market in events.get('903193', {}).get('markets', []):
    if 'outcomePrices' in market and 'clobTokenIds' in market:
        if "Kamala" in market['question']:
            #print(market['id'], market['question'], market['outcomePrices'])
            outcome_prices = json.loads(market['outcomePrices'])
            print(outcome_prices)
            buysum += float(outcome_prices[0])
            sellsum += float(outcome_prices[1])
            print('=========')

        if "Trump" in market['question']:
            #print(market['id'], market['question'], market['outcomePrices'])
            outcome_prices = json.loads(market['outcomePrices'])
            print(outcome_prices)
            buysum += float(outcome_prices[0])
            sellsum += float(outcome_prices[1])
            print('=========')


# Print the total sums for both Kamala and Trump markets
print(f"Total Sum of Buy Prices: {buysum}")
print(f"Total Sum of Sell Prices: {sellsum}")

if buysum <= 0.99:
    print("execute buy")
if buysum >= 0.997:
    print("execute sell")

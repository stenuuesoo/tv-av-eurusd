import requests
import time
import json

# Replace YOUR_API_KEY with your actual Alpha Vantage API key
api_key = "x_x"

# TradingView Paper Trading API credentials
paper_trading_api_key = "YOUR_PAPER_TRADING_API_KEY"
paper_trading_account_id = "YOUR_PAPER_TRADING_ACCOUNT_ID"

# Define the interval for fetching real-time data
interval = 1  # Fetch data every 1 minute

while True:
    # Fetch real-time EUR/USD data from Alpha Vantage
    url = f"https://www.alphavantage.co/query?function=CURRENCY_REALTIME&from_currency=EUR&to_currency=USD&interval={interval}m&apikey={api_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract the latest real-time quote
    latest_quote = data["Realtime Currency Data"]["5. Exchange Rate"]
    print(f"Real-time EUR/USD price: {latest_quote}")

    # Implement your trading logic here to determine the trade action (buy, sell, or hold)
    # Based on your trading strategy, determine whether to buy, sell, or hold EUR/USD
    trade_action = "buy"  # Replace with your actual trading decision

    # Generate a trade order for TradingView Paper Trading
    trade_order = {
        "symbol": "EURUSD",
        "amount": 1,  # Adjust the trade amount as needed
        "side": trade_action,  # "buy", "sell", or "hold"
    }

    # Send the trade order to TradingView Paper Trading API
    headers = {
        "Authorization": f"Bearer {paper_trading_api_key}",
        "Content-Type": "application/json",
    }
    data = json.dumps(trade_order)
    url = f"https://api.tradingview.com/paperTrading/v1/accounts/{paper_trading_account_id}/orders"
    response = requests.post(url, headers=headers, data=data)

    # Check the response status code to ensure successful order execution
    if response.status_code == 200:
        print(f"Trade order successfully placed: {trade_action}")
    else:
        print(f"Failed to place trade order: {response.status_code}")

    # Wait for the defined interval before fetching the next data update
    time.sleep(interval * 60)
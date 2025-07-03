# api/signal.py

import random

def handler(request):
    signal = random.choice(["BUY", "SELL", "WAIT"])
    print(f"📡 Signal sent: {signal}")

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": f'{{"signal": "{signal}"}}'
    }

import random

def handler(request):
    signal = random.choice(["BUY", "SELL", "WAIT"])
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": f'{{"signal": "{signal}"}}'
    }

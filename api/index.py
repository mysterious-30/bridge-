def handler(request):
    ip = request.get("headers", {}).get("x-forwarded-for", "unknown")
    print(f"👋 Visitor from IP: {ip}")

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/plain" },
        "body": f"Hello from Vercel Python API! Your IP: {ip}"
    }

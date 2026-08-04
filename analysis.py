def analyze(event):

    actual = float(event["actual"])
    forecast = float(event["forecast"])

    if actual > forecast:
        return (
            "📈 USD Bullish\n"
            "📉 Gold Bearish\n"
            "📉 EURUSD Bearish"
        )

    elif actual < forecast:
        return (
            "📉 USD Bearish\n"
            "📈 Gold Bullish\n"
            "📈 EURUSD Bullish"
        )

    return "Neutral"

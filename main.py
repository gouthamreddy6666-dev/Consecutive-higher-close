import yfinance as yf

stocks = [
    "RELIANCE.NS",
    "BEL.NS",
    "HAL.NS",
    "ONGC.NS",
    "SBIN.NS"
]

CONSECUTIVE_DAYS = 3

print("\nStarting Consecutive Higher Close Scanner...\n")

qualified = []

for stock in stocks:

    try:
        df = yf.download(
            stock,
            period="30d",
            interval="1d",
            auto_adjust=True,
            progress=False
        )

        closes = df['Close'].tolist()

        condition = True

        for i in range(1, CONSECUTIVE_DAYS + 1):

            if closes[-i] <= closes[-(i + 1)]:
                condition = False
                break

        if condition:

            qualified.append(stock)

            print(
                f"{stock} → "
                f"{CONSECUTIVE_DAYS} consecutive higher closes"
            )

    except Exception as e:
        print(f"Error scanning {stock}: {e}")

print("\n===================")
print("QUALIFIED STOCKS")
print("===================\n")

for q in qualified:
    print(q)

print("\nScanner completed.\n")

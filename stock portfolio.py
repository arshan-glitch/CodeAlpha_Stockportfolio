
# Stock Portfolio Tracker
# Task 3- Code Alpha Internship

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190,
    "NVDA": 120
}

portfolio = []
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input(
        "\nEnter stock name (or 'done' to finish): "
    ).strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append({
        "Stock": stock_name,
        "Quantity": quantity,
        "Price": price,
        "Investment": investment
    })

    total_investment += investment

    print(f"{stock_name} added successfully!")
    print(f"Investment value: ${investment:,.2f}")

# Display portfolio summary
print("\n" + "=" * 45)
print("           PORTFOLIO SUMMARY")
print("=" * 45)

if portfolio:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for item in portfolio:
        print(
            f"{item['Stock']:<10}"
            f"{item['Quantity']:<10}"
            f"${item['Price']:<9.2f}"
            f"${item['Investment']:.2f}"
        )

    print("-" * 45)
    print(f"Total Investment: ${total_investment:,.2f}")

    # Save portfolio to CSV file
    with open("stock_portfolio.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Stock", "Quantity", "Price", "Investment"]
        )
        writer.writeheader()
        writer.writerows(portfolio)

    print("\nPortfolio saved to stock_portfolio.csv")

else:
    print("No stocks were added to your portfolio.")

print("\nThank you for using Stock Portfolio Tracker!")
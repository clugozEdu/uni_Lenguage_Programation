# Description: Write a function discount(price) that takes a price as input and returns the price after a 10% discount if the price is greater than 500, and the original price otherwise.
def discount(price):
    if price > 500:
        discount = price * 0.10  # 10% discount
        price_final = price - discount
        return price_final
    else:
        return price
      
# Examples
def main():
    print(discount(1000))  # 900.0
    print(discount(200))  # 200
    print(discount(500))  # 500

main()
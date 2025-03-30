def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (discount_percent * price / 100)     
        return final_price
    else:
        return price
        
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount_percentage: "))

print (calculate_discount(price, discount_percent))

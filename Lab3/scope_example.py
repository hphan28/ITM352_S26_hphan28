#This Program demonstrates variable scope in Python
#Name: Harrison Phan
#Date: 2024-02-05

def calculate_discounted_price(price):
    discount = 0.9
    price = price * discount
    print (f"Discounted Price inside function:{price:.2f}")
price = 100
print (f"Original Price before function call: {price:.2f}")
discounted_price = calculate_discounted_price(price)

print(f"Original Price after function call: {price:.2f}")

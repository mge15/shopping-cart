# shopping_cart.py
import os

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#input one or more product identifiers

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "OOPS, please set env var called 'SENDGRID_API_KEY'")
MY_ADDRESS = os.environ.get("MY_EMAIL_ADDRESS", "OOPS, please set env var called 'MY_EMAIL_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY)
print("Client:", type(client))

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
#
# or maybe ...
#html_content = "Hello <strong>World</strong>"
#
# or maybe ...
#html_list_items = "<li>You ordered: Product 1</li>"
#html_list_items += "<li>You ordered: Product 2</li>"
#html_list_items += "<li>You ordered: Product 3</li>"
#html_content = f"""
#<h3>Hello this is your receipt</h3>
#<p>Date: ____________</p>
#<ol>
#    {html_list_items}
#</ol>
#"""
print("HTML:", html_content)

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS,
               subject=subject, html_content=html_content)

try:
    response = client.send(message)

    # > <class 'python_http_client.client.Response'>
    print("RESPONSE:", type(response))
    print(response.status_code)  # > 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e.message)

TAX_RATE = float(os.environ.get("TAX_RATE", default = 0))

print(TAX_RATE)

total_price = 0
checkout = []

while True:
    id = input("Please input a product identifier, or 'DONE'  if there are no more items: ")
    if id == "DONE":
        break
    try:
        n = float(id)
    except ValueError:
        print ("Input must be a number between 1-20. Try again or input 'Done' if there are no more items")
    else:
        checkout.append(id)

#look-up products
#product_ids = [1, 8, 6, 16, 6]  # temporary list of valid ids for testing purposes

#print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", product_ids)

#TODO: perform product look-ups here!

print("--------------------------------")
print("Safeway")
print("--------------------------------")
print("Web: https://local.safeway.com/safeway/dc/washington/1855-wisconsin-ave-nw.html")
print("Phone: (202) 333-3223")
print("Checkout Time: 2021-01-15 14:07:25")
print("--------------------------------")
print("Shopping Cart Items:")

for prod_id in checkout:
    matching_products = [prod for prod in products if str(prod["id"]) == str(prod_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("+ ", matching_product["name"], "(", to_usd(matching_product["price"]), ")")

print("Total Price:", str(total_price))
tax = int(total_price) * (TAX_RATE)
net_total = int(total_price) + tax

# Print the receipt
# Went back into code to add appropriate print statements

print("--------------------------------")
print("Subtotal:", to_usd(total_price))
print("Plus Sales Tax:", to_usd(tax))
print("Total:", to_usd(net_total))
print("--------------------------------")
print("Thanks for your business! Please come again.")

#answer = input("Would you like to receive the receipt by email? [y]/n: ")
  #  if answer == "y"
   # if answer == "n"
#else: print("Invalid input. Please input y for 'yes' or n for 'no'")

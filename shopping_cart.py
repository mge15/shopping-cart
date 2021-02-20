# shopping_cart.py
import os
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from dotenv import load_dotenv
from datetime import datetime

products = [
    {"id": 1, "name": "Chocolate Sandwich Cookies", "department": "snacks",
        "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id": 2, "name": "All-Seasons Salt", "department": "pantry",
        "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea",
        "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce",
        "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care",
        "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id": 7, "name": "Pure Coconut Water With Orange", "department": "beverages",
        "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen",
        "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs",
        "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages",
        "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages",
        "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id": 12, "name": "Chocolate Fudge Layer Cake", "department": "frozen",
        "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care",
        "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household",
        "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id": 15, "name": "Overnight Diapers Size 6", "department": "babies",
        "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks",
        "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood",
        "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen",
        "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta",
        "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id": 21, "name": "Organic Bananas", "department": "fruit", "aisle": "fresh produce", "price": 0.79, "price_per": "pound"}
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
load_dotenv()

TAX_RATE = float(os.environ.get("TAX_RATE", default=0))

timestamp = datetime.now()
human_friendly_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")

total_price = 0
checkout = []
pounds = []

while True:
    id = input("Please input a product identifier, or 'DONE'  if there are no more items: ")
    if id == "DONE":
        break
    try:
        n = float(id)
    except ValueError:
        print("Input must be a number between 1-20. Try again or input 'DONE' if there are no more items")
    else:
        if float(id) >= 1 and float(id) <= 21:
            if float(id) == 21:
                lbs = input("Please input the number of pounds: ")
                pounds.append(lbs)
                checkout.append(id)
            else:
                checkout.append(id)
        else:
            print("Input must be a number between 1-20. Try again or input 'DONE' if there are no more items")

#look-up products
#product_ids = [1, 8, 6, 16, 6]  # temporary list of valid ids for testing purposes

#print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", product_ids)

#TODO: perform product look-ups here!

print("--------------------------------")
print("Safeway")
print("--------------------------------")
print("Address: 1855 Wisconsin Ave NW, Washington, DC, 20007")
print("Web: https://local.safeway.com/safeway/dc/washington/1855-wisconsin-ave-nw.html")
print("Phone: (202) 333-3223")
print("Checkout Time: ", human_friendly_timestamp)
print("--------------------------------")
print("Shopping Cart Items:")

pdcts = []
i = 0

for prod_id in checkout:
    matching_products = [prod for prod in products if str(prod["id"]) == str(prod_id)]
    matching_product = matching_products[0]
    if matching_product["price_per"] == "item":
        total_price = total_price + matching_product["price"]
        pdcts.append({"id": prod_id, "name": matching_product["name"], "price": to_usd(matching_product["price"])})
        print("+ ", matching_product["name"], "(", to_usd(matching_product["price"]), ")")
    else:
        price = matching_product["price"] * float(pounds[i])
        total_price = total_price + price
        pdcts.append({"id": prod_id, "name": matching_product["name"], "price": to_usd(price)})
        print("+ ", matching_product["name"], "(", to_usd(price), ")")
        i = i + 1

print("Total Price:", to_usd(total_price))
tax = total_price * (TAX_RATE)
net_total = total_price + tax

# Print the receipt
# Went back into code to add appropriate print statements

print("--------------------------------")
print("Subtotal:", to_usd(total_price))
print("Plus Sales Tax:", to_usd(tax))
print("Total:", to_usd(net_total))
print("--------------------------------")
print("Would you like a receipt?")

#email code
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

# this must match the test data structure


template_data = {
    "total_price_usd": to_usd(net_total),
    "human_friendly_timestamp": human_friendly_timestamp,
    "subtotal_price_usd": to_usd(total_price),
    "tax_usd": to_usd(tax),
    "products": pdcts
}  # or construct this dictionary dynamically based on the results of some other process :-D

# > <class 'sendgrid.sendgrid.SendGridAPIClient>


client = SendGridAPIClient(SENDGRID_API_KEY)
#print("CLIENT:", type(client))

#subject = "Your Receipt from Safeway"

#html_content = "Hello World"
#print("HTML:", html_content)

# FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
# ... but we can customize the `to_emails` param to send to other addresses

#message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

recipient = input("Please input your email address, or 'N' to opt out: ")

if recipient == "N":
    print("OK! Printing out receipt now.")
else:
    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    #print("MESSAGE:", type(message))

    print("Sending receipt via email...")

    try:
        response = client.send(message)

        # > <class 'python_http_client.client.Response'>
        #print("RESPONSE:", type(response))
        #print(response.status_code)  # > 202 indicates SUCCESS
        #print(response.body)
        #print(response.headers)
        print("Email sent successfully!")

    except Exception as err:
        print(type(err))
        print(err)

print("Thanks for your business! Please come again.")
#end email code

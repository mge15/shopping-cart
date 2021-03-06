## Shopping Cart Project
# Objective

Write a program that asks the user to input one or more product identifiers, then looks up the prices for each, then prints an itemized customer receipt including the total amount owed.

Here is the [project description](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/shopping-cart/README.md)

Attribution: Most of the instructions included in this Read Me File are from the "Shopping Cart" Project Instructions and associated further exploration challenge instructions.

## Setup
# Repo Setup

Create a new remote project repository on GitHub called  "shopping-cart". When prompted, add a "README.md" file and a Python-flavored ".gitignore" file during the repo creation process. After this process is complete, you should be able to view the repo on GitHub at an address like  https://github.com/YOUR_USERNAME/shopping-cart.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd shopping-cart
```

Use the text editor or the command-line to create a file in that repo called "shopping_cart.py", and then place the following contents inside:

```sh
# shopping_cart.py

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

print(products)
```

Check that the setup is correct by running the Python script from the command-line:

```sh
python shopping_cart.py
```

# Environment Setup

If you are interested in pursuing the bonus challenges, you will want to create and activate a new Anaconda virtual environment, and use a "requirements.txt" file approach

```sh
# IF USING THIRD-PARTY PACKAGES, USE A NEW ENV:
conda create -n shopping-env python=3.8
conda activate shopping-env
pip install -r requirements.txt # (after specifying desired packages inside; we will do this in the bonus challenges)
```

Within an active virtual environment of choice ("base" or project-specific), run the Python script from the command-line:

```sh
python shopping_cart.py
```

If you see the provided "products" data structure, you're ready to move on to project development.

## Step 1: Capturing User Inputs

1. Accept a user input value, store it in a variable, and print it. HINT: use the input() function
2. One at a time, iteratively accept a user input value, store it in a variable, and print it. HINT: use an infinite while loop. NOTE: you may have to press "control-c" to quit your script if you get stuck.
3. One at a time, iteratively accept a user input value, store it in a variable, and print it. But stop the loop if the user inputs the word "DONE". HINT: use an if statement in conjunction with the break keyword.
4. Repeat the previous step, but instead of printing each user input, store them all in a single list. Then print the list after the user is "DONE".

## Step 2: Look-up Products

To speed-up the development process, temporarily shift approach to use a hard-coded list of product identifiers instead of asking for inputs each time you want to test the program. At this time, your script might look something like this:

```sh
products = [...] #<--- that long list of product dictionaries provided above

#
# some commented-out loop
# ... representing the result of the first checkpoint (if you did it)
# ... which accepts user inputs
# ... and prints the results
# ... and which we are temporarily ignoring
# ... (yours will actually be some working python code)
#

product_ids = [1, 8, 6, 16, 6] # temporary list of valid ids for testing purposes

print("SHOPPING CART ITEM IDENTIFIERS INCLUDE:", product_ids)

#TODO: perform product look-ups here!
```

1. For a single valid product identifier, look up the matching product and print its name and price. HINT: try using a custom function in conjunction with a list comprehension.
2. For each valid product identifier in the example list, look up the matching product and print its name and price.
3. For each valid product identifier in the example list, look up the matching product and print its name and price, and add its price to a running-total of all prices, then print the running-total after iterating through the entire list.

## Printing the Receipt

The receipt should include:
1. A grocery store name of your choice
2. A grocery store phone number and/or website URL and/or address of choice
3. The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
4. The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
5. The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
6. The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
7. The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
8. A friendly message thanking the customer and/or encouraging the customer to shop again

## Customizing the Sales Tax

The user is allowed to configure the sales tax by passing an environment variable called "TAX_RATE" stored in a local ".env" file.

To get started, import the module that is necessary when working with a ".env" file

```sh
import os
```

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify the tax rate:

    TAX_RATE= put value here

In the "requirements.txt" file, put the following contents:

```sh
# this is the requirements.txt file
python-dotenv
```

Use the following code to take the environment variables from .env and assign it to a variable.

```sh
from dotenv import load_dotenv

load_dotenv()

TAX_NAME = os.getenv("TAX_RATE", default=0)

```

## Sending Receipts via Email
# Installation

From within an active virtual environment, install the sendgrid package

```sh
pip install sendgrid

# optionally install a specific version:
#pip install sendgrid==6.6.0
```

# Setup

Sign up for a SendGrid account, then follow the instructions to complete the "Single Sender Verification," clicking the link in a confirmation email to verify your account.

Then create a SendGrid API Key with "full access" permissions. Store the API Key value in an environment variable called SENDGRID_API_KEY.

Also set an environment variable called SENDER_ADDRESS to be the same email address as the single sender address you just associated with your SendGrid account (e.g. "abc123@gmail.com").

Use a ".env" file approach to managing these environment variables.

# Usage

Test that the the installation and setup worked by sending the following email:

```sh
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "Your Receipt from the Green Grocery Store"

html_content = "Hello World"
print("HTML:", html_content)

# FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
# ... but we can customize the `to_emails` param to send to other addresses
message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
    print(type(err))
    print(err)
```

Check inbox to see that it was sent successfully

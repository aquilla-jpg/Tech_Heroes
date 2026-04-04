#import the needed library
import pandas as pd

#create a dictionary with the product catalog
catalog = {'Product ID': ['RICE02','PUR50','MAX02','BIG01','JEH03','SPH25','CAL11','DIS25','SHEA30','LED71','BRE10'],
          'Product': ['2lbs White Rice', 'Shark - Air Purifier - White', 'Apple - Airpods Max 2', 'Bigga - Kola Champange Flavored Soda', 'JEHONN - Dustpan and Brush', 'Sophie - 3 Ply Tissue', "Cal's - Cherry Syrup", 'Disney - Mickey Tumbler', 'Shea - Clarifying Shampoo', 'Pursonic - LED 3-in-1 Bundle', 'Breeze - Air Mist - Lavendar'],
          'Price': [103.69, 20444.94, 5084.02, 339.02, 994.45, 1008.05, 1900.45, 3560, 1843.05, 8596.05, 6097.65],
          'Quantity': [10, 20, 25, 10, 15, 20, 10, 20, 10, 20, 10]}

#convert the dictionary to a DataFrame for a table-like view
df = pd.DataFrame(catalog)

"""
This dictionary assigns product information to the product id. This was done to
make it easier to retrive information about a specific product and limit
possible errors.
"""
products = {
    "RICE02": {"Product":"2lbs White Rice", "Price": 103.69,"Quantity": 10},
    "PUR50": {"Product": "Shark - Air Purifier - White", "Price": 20444.94,"Quantity": 20},
    "MAX02": {"Product": "Apple - Airpods Max 2", "Price": 5084.02, "Quantity": 25},
    "BIG01": {"Product": "Bigga - Kola Champange Flavored Soda", "Price": 339.02, "Quantity": 10},
    "JEH03": {"Product": "JEHONN - Dustpan and Brush", "Price": 994.45, "Quantity": 15},
    "SPH25": {"Product": "Sophie - 3 Ply Tissue", "Price": 1008.05, "Quantity": 20},
    "CAL11": {"Product": "Cal's - Cherry Syrup", "Price": 1900.45, "Quantity": 10},
    "DIS25": {"Product": "Disney - Mickey Tumbler", "Price": 3560.00, "Quantity": 20},
    "SHEA30": {"Product": "Shea - Clarifying Shampoo", "Price": 1843.05, "Quantity": 10},
    "LED71": {"Product": "Pursonic - LED 3-in-1 Bundle", "Price": 8596.05, "Quantity": 20},
    "BRE10": {"Product": "Breeze - Air Mist - Lavendar", "Price": 6097.65, "Quantity": 10}
    }

#Define variables
discount_rate = 0.05
discount_limit = 5000
sales_tax = 0.10

def add_to_cart(cart):

  #while the user wants to add product/s to the cart
  while True:

    #ask the user for the product id, .upper() turns letters to all caps
    product_id = input("Please enter the Product ID of the item you wish to add to your cart. ").upper()

    #check if the product id is not the products dictionary
    if product_id not in products:
      print("Invalid Product ID!")
      continue

    #while the product id is in the dictionary
    while True:

      #do
      try:

        """
        ask the user to enter the quantity of the product they want
        int() converts the input to an integer
        """
        quantity = int(input("Enter the quantity: "))

        #if the quantity is less or equal to 0
        if quantity <= 0:
          print("Invalid quantity. Please enter a positive number.")

        #if the quantity is greater than 0
        else:

          #exit the statement
          break

      #if ValueError is outputted
      except ValueError:
        print("Invalid input. Please enter a number.")

    #get the row index for prouct id in catalog
    row = df.loc[df['Product ID'] == product_id].index[0]

    #locate the exact position of the quantity of the product
    stock = df.loc[row, 'Quantity']

    #if the quantity is greater than the stock available
    if quantity > stock:
      print(f"Not enough stock available for {products[product_id]['Product']}. Available: {stock}. You requested: {quantity}")

      #skip the following steps
      continue

    #look for the name of the product in the same row and store in product name
    product_name = df.loc[row, 'Product']

    #look for the price of the product in the same row and store in unit price
    unit_price = df.loc[row, 'Price']

    #check if product is already in the shopping cart
    if product_id in cart:

      #add the new quantity to what is already in the cart
      cart[product_id]['Quantity'] += quantity

    #if the product is not in the cart
    else:

      #add the new product and detials to the cart
      cart[product_id] = {
        'Product': product_name,
        'Price': unit_price,
        'Quantity': quantity}

    #update the quantity in df to reflect the quantity minus what was added to the cart
    df.at[row, 'Quantity'] -= quantity
    print(f"{product_name} added to cart (Quantity: {quantity})")

    #if the quantity in df for the product is less than 5
    if df.at[row, 'Quantity'] < 5:

      #alert the user that stock is low
      print(f"Alert - Low stock: {product_name}. Remaining: {df.at[row, 'Quantity']}")

    #if the quantity is equal to 0
    if df.at[row, 'Quantity'] == 0:

      #alert the user that the product is out of stock
      print(f"Out of stock: {product_name}")

    #ask the user if they want to add another product, .lower() turns letters into lower case
    another = input("Do you want to add another item to your cart? (yes/no): ").lower()

    #if the answer is not yes
    if another != "yes":

        #ask if they wish to proceed to check out
        ready = input("Are you ready to checkout? (yes/no): ").lower()

        #if the entered input is yes
        if ready == "yes":
          #call the checkout function
          checkout(cart)

        #exit the loop
        return False

#create a function to remove items from the shopping cart
def remove_from_cart(cart):

  #check if the cart empty
  if not cart:

    #exit the statment
    return

  #ask the user to enter the product id of the product they wish to remove
  product_id = input("Please enter the Product ID to remove: ").upper()

  #check if the product id is not in the cart
  if product_id not in cart:
    print("Invalid Product ID!")

    #exit the if block
    return

  #while the product id is in the cart
  while True:

    #do
    try:

      #ask how much of the product is to be removed
      quantity = int(input("Enter quantity to remove: "))

      #if the quantity is less than or equal to 0
      if quantity <= 0:
        print("Enter a positive number.")
        #exit the if block
        continue

    #if an error occurs
    except ValueError:
        print("Invalid quantity.")
        continue

    #get the current quantity of the item in the cart
    current_qty = cart[product_id]['Quantity']

    #if the quantity to be removed is greater than the quantity inside the cart
    if quantity > current_qty:
        print("Cannot remove more than what's in cart.")

        #ask for the quantity to be removed again
        return

    #update the product catalog
    #look for the row index of Product ID and assign to row
    row = df.loc[df['Product ID'] == product_id].index[0]

    #look for the quantity of the product in catalog and add what was taken from cart back to catalog
    df.at[row, 'Quantity'] += quantity

    #subtract the quantity to be removed from what is in cart
    cart[product_id]['Quantity'] -= quantity

    #if the quantity of the product is equal to 0
    if cart[product_id]['Quantity'] == 0:

        #delete the profuct from the cart
        del cart[product_id]
        print("Item completely removed from cart")

    #if the quantity is greater than 0
    else:
        print(f"Removed {quantity} item(s). Remaining in cart: {cart[product_id]['Quantity']}")
        print("\n↩ --------------------Returning to main menu---------------------")
    break

#create a function that accepts one argument and shows the user what is in their cart
def view_cart(cart):

    #checks if the cart is empty
    if not cart:

      #if yes
      print("🛒 Your cart is empty")
      return

    print("\n*************** YOUR CART **********************")

    #establish the variable subbtotal
    subtotal = 0

    #create the headers for a table
    print(f"{'Product ID':<12} {'Product':<30} {'Qty':<8} {'Unit Price':<12} {'Total'}")
    print("\n-------------------------------------------------------------------")

    #loop through each key-value pair
    for product_id, item in cart.items():

      #store the price of one product to unit price
      unit_price = item['Price']

      #store the quantity
      quantity = item['Quantity']

      #calculate the total of the product
      item_total = unit_price * quantity

      #add the variables to the table
      print(f"{product_id:<12} {item['Product']:<30} {quantity:<8} "
              f"${unit_price:<11.2f} ${item_total:.2f}")

      #add the total of the product to the subtotal
      subtotal += item_total

    print("\n-------------------------------------------------------------------")
    print(f"Subtotal: ${subtotal:.2f}")
    print("\n↩ --------------------Returning to main menu---------------------")

#create a function to remove items from the shopping cart
def remove_from_cart(cart):

  #check if the cart empty
  if not cart:

    #exit the statment
    return

  #ask the user to enter the product id of the product they wish to remove
  product_id = input("Please enter the Product ID to remove: ").upper()

  #check if the product id is not in the cart
  if product_id not in cart:
    print("Invalid Product ID!")

    #exit the if block
    return

  #while the product id is in the cart
  while True:

    #do
    try:

      #ask how much of the product is to be removed
      quantity = int(input("Enter quantity to remove: "))

      #if the quantity is less than or equal to 0
      if quantity <= 0:
        print("Enter a positive number.")
        #exit the if block
        continue

    #if an error occurs
    except ValueError:
        print("Invalid quantity.")
        continue

    #get the current quantity of the item in the cart
    current_qty = cart[product_id]['Quantity']

    #if the quantity to be removed is greater than the quantity inside the cart
    if quantity > current_qty:
        print("Cannot remove more than what's in cart.")

        #ask for the quantity to be removed again
        return

    #update the product catalog
    #look for the row index of Product ID and assign to row
    row = df.loc[df['Product ID'] == product_id].index[0]

    #look for the quantity of the product in catalog and add what was taken from cart back to catalog
    df.at[row, 'Quantity'] += quantity

    #subtract the quantity to be removed from what is in cart
    cart[product_id]['Quantity'] -= quantity

    #if the quantity of the product is equal to 0
    if cart[product_id]['Quantity'] == 0:

        #delete the profuct from the cart
        del cart[product_id]
        print("Item completely removed from cart")

    #if the quantity is greater than 0
    else:
        print(f"Removed {quantity} item(s). Remaining in cart: {cart[product_id]['Quantity']}")
        print("\n↩ --------------------Returning to main menu---------------------")
    break

def check_stock():

  #ask the user for the product id of product they are looking for
  product_id = input("Please enter the Product ID of the item you wish to check: ").upper()

  #check if product id is not in the product dictionary
  if product_id not in products:
    print("Invalid Product ID!")

    #exit the if block
    return

  #assign the rox index of the product id to row
  row = df.loc[df['Product ID'] == product_id].index[0]

  #assigns the value found in same row under product to product
  product = df.loc[row, 'Product']

  #assigns the value found in the same row under quantity to quantity
  quantity = df.loc[row, 'Quantity']

  #display the quantity of the product
  print("\n STOCK CHECK")
  print(f"The quantity of {product} is {quantity}")
  print("\n↩ --------------------Returning to main menu---------------------")

def checkout(cart):

  #check if the cart is not empty
  if not cart:
    print("Your cart is empty")
    return False

  #if the cart is not empty
  #calculate the subtotal
  subtotal = sum (item['Price'] * item['Quantity'] for item in cart.values())

  #establish the discount variable
  discount = 0

  #if the subtotal is greater than the discount limit
  if subtotal > discount_limit:

    #calculate the discount
    discount = subtotal * discount_rate

  #calculate tax
  tax_amount = subtotal * sales_tax

  #calculate the total
  total = subtotal + tax_amount - discount

  #display
  print("\n CHECKOUT")
  print(f"Subtotal: ${subtotal:.2f}")
  print(f"Discount: ${discount:.2f}")
  print(f"Tax: ${tax_amount:.2f}")
  print(f"Total Due: ${total:.2f}")

  #ask for the customer's name
  customer_name = input("Enter your name: ").capitalize()

  #
  while True:
    #while the cart is not empty
    try:

      #ask for payment
      payment = float(input("Enter payment amount: $"))

      #if payment is less than the total
      if payment < total:
          print("Insufficient payment")

      #if the payment exceeds or equals the total
      else:

          #exit the loop
          break

    #
    except ValueError:
        print("Invalid input")

  #calculate the change
  change = payment - total

  #call the generate receipt function
  generate_receipt(customer_name, cart, subtotal, discount, tax_amount, total, payment, change)

  #clear the shopping cart for the next transaction
  cart.clear()

  #handles errors
  return True

#create a function that takes 8 arguments and generate a receipt
def generate_receipt(customer_name, cart, subtotal, discount, tax_amount, total, payment, change):
  print("\n************************************")
  print("\n   BEST BUY RETAIL STORE RECEIPT")
  print("\n************************************")

  #for every item in the cart values
  for item in cart.values():

    #calculate the total price for the product selected
    total = item['Price'] * item['Quantity']
    print(f"{item['Product']}")
    print(f"Quantity: {item['Quantity']} x ${item['Price']} = ${total:.2f}")
    print("\n**********************************************")

    print(f"Customer Name: {customer_name}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Total Due: ${total:.2f}")
    print(f"Payment: ${payment:.2f}")
    print(f"Change: ${change:.2f}")
    print("\n Thank you for shopping with Best Buy!")
    print("\n*********************************************")

#establish an empty cart
cart = {}

#main loop
while True:

  #Best Buy Menu
  print("\n*************************BEST BUY MENU*************************")
  print (df)
  print("\n***************************************************************")
  print("1. Add to Cart   2. Remove from Cart")
  print("3. View Cart     4. Checkout")
  print("5. Check Stock   6. Exit")

  #ask the user to select an option
  choice = input("Please select an option (1-6): ")

  #the follow nested if statements matches the users selection to the appropriate function
  if choice == "1":
      if add_to_cart(cart):
        break

  elif choice == "2":
      remove_from_cart(cart)

  elif choice == "3":
      view_cart(cart)

  elif choice == "4":
      if checkout(cart):
        cart = {}

  elif choice == "5":
      check_stock()

  elif choice == "6":
      print("Thank you for choosing BEST BUY!")
      break

  #if the user selected a number that was not an option
  else:
    print("Invalid option")

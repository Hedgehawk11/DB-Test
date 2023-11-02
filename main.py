# Import the required libraries
# Connect to the MongoDB server

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import easywebhooks

uri = "mongodb+srv://eee:eee@cluster0.mnooggh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
print('connected!')
# Create/connect to the bank database
db = client['bank']

# Create/connect to the users collection
users = db['users']
"""
# Create 6 users
users.insert_many([
    {'name': 'Hedgehawk11', 'balance': 1000},
    {'name': 'Psych82', 'balance': 1000},
    {'name': 'Kingofcheeze', 'balance': 1000},
    {'name': 'Captainbanna19', 'balance': 1000},
    {'name': 'fullwizard', 'balance': 1000},
    {'name': 'Dave', 'balance': 10000}
])
"""

name = input("Enter your name: ")
for user in users.find():
  if user['name'] == name:
    print("Welcome back, " + name + "!")
    person = name
    break




# Connect to MongoDB

db = client['bank']
users = db['users']
def balance_inquiry():
  name = input("Enter your name: ")
  user = users.find_one({'name': name})
  print( f"Your current balance is: {user['balance']}")
choice = ""
def main_menu():
  print("1. Transfer money")
  print("2. Balance inquiry")
  choice = input("Enter your choice: ")
    
  if choice == 1:

    print("Choose the recipient:")
    for user in users.find():
      print(user['name'])
    recipient = input("Enter the recipient: ")

    amount = float(input("Enter the amount to transfer: "))

    sender_user = users.find_one({'name': sender})
    recipient_user = users.find_one({'name': recipient})
    sender_balance = sender_user['balance']
    recipient_balance = recipient_user['balance']

    if sender_balance >= amount:
      sender_balance -= amount
      recipient_balance += amount

      users.update_one({'name': user}, {'$set': {'balance': sender_balance}})
      users.update_one({'name': recipient}, {'$set': {'balance': recipient_balance}})
        
      easywebhooks.send(f"{user} has transferred {amount} to {recipient}")
      return "Transfer successful!"
    else:
      return "Insufficient balance for transfer."
  elif choice == 2:
    balance_inquiry()
      


main_menu()
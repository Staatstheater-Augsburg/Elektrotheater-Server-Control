from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

print("Enter username:")
username = input()

print("Enter password:")
password = input()

print("Please copy this line to your .env file:\n")

print(username + ' = "' + generate_password_hash(password) + '"\n')
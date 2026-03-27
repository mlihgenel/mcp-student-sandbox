import os

AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")

def connect():
    print(f"Connecting with: {AWS_SECRET_KEY}")

# Test the function
connect()

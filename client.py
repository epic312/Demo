import sys
def perform_attack():
    # TODO: Your attack code goes here
    # You have intercepted: message and its mac
    intercepted_message = b"amount=100&to=alice"
    intercepted_mac = "..." # From server.py output
# Your goal: append data and compute valid forged MAC
    data_to_append = b"&admin=true"
    forged_message = b"" # Replace with your forged message
    forged_mac = "" # Replace with your forged MAC
    print("Forged message:", forged_message)
    print("Forged MAC:", forged_mac)
if __name__ == "__main__":
    perform_attack()
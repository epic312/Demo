# === secure_server.py (Using HMAC for Secure Implementation) ===
import hmac
import hashlib

SECRET_KEY = b'supersecretkey'

def generate_mac(message: bytes) -> str:
    return hmac.new(SECRET_KEY, message, hashlib.md5).hexdigest()

def verify(message: bytes, mac: str) -> bool:
    expected_mac = generate_mac(message)
    return mac == expected_mac

def main():
    message = b"amount=100&to=alice"
    mac = generate_mac(message)

    print("=== Secure Server Simulation ===")
    print(f"Original message: {message.decode()}")
    print(f"MAC: {mac}")

    forged_message = message + b"&admin=true"
    forged_mac = mac

    print("--- Verifying forged message ---")
    if verify(forged_message, forged_mac):
        print("MAC verified (unexpected, should not happen).")
    else:
        print("MAC verification failed (expected). Secure implementation works.")

if __name__ == "__main__":
    main()
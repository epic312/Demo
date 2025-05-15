# MAC Forgery Assignment - Demonstration and Defense

## Files Included:
- `server.py`: Insecure implementation using MD5 with `MAC = hash(secret || message)`
- `client.py`: Attack script using `hashpumpy` to perform length extension attack.
- `secure_server.py`: Secure version of the server using HMAC.
- `background_writeup.pdf`: Theoretical explanation of MACs and the attack.
- `mitigation_writeup.pdf` / `.docx`: Explanation of secure mitigation using HMAC.

## How to Run:

### 1. Run the Vulnerable Server
```bash
python server.py
```
- Displays the original message and MAC.
- Tries to verify a forged message (will fail without attack).

### 2. Run the Attack
```bash
python client.py
```
- Performs a length extension attack.
- Tries different key lengths to forge a valid MAC.
- Shows the forged message and MAC if successful.

### 3. Run the Secure Server
```bash
python secure_server.py
```
- Uses HMAC instead of hash(secret || message).
- Verifies that forged MACs are no longer accepted.

## Dependencies
- Python 3.x
- `hashpumpy`:
```bash
pip install hashpumpy
```

## Conclusion
This assignment demonstrates why naive MAC constructions are insecure and how HMAC mitigates these issues. Always use HMAC for secure authentication.
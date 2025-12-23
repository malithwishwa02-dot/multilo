import json

FIELDS = [
    ("name", "Full Name"),
    ("address", "Billing Address"),
    ("phone", "Phone Number"),
    ("email", "Email"),
    ("dob", "Date of Birth (YYYY-MM-DD)"),
    ("cc_number", "Card Number (16 digits)"),
    ("exp", "Expiration (MM/YYYY)"),
    ("cvv", "CVV (3-4 digits)"),
    ("target", "Target (domain/IP/API/URL/service/etc)")
]

def interactive_fulz_input():
    fulz = {}
    print("== INTERACTIVE FULZ & TARGET INPUT ==")
    for field, prompt in FIELDS:
        fulz[field] = input(f"{prompt}: ").strip()
    # Validate CC number (Luhn)
    from profile_generator import luhn_check
    if not luhn_check(fulz["cc_number"]):
        print("❌ Invalid credit card number (Luhn fail).")
        exit(1)
    return fulz

def load_fulz_json(path):
    with open(path, 'r') as f:
        fulz = json.load(f)
    # (same validation as above)
    return fulz
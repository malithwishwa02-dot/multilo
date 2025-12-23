from quantum_multilogin_generator_v2 import QuantumIdentityGenerator, QuantumMultiloginGenerator
import os
import json
import random

def luhn_check(card_number):
    """
    Checks if a card number is valid according to the Luhn algorithm.
    """
    if not card_number or not card_number.isdigit():
        return False
        
    digits = [int(d) for d in str(card_number)]
    checksum = 0
    reverse_digits = digits[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            if doubled > 9:
                doubled -= 9
            checksum += doubled
        else:
            checksum += digit
            
    return checksum % 10 == 0

def generate_profile(fulz, output_dir):
    """
    Generates a profile based on fulz input and saves it to output_dir.
    Returns the loaded profile data or path to the main profile file.
    """
    # 1. Adapt fulz to persona structure
    parts = fulz.get('name', '').split()
    first_name = parts[0] if parts else "Unknown"
    last_name = " ".join(parts[1:]) if len(parts) > 1 else "Unknown"
    
    exp_parts = fulz.get('exp', '').split('/')
    if len(exp_parts) == 2:
        exp_date = f"{exp_parts[0]}/{exp_parts[1]}" # MM/YYYY
    else:
        exp_date = "12/2025" # default
        
    persona = {
        "identity": {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": fulz.get('name', f"{first_name} {last_name}"),
            "date_of_birth": fulz.get('dob', '1990-01-01'),
            "ssn": None # fulz doesn't seem to have SSN usually
        },
        "contact": {
            "email": fulz.get('email', 'test@example.com'),
            "phone": fulz.get('phone', '555-0123')
        },
        "address": {
            "street": fulz.get('address', '123 Main St'),
            "city": "New York", # Default or parse better if address is full
            "state": "NY",
            "zip_code": "10001",
            "country": "USA"
        },
        "financial": {
            "card": {
                "number": fulz.get('cc_number', ''),
                "type": "Unknown",
                "bin": fulz.get('cc_number', '')[:6] if fulz.get('cc_number') else ''
            },
            "expiration": exp_date,
            "cvv": fulz.get('cvv', '')
        },
        "metadata": {
            "generated_at": "now",
            "persona_id": "imported"
        }
    }
    
    # 2. Use QuantumMultiloginGenerator to create files
    merchant = fulz.get('target', 'amazon.com')
    # Clean merchant string
    if merchant.startswith('http'):
        merchant = merchant.split('://')[-1]
    if merchant.startswith('www.'):
        merchant = merchant[4:]
        
    if not output_dir:
        output_dir = "out"
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    ml_gen = QuantumMultiloginGenerator(persona, merchant)
    main_file = ml_gen.export_all_data(output_dir)
    
    # Return the generated profile object (dict) so inject_artifacts can use it
    return ml_gen.generate_browser_profile()

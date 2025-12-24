"""
Validation utilities for Quantum Profile Warmup CLI
Provides input validation and data verification functions
"""

import re
from typing import Optional, Dict, Any, List

class ValidationError(Exception):
    """Custom validation error"""
    pass

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone: str) -> bool:
    """Validate phone number format (XXX-XXX-XXXX)"""
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))

def validate_card_number(card_number: str) -> bool:
    """Validate credit card number using Luhn algorithm"""
    if not card_number.isdigit():
        return False
    
    digits = [int(d) for d in card_number]
    
    # Luhn algorithm
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    return sum(digits) % 10 == 0

def validate_cvv(cvv: str, card_type: str = "visa") -> bool:
    """Validate CVV format"""
    if card_type.lower() in ["american express", "amex"]:
        return len(cvv) == 4 and cvv.isdigit()
    return len(cvv) == 3 and cvv.isdigit()

def validate_zip_code(zip_code: str) -> bool:
    """Validate US ZIP code format"""
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))

def validate_expiration_date(exp_date: str) -> bool:
    """Validate expiration date format (MM/YYYY)"""
    pattern = r'^(0[1-9]|1[0-2])/\d{4}$'
    return bool(re.match(pattern, exp_date))

def validate_fulz_data(fulz: Dict[str, Any]) -> List[str]:
    """
    Validate FULZ (Full Person) data structure
    
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Check required fields
    required_fields = ["identity", "contact", "address", "financial"]
    for field in required_fields:
        if field not in fulz:
            errors.append(f"Missing required field: {field}")
    
    # Validate identity
    if "identity" in fulz:
        identity = fulz["identity"]
        if "full_name" not in identity:
            errors.append("Missing identity.full_name")
    
    # Validate contact
    if "contact" in fulz:
        contact = fulz["contact"]
        if "email" in contact and not validate_email(contact["email"]):
            errors.append(f"Invalid email format: {contact['email']}")
        if "phone" in contact and not validate_phone(contact["phone"]):
            errors.append(f"Invalid phone format: {contact['phone']}")
    
    # Validate address
    if "address" in fulz:
        address = fulz["address"]
        required_address_fields = ["street", "city", "state", "zip_code"]
        for field in required_address_fields:
            if field not in address:
                errors.append(f"Missing address.{field}")
        
        if "zip_code" in address and not validate_zip_code(address["zip_code"]):
            errors.append(f"Invalid ZIP code format: {address['zip_code']}")
    
    # Validate financial
    if "financial" in fulz:
        financial = fulz["financial"]
        if "card" in financial:
            card = financial["card"]
            if "number" in card and not validate_card_number(card["number"]):
                errors.append(f"Invalid card number (Luhn check failed)")
        
        if "cvv" in financial and not validate_cvv(financial["cvv"]):
            errors.append(f"Invalid CVV format")
        
        if "expiration" in financial and not validate_expiration_date(financial["expiration"]):
            errors.append(f"Invalid expiration date format (use MM/YYYY)")
    
    return errors

def validate_profile_data(profile: Dict[str, Any]) -> List[str]:
    """
    Validate multilogin profile data structure
    
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    required_fields = ["profile_id", "os", "browser", "user_agent"]
    for field in required_fields:
        if field not in profile:
            errors.append(f"Missing required profile field: {field}")
    
    return errors

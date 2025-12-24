import os
import requests

API_BASE_URL = "https://api.multilogin.com/v2"
API_KEY = os.getenv("MULTILOGIN_API_KEY")  # Set in environment or .env file

def get_headers():
    '''Get authorization headers for Multilogin API'''
    if not API_KEY:
        raise ValueError("MULTILOGIN_API_KEY not set in environment variables.")
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def list_profiles():
    '''Fetch all browser profiles'''
    endpoint = f"{API_BASE_URL}/browser_profiles"
    response = requests.get(endpoint, headers=get_headers())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error listing profiles: {response.status_code} {response.text}")
        return None

def create_profile(profile_data):
    '''Create a new browser profile using posted data according to API docs'''
    endpoint = f"{API_BASE_URL}/browser_profiles"
    response = requests.post(endpoint, headers=get_headers(), json=profile_data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Error creating profile: {response.status_code} {response.text}")
        return None

if __name__ == "__main__":
    # Example: List profiles
    print("Listing browser profiles...")
    profiles = list_profiles()
    print(profiles)

    # Example: Create new profile (replace with required fields as per API)
    profile_example = {
        "name": "TestProfile",
        # Add more fields from the API documentation as needed.
    }
    print("Creating a new browser profile...")
    result = create_profile(profile_example)
    print(result)
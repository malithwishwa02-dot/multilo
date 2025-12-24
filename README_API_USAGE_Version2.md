# Multilogin API Integration for `multilo`

This module securely interacts with the [Multilogin API](https://documenter.getpostman.com/view/28533318/2s946h9Cv9#6170937a-d3f3-4f08-b0a4-32331d2a6a49).

## Getting Started

### Prerequisites

- Python 3.x
- Multilogin account and API access (token)

### Setup

1. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

2. **Configure your API key securely**  
   - Copy `.env.example` to `.env` and fill in your actual key, or set as an environment variable:
     ```
     MULTILOGIN_API_KEY=your_actual_multilogin_api_key
     ```

3. **Usage**
   - To list profiles:
     ```
     python multilogin_api_client.py
     ```
   - To create profiles, edit `profile_example` in the script with required fields from [API Docs](https://documenter.getpostman.com/view/28533318/2s946h9Cv9#6170937a-d3f3-4f08-b0a4-32331d2a6a49).

## Security
- Never commit your `.env` file or API keys to a public repo!
- Use `.gitignore` to exclude secrets:
  ```
  .env
  ```
- Rotate keys regularly in your Multilogin dashboard.

## Extending
- Add more functions for other endpoints following the patterns in `multilogin_api_client.py`.
- Refer to [Postman API Docs](https://documenter.getpostman.com/view/28533318/2s946h9Cv9) for full endpoint specs.

## Troubleshooting
- If authentication fails, check your API key setup.
- For endpoint errors, consult the printed error code and doc links.

---

**For any custom integration or advanced API workflow, extend the Python functions or request further samples.**
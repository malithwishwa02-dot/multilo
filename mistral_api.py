import requests

def ask_mistral(prompt, api_key):
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "model": "mistral-medium-latest",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
        "temperature": 1.0
    }
    resp = requests.post(
        "https://api.mistral.ai/v1/chat/completions",
        headers=headers,
        json=data,
        timeout=30
    )
    return resp.json()["choices"][0]["message"]["content"] if resp.ok else resp.text
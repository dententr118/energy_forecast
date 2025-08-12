import requests
from config import API_KEY, BASE_URL

try:
    response = requests.get(
        f"{BASE_URL}carbon-intensity/latest?zone=SE",
        headers={
            "auth-token": f"{API_KEY}"
        }
    )
    response.raise_for_status()
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")


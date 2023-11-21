import requests
from dotenv import load_dotenv
load_dotenv()
import os

def pin_file_to_ipfs(filepath):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    # Ensure the file has a .log extension
    if not filepath.endswith('.log'):
        raise ValueError("Invalid file type. Only .log files are supported.")
    
    # Retrieve JWT bearer token from environment variable
    bearer_token = os.environ.get("YOUR_JWT_BEARER_TOKEN")

    if not bearer_token:
        raise ValueError("JWT bearer token not found in the environment variables.")

    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {bearer_token}"
    }

    files = {"file": (os.path.basename(filepath), open(filepath, "rb"), "text/plain")}

    response = requests.post(url, files=files, headers=headers)
    print(response)

    # Check if the request was successful
    response.raise_for_status()

    # Parse and return the IpfsHash from the response
    ipfs_hash = response.json().get("IpfsHash")
    return ipfs_hash


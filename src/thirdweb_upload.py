from thirdweb import ThirdwebSDK
from thirdweb.types import SDKOptions
import os
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file

SECRET_KEY = os.environ.get("3RDWEB_TOKEN")


async def upload_data(data):
    sdk = ThirdwebSDK("mumbai", options=SDKOptions(secret_key=SECRET_KEY))
    return sdk.storage.upload(data)

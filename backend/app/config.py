import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG", "False") == "True"
API_KEY = os.getenv("GOOGLE_API_KEY", "")
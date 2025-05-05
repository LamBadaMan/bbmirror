import os
from dotenv import load_dotenv

load_dotenv()

GIE_KEY = os.getenv("GIE_KEY")

if not GIE_KEY:
    raise ValueError("GIE_KEY environment variable is not set.")
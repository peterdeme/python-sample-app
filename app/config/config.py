import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv(".env", override=False)


def get(key: str, default: Optional[str] = None) -> str:
    return os.getenv(key, default)

from __future__ import annotations

import os
import secrets
import time

import jwt

DEFAULT_TOKEN_SECRET_KEY = (
    "7f-j&CKk=coNzZc0y7_4obMP?#TfcYq%fcD0mDpenW2nc!lfGoZ|d?f&RNbDHUX6HIDROWEBBACK"
)


def generate_token(expires_in: int = 60) -> str:
    """Generate a short-lived Hidroweb bearer token."""
    payload = {
        "sub": str(secrets.randbelow(1_000_000)),
        "iss": "HidroWeb-Front",
        "permissions": ["read", "write"],
        "exp": int(time.time()) + expires_in,
    }
    secret_key = os.getenv("PHYDRO_TOKEN_SECRET_KEY") or os.getenv(
        "HIDROWEB_TOKEN_SECRET_KEY",
        DEFAULT_TOKEN_SECRET_KEY,
    )

    return jwt.encode(payload, secret_key, algorithm="HS256")


def get_headers() -> dict[str, str]:
    """Build request headers expected by Hidroweb."""
    token = f"Bearer {generate_token()}"
    return {
        "Authorization": token,
        "Content-Type": "application/x-www-form-urlencoded",
        "HidroWeb-Front": token,
    }

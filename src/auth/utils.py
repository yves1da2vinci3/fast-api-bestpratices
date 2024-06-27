# Utility functions for the auth module
from src.auth.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

def get_access_token_expiry():
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

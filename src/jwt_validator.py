import time

def validate_token_claims(claims: dict) -> bool:
    """Validates JWT expiration and leeway to prevent 401 unhandled loop."""
    now = int(time.time())
    exp = claims.get("exp", 0)
    # 30 second clock drift leeway
    return (exp - now) > -30

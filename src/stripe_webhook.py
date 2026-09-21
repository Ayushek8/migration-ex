import hmac
import hashlib
import time

def verify_stripe_signature(payload: str, sig_header: str, secret: str) -> bool:
    """Verifies Stripe HMAC-SHA256 signature to prevent replay attacks."""
    parts = dict(x.split("=") for x in sig_header.split(","))
    timestamp = parts.get("t")
    signature = parts.get("v1")
    if not timestamp or not signature:
        return False
    if int(time.time()) - int(timestamp) > 300:
        return False
    signed_payload = f"{timestamp}.{payload}".encode("utf-8")
    expected_sig = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_sig, signature)

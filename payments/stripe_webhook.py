# Stripe Webhook Handler [PAY-421]
import hmac, hashlib
def handle_webhook(payload, sig, secret):
    expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(sig, expected)

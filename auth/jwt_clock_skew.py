# JWT Clock Skew Fix [AUTH-108]
import time
def is_token_valid(exp_timestamp, leeway=60):
    return time.time() < (exp_timestamp + leeway)

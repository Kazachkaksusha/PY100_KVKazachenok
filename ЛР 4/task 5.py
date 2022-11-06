import string
import random

def get_random_password(n) -> str:
    chars = string.digits + string.ascii_lowercase + string.ascii_uppercase
    return "".join(random.sample(chars, n))


print(get_random_password(8))

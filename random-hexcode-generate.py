import random

def generate_random_hex_code():
    hex_code = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))
    return hex_code

# Generate a random hex code
random_hex_code = generate_random_hex_code()
print(random_hex_code)
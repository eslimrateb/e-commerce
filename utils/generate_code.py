import random

def generate_code(length=8):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    code = ''.join(random.choice(characters) for _ in range(length))
    return code
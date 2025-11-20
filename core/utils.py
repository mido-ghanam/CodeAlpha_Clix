import random, string

def generate_code(length=8, use_letters=False, use_mixed_case=False, exclude_similar=False):
  if use_letters:
    if use_mixed_case: characters = string.ascii_letters + string.digits
    else: characters = string.ascii_lowercase + string.digits
  else: characters = string.digits
  if exclude_similar: 
    similar_chars = '0Oo1lI'
    characters = ''.join(c for c in characters if c not in similar_chars)
  return ''.join(random.choice(characters) for _ in range(length))

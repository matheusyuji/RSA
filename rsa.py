from sympy import isprime, mod_inverse

# Retorna uma lista de números primos abaixo do limite especificado
def find_primes_below(limit):
  primes = []
  for num in range(2, limit):
    if isprime(num):
      primes.append(num)
  return primes

# Fatora n em dois números primos p e q
def factor_n(n, primes):
  for p in primes:
    if n % p == 0:
      q = n // p
      if isprime(q):
        return p, q
  return None, None

# Calcula a chave privada d a partir da chave pública (e, n)
def calculate_private_key(e, n):

  primes = find_primes_below(1024)
  p, q = factor_n(n, primes)
  
  if p is None or q is None:
    raise ValueError("Não foi possível fatorar n em dois primos.")
  
  # Calcula φ(n)
  phi_n = (p - 1) * (q - 1)
  
  # Calcula d
  d = mod_inverse(e, phi_n)
  
  return d, p, q

# Criptografa cada caractere de uma string e retorna a lista de cifras
def encrypt(message, e, n):
  encrypted_chars = []
    
  # Criptografa cada caractere
  for char in message:
    m = ord(char)  # Converte o caractere para seu valor inteiro (ASCII)
    c = pow(m, e, n)  # Criptografa o caractere
    encrypted_chars.append(c)  # Adiciona o texto cifrado à lista
    
  return encrypted_chars

# Descriptografa cada caractere de uma lista de cifras e retorna a string original
def decrypt(encrypted_chars, d, n):
  decrypted_chars = []
    
  # Descriptografa cada caractere
  for c in encrypted_chars:
    m = pow(c, d, n)  # Descriptografa o caractere
    decrypted_chars.append(chr(m))  # Converte o valor inteiro de volta para caractere
    
  return ''.join(decrypted_chars)  # Junta os caracteres em uma string


try:
  # Lê n e e da entrada do usuário
  n = int(input("Digite o valor de n (módulo): "))
  e = int(input("Digite o valor de e (expoente público): "))
  
  d, p, q = calculate_private_key(e, n)
  print(f"Chave privada d: {d}")
  print(f"Primos p: {p}, q: {q}")

  original_message = input("Digite a mensagem a ser criptografada: ")
  print(f"Mensagem original: {original_message}")

  encrypted_message = encrypt(original_message, e, n)
  print(f"Mensagem criptografada: {encrypted_message}")

  decrypted_message = decrypt(encrypted_message, d, n)
  print(f"Mensagem descriptografada: {decrypted_message}")
except ValueError as ve:
  print(ve)
except Exception as ex:
  print(f"Ocorreu um erro: {ex}")
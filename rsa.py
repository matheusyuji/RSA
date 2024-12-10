from sympy import isprime, mod_inverse

# Retorna uma lista de números primos abaixo do limite especificado.
def find_primes_below(limit):
  primes = []
  for num in range(2, limit):
    if isprime(num):
      primes.append(num)
  return primes

# Fatora n em dois números primos p e q.
def factor_n(n, primes):
  for p in primes:
    if n % p == 0:
      q = n // p
      if isprime(q):
        return p, q
  return None, None

# Calcula a chave privada d a partir da chave pública (e, n).
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

try:
  # Lê n e e da entrada do usuário
  n = int(input("Digite o valor de n (módulo): "))
  e = int(input("Digite o valor de e (expoente público): "))
  
  d, p, q = calculate_private_key(e, n)
  print(f"Chave privada d: {d}")
  print(f"Primos p: {p}, q: {q}")
except ValueError as ve:
  print(ve)
except Exception as ex:
  print(f"Ocorreu um erro: {ex}")
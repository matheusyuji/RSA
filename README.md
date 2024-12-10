# RSA
Este programa implementa a criptografia RSA em Python. Ele permite que o usuário insira valores para `n` (módulo) e `e` (expoente público), calcula a chave privada `d`, e permite a criptografia e descriptografia de mensagens.

## Funcionalidades

- Fatoração de `n` em dois números primos `p` e `q`.
- Cálculo da chave privada `d` a partir da chave pública `(e, n)`.
- Criptografia de uma mensagem caractere por caractere.
- Descriptografia da mensagem criptografada.

## Funções Principais
``
* `find_primes_below(limit)`: Retorna uma lista de números primos abaixo do limite especificado.
* `factor_n(n, primes)`: Fatora `n` em dois números primos `p` e `q`.
* `calculate_private_key(e, n)`: Calcula a chave privada `d` a partir da chave pública `(e, n)`.
* `encrypt(message, e, n)`: Criptografa cada caractere de uma string e retorna a lista de cifras.
* `decrypt(encrypted_chars, d, n)`: Descriptografa cada caractere de uma lista de cifras e retorna a string original.

## Obsevações
* O programa assume que `n` é o produto de dois números primos e que `e` é um expoente público válido.
* A fatoração de `n` pode falhar se `n` não for um produto de dois primos ou se os primos forem muito grandes.

## Requisitos

- Python 3.x
- Biblioteca `sympy` para operações matemáticas (instalável via pip).

## Uso

1. Execute o programa:

```bash
python3 rsa.py
```

2. Quando solicitado, insira os valores de `n` e `e`:

```bash
Digite o valor de n (módulo): [seu valor]
Digite o valor de e (expoente público): [seu valor]
```

3. Em seguida, insira a mensagem que deseja criptografar:

```bash
Digite a mensagem a ser criptografada: [sua mensagem]
```

4. O programa exibirá a chave privada `d`, os primos `p` e `q`, a mensagem criptografada e a mensagem descriptografada.
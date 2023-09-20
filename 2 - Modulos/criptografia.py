import hashlib as crip

# QUAIS DISPONIVEIS
print (crip.algorithms_available)

# DISPONIVEIS DO SO

print (crip.algorithms_guaranteed)

# CRIPTOGRAFANDO EM SHA512

algoritmo = crip.sha512()
info = "dados a serem criptografados".encode()
algoritmo.update(info)
print (algoritmo.digest())
print(algoritmo.hexdigest())

algoritmo2 = crip.sha256()
algoritmo2.update(info)
print (algoritmo2.digest())
print(algoritmo2.hexdigest())
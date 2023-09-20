import json

pessoa = '{"nome": "Anakinpyt guerra", "linguagens": ["php", "python"]}'

dicionarioJson = json.dumps(pessoa)

print (dicionarioJson)
# print (dicionarioJson['linguagens'])
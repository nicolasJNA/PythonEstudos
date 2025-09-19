"""
Estudo de dicionario no paython
Conjunto não ordenado de pares chave e valor
"""
DicionarioTelefonico = {
    "nicolas":"8522-6530",
    "josue": "7455-2031",
    "franci":"87454-2136",
    "luana":"3265-9878"
    }
print(DicionarioTelefonico["franci"])
print(DicionarioTelefonico.keys()) #retorna as chaves
print(DicionarioTelefonico.values())
print(DicionarioTelefonico.pop("josue")) #retorna josue e deleta do dicio
print(DicionarioTelefonico.keys()) 

print(DicionarioTelefonico.get("luana")) #caso não tera chave retorna None
#print(DicionarioTelefonico["josue"]) #retorna Keyerror
print(DicionarioTelefonico.items())

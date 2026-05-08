# %% 
caderno = dict()

caderno["maça"] = 0.67
caderno["leite"] = 1.49
caderno["abacate"] = 1.49

print(caderno["abacate"])
# %%
lista_telefonica = {}

lista_telefonica["jenny"] = 8675309
lista_telefonica["emergencia"] = 190

print(lista_telefonica["jenny"])

# %%
votaram = {}

def verifica_eletior(nome):
    if votaram.get(nome):
        print("Mande embora")
    else:
        votaram[nome] = True
        print("Deixe votar")

# %%

# %%
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    
# %%
fat()

# %%
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total
print(soma([2,4,6]))
# %%
def conta(lista):
    count = 0
    for i in lista:
        count = i 
    return count

# %%
lista = [1,3,14,5,9]
print(conta(lista))

# %%
def maior_valor(lista):
    max = 0
    for i in lista:
        if i > max:
            max = i
    return max

# %%
print(maior_valor(lista))
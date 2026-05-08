# %%
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
print(quicksort([10,5,2,3]))

# %%
def imprime_itens(lista):
    for i in lista:
        print(i)

# %%
from time import sleep

def imprime_lista2(lista):
    for i in lista:
        sleep(1)
        print(i)

#%%
l = [2,4,6,8,10]
# %%
imprime_lista2(l)
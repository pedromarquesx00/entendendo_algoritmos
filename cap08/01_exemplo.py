# %%
estados_abranger = set(["mt","wa","or","id","nv","ut","ca","az"])

arr = [ 1,2,2,3,3,3]
set(arr)
set([1,2,3])

estacoes = {}
estacoes["kum"] = set(["id","nv","ut"])
estacoes["kdois"] = set(["wa","id","mt"])
estacoes["ktres"] = set(["or","nv","ca"])
estacoes["kquatro"] = set(["nv","ut"])
estacoes["kcinco"] = set(["ca","az"])

estacoes_final = set()


while estados_abranger:
    melhor_estacao = None
    estacoes_cobertos = set()

    for estacao, estacoes_por_estado in estacoes.items():
        cobertos = estados_abranger & estacoes_por_estado
        if len(cobertos) > len(estacoes_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos
            
    estados_abranger -= estados_cobertos
    estacoes_final.add(melhor_estacao)

print(estacoes_final)
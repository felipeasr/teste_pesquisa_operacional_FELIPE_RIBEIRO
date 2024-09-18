import pandas as pd

dados = pd.read_excel('Teste Pesquisa Operacional - Dados.xlsx')

dados.info()
#dados.Item.describe()
#dados.CaixaId.describe()
#dados.Peças.describe()

capacidade_maxima = 2000

# Agrupar os itens por caixas
caixas_agrupadas = dados.groupby('CaixaId')[['Item', 'Pecas']].apply(lambda x: list(zip(x['Item'], x['Pecas']))).to_dict()



ondas = []
caixas_nas_ondas = []


# (Restrição 5: somatório das peças <= 2000)
def pode_adicionar_caixa_na_onda(onda, itens_caixa):
    total_pecas = sum([pecas for _, pecas in onda])
    pecas_caixa = sum([pecas for _, pecas in itens_caixa])
    return (total_pecas + pecas_caixa) <= capacidade_maxima


for id_caixa, itens_caixa in caixas_agrupadas.items():
    caixa_alocada = False
    
    # (Restrição 3: só pode alocar se a onda existir)
    for id_onda, onda in enumerate(ondas):
        if pode_adicionar_caixa_na_onda(onda, itens_caixa): 
            onda.extend(itens_caixa)  # Aloca a caixa a essa onda (Restrição 2)
            caixas_nas_ondas.append({'CaixaId': id_caixa, 'OndaId': id_onda + 1})
            caixa_alocada = True
            break
    
    
    if not caixa_alocada:
        ondas.append(itens_caixa)  # Cria nova onda (Restrição 4)
        caixas_nas_ondas.append({'CaixaId': id_caixa, 'OndaId': len(ondas)})


df_resultado = pd.DataFrame(caixas_nas_ondas)
df_resultado.to_excel('atribuicao_caixas_nas_ondas.xlsx')

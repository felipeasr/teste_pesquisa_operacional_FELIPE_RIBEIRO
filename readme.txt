Link GIT: https://github.com/felipeasr/teste_pesquisa_operacional_FELIPE_RIBEIRO

# Felipe de Assis Ribeiro 
Problema: O objetivo é organizar caixas contendo itens em ondas de produção de forma que:

Cada caixa esteja em uma onda;
O número de ondas ativas seja minimizado;
Cada item apareça no menor número de ondas possível;
A soma das peças nas caixas atribuídas a uma onda não pode exceder 2000 peças.


Proposta de solução: Para a resolução do problema, foi utilizada a heurística gulosa (greedy). A cada iteração, o algoritmo tenta alocar uma caixa a uma onda já existente, respeitando o limite de 2000 peças por onda. Se não for possível alocar a caixa em nenhuma onda ativa, uma nova onda é criada.

Poderia ser utilizada a biblioteca PuLP, usada para modelagem de problemas de Programação Linear e Inteira (mas requer grande uso computacional). Com ela, é possível chegar a um modelo mais preciso para resolver o problema.


Para executar o código, basta instalar a biblioteca Pandas com:
!pip install pandas
Versão do Python utilizada: 3.12.5
e executar :
python pesquisaOperacional.py
ou executar no notebook pesquisaOperacional.ipynb
# pip install googlesearch-python
from googlesearch import search

# Texto da busca
query = 'Lon Hunter'

# faz a busca e cria os links com os resultados
result = list(
    search(
        query,
        lang= 'pt-br',
        num_results=7
    )
)


# Mostra os resultados
print(result)
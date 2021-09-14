# Estudo fastapi

## "Schema"
- A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

## Order matters
When creating path operations, you can find situations where you have a fixed path.

## Query parameters
Also notice that FastAPI is smart enough to notice that the path parameter item_id is a path parameter and q is not, so, it's a query parameter.

And of course, you can define some parameters as required, some as having a default value, and some entirely optional:

# String vslidations on query parameters
But we are now declaring it with Query, for example like:


q: Optional[str] = Query(None, min_length=3)
So, when you need to declare a value as required while using Query, you can use ... as the first argument:


# Estudo do modelo de oferta do Solidariedade

- Tabela Pedido/Oferta - podemos chamar só de ordem:
    - ID oferta/pedido
    - ID produto
    - ID Pesquisador Proprietário
    - ID histórico status

- Tabela Produto:
    - ID produto
    - Quantidade
    - Tipo
    - Data de validade

- Tabela Pesquisador:
    - ID pesquisador
    - Instituição
    - Nome pesquisador
    - email

- Lista histórico de status:
    - ID histórico
    - Criado (Pedido) timestamp
    - Atendido timestamp

# Pastas
- Serviço (regras de negocio)
- BD repositrios...

# Notas Meet 24/08 Equipe solidariedade
## apresentacao
- eles sao da TI da fcm
## Histórico

- Prof Gondijo entre a pos grad
na FCM na medicina
- Levou pra Capes.
- Foi pra Cleusa, mas quem são vcs?
- não é vendas.
- cada um q se vira como se faz a troca
- PPGs
- necessidades de informaticas da outras faculdades
- criar essa plataforma de troca de insumos

- Parceria com a Capes



## Geral
- Integrado ao Cafe de autenticação
- Abrigado na nuvem da Unicamp
- Mais pedidos do que ofertas

## symphony

## ideias
- colaborando com a comunidade
- pontuação da capes
- vencimento de insumos na fcm

- anotar numeros de interesses...

- Envio de emails pra labs candidatos

- a ordenação de distancia n é dita pro usuario

## Random
- Dev leader n veio

- lab multi usuario da capes
- agenda de qdo as pessoas podem usar um recurso


## Desafio
- As pessoas utilizarem, tem varios anos e ngm usa direito



# Q:
- Reunião com RNP?

- Como que a industria faz essas trocas?
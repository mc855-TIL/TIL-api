# Estudo fastapi

## "Schema"
- A "schema" is a definition or description of something. Not the code that implements it, but just an abstract description.

## Order matters
When creating path operations, you can find situations where you have a fixed path.

## Query parameters
Also notice that FastAPI is smart enough to notice that the path parameter item_id is a path parameter and q is not, so, it's a query parameter.

And of course, you can define some parameters as required, some as having a default value, and some entirely optional:

## String validations on query parameters
But we are now declaring it with Query, for example like:

## Path Parameters and Numeric Validations
With Query, Path (and others you haven't seen yet) you can declare metadata and string validations in the same ways as with Query Parameters and String Validations.

And you can also declare numeric validations:

- gt: greater than
- ge: greater than or equal
- lt: less than
- le: less than or equal

## Body - multiple parameters
You can add multiple body parameters to your path operation function, even though a request can only have a single body.

But FastAPI will handle it, give you the correct data in your function, and validate and document the correct schema in the path operation.

You can also declare singular values to be received as part of the body.

And you can instruct FastAPI to embed the body in a key even when there is only a single parameter declared.

## Body - Fields
You can use Pydantic's Field to declare extra validations and metadata for model attributes.

You can also use the extra keyword arguments to pass additional JSON Schema metadata.

## Nested models

you can also have arbitrarily nested models.

## Extra models
Here are some of the additional data types you can use:

- UUID:
A standard "Universally Unique Identifier", common as an ID in many databases and systems.
In requests and responses will be represented as a str.

- datetime.datetime:

## Headers
same logic of Cookie, Query and Path

## Response model
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)

## Extra models
Use multiple Pydantic models and inherit freely for each case.

You don't need to have a single data model per entity if that entity must be able to have different "states". As the case with the user "entity" with a state including password, password_hash and no password.

A Python datetime.datetime.
In requests and responses will be represented as a str in ISO 8601 format, like: 2008-09-15T15:53:00+05:00.


q: Optional[str] = Query(None, min_length=3)
So, when you need to declare a value as required while using Query, you can use ... as the first argument:

You can declare additional validations and metadata for your parameters.

Generic validations and metadata:

alias
title
description
deprecated
Validations specific for strings:

min_length
max_length
regex

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
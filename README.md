# TIL-api
## Descrição
API da Troca de Insumos de Laboratórios (TIL), um projeto da matéria mc855.

## Developers
Leandro Nascimento RA: 171855\
Leonardo Koike RA: 201332

## Depende
make\
python (versão 3.8 de preferência)\
pip
## Instalação
No diretório root desse projeto, basta executar os seguintes comandos:

```python
#criação e ativação da ambiente virtual
python -m venv mc855 & ./mc855/bin/activate
#instalar o gerenciador de pacotes poetry
pip install poetry
#instalar os pacotes
poetry install
```

## Execução
No seu prompt de comando ou terminal basta executar os seguintes comandos:

    export $(xargs <.env)\
    make run

E acessar no browser o host: [http://localhost:8000/docs](http://localhost:8000/docs)
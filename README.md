<div align="center">

# Master Learn Backend

[Instalação](#instalação) • [Configuração](#configuração) • [Executando](#executando) • [Tecnologias](#tecnologias)

![Python](https://img.shields.io/badge/Python-100%25-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)

</div>

---

### Sumário
- [Introdução](#introdução)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Executando](#executando)
- [Tecnologias](#tecnologias)

# Introdução

**Master Learn Backend** é uma API construída em **Python** com **FastAPI**, usando **SQLAlchemy** como ORM e **MySQL** como banco de dados.

# Pré-requisitos

- **Python 3** instalado;
- Um servidor **MySQL** acessível (local ou remoto).

# Instalação

Clone o repositório:

```sh
git clone https://github.com/cmarinho-dev/master-learn-backend.git
cd master-learn-backend
```

Crie e ative um ambiente virtual:

```sh
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

Instale as dependências:

```sh
pip install -r requirements.txt
```

# Configuração

Crie um arquivo `.env` na raiz do projeto com os dados de acesso ao seu banco MySQL:

```env
DB_NAME=nome-do-banco-de-dados
DB_USER=nomeusuario-do-banco
DB_PASSWORD=senhausuario-do-banco
DB_HOST=url-do-banco
DB_PORT=porta-do-banco
```

# Executando

Com o ambiente virtual ativo e o `.env` configurado, suba a API com o Uvicorn:

```sh
uvicorn src.main:app --reload
```

Por padrão, a documentação interativa da API (gerada automaticamente pelo FastAPI) fica disponível em `http://localhost:8000/docs`.

# Tecnologias

- **FastAPI** — framework web para construção da API;
- **Uvicorn** — servidor ASGI usado para rodar a aplicação;
- **SQLAlchemy** — ORM para acesso ao banco de dados;
- **PyMySQL** — driver de conexão com MySQL;
- **python-dotenv** — carregamento de variáveis de ambiente a partir do `.env`.

---

<div align="center">

Feito com FastAPI + SQLAlchemy.

</div>

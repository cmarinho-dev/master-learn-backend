### Como executar o projeto

1º Crie um ambiente com o venv
```bash
python -m venv .venv
```

2º Ative o venv
```bash
.\venv\Scripts\activate
```

3º Baixe as dependências
```bash
pip install -r requirements.txt
```

4º Configure o acesso ao banco <br>
Crie o arquivo `.env` na raíz do projeto e adicione os seguintes dados conforme seu banco MySQL
```env
DB_NAME=nome-do-banco-de-dados
DB_USER=nomeusuario-do-banco
DB_PASSWORD=senhausuario-do-banco
DB_HOST=url-do-banco
DB_PORT=porta-do-banco
``` 

5º Execute o projeto
```bash
uvicorn src.main:app --reload
```

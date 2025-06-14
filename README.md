# Body Measures Flask App

Web application built with flask, javascript, html and css for tracking body measurements.

## Estrutura do APP
* Config: inicialização de variáveis de ambiente
* Controllers: funções das rotas. Recebem a requisição, interagem com outros módulos e enviam a resposta
* Models: modelos criados com pydantic para validação e formatação de dados
* static: arquivos css e imagens
* templates: arquivos html

## Siga os passos abaixo para clonar e executar o projeto localmente:
* 1. Clone o repositório
```
git clone https://github.com/BernardoChamilet/body_measures_flask_app
cd body_measures_flask_app
```
* 2. Crie um ambiente virtual (opcional)
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
* 3. Instale as dependências
```
pip install -r requirements.txt
```
* 4. Crie um .env na raiz do projeto contendo
```
APIURL=url_da_api(body_measures_flask_api)
PORT=porta_do_app
DEBUG=True/False
```
* 5. Na raiz do projeto rode
```
python app.py
```

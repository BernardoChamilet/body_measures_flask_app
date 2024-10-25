from flask import Blueprint, redirect, request, render_template, make_response
import src.models.usuario as models
from pydantic import ValidationError
import requests
from src.config.config import apiurl

login_bp = Blueprint('login', __name__)

# Login
@login_bp.route("/")
@login_bp.route("/login", methods=['POST','GET'])
def login():
	# Envio do formulário
	if request.method == 'POST':
		# Obtendo dados enviados pelo formulário
		dados = request.form
		# Validando dados
		try:
			login = models.Login(**dados)
		except ValidationError:
			msgErro = "Preencha os campos corretamente"
			return render_template("login.html", msgErro=msgErro)
		loginDict = login.model_dump()
		# Fazendo requisição a API
		respostaAPI = requests.post(f'{apiurl}/login', json=loginDict)
		if respostaAPI.status_code == 200:
			# sucesso 200
			# Colocando token nos cookies do navegador
			token = respostaAPI.json().get('token')
			response = make_response(redirect("/inicio"))
			response.set_cookie('token', token, httponly=True, samesite='Strict')
			return response
		elif respostaAPI.status_code == 401:
			msgErro = "Usuário ou senha incorreto(os)"
			return render_template("login.html", msgErro=msgErro)
		elif respostaAPI.status_code == 400:
			msgErro = "Preencha os campos corretamente" #400
			return render_template("login.html", msgErro=msgErro)
		else:
			msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500
			return render_template("login.html", msgErro=msgErro)
	# Renderização da página de login
	if request.method == 'GET':
		return render_template("login.html")
	
# Logout
@login_bp.route("/sair", methods=['GET'])
def sair():
	response = redirect("/login")
    # Removendo o token do cookie configurando-o como vazio e com expiração no passado
	response.set_cookie('token', '', expires=0)
	return response
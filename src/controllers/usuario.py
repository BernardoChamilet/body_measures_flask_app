from flask import Blueprint, request, render_template
import src.models.usuario as models
from pydantic import ValidationError
import requests
from src.config.config import apiurl

usuario_bp = Blueprint('usuario', __name__)

# Cadastro de usuários
@usuario_bp.route("/cadastro", methods=['POST','GET'])
def cadastro():
	# Envio do formulário
	if request.method == 'POST':
		# Obtendo dados enviados pelo formulário
		dados = request.form
		# Validando dados
		try:
			usuario = models.Usuario(**dados)
		except ValidationError as e:
			msgErro = "Preencha os campos corretamente"
			return render_template("cadastro.html", msgErro=msgErro, dadosForm=dados)
		usuarioDict = usuario.model_dump()
		# Fazendo requisição a API
		respostaAPI = requests.post(f'{apiurl}/usuarios', json=usuarioDict)
		if respostaAPI.status_code == 201:
			# Sucesso 201
			return render_template("login.html",sucesso=True)
		elif respostaAPI.status_code == 409:
			msgErro = "Usuário já existe" #409
			return render_template("cadastro.html", msgErro=msgErro, dadosForm=dados)
		elif respostaAPI.status_code == 400:
			msgErro = "Preencha os campos corretamente" #400
			return render_template("cadastro.html", msgErro=msgErro, dadosForm=dados)
		else:
			msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500
			return render_template("cadastro.html", msgErro=msgErro, dadosForm=dados)
	# Renderização da página de cadastro
	if request.method == 'GET':
		return render_template("cadastro.html", dadosForm={})
from flask import Blueprint, request, render_template, redirect
import requests
from src.config.config import apiurl
import src.models.medida as models
from pydantic import ValidationError

medida_bp = Blueprint('medida', __name__)

# Início
@medida_bp.route("/inicio", methods=['GET'])
def inicio():
	# Renderização da página de início
	# Obtendo o token do cookie
	token = request.cookies.get('token')
	if not token:
		# Se o token não estiver presente, redirecionar para a página de login
		return redirect("/login")
	headers = {'Authorization': f'Bearer {token}'}
	# Fazendo requisição a API para buscar dados do usuário logado
	respostaAPI = requests.get(f'{apiurl}/usuarios/me', headers=headers)
	if respostaAPI.status_code == 200:
		nomeLogado = respostaAPI.json().get('nome')
	elif respostaAPI.status_code == 401:
		# Token faltando, inválido ou expirado
		return redirect("/login")
	else:
		msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500
		return render_template("login.html", msgErro=msgErro)
	# Fazendo requisição a API para buscar medidas do usuários
	respostaAPI = requests.get(f'{apiurl}/medidas', headers=headers)
	if respostaAPI.status_code == 200:
		medidas = respostaAPI.json()
	elif respostaAPI.status_code == 204:
		medidas = []
	elif respostaAPI.status_code == 401:
		# Token faltando, inválido ou expirado
		return redirect("/login")
	else:
		msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500
		return render_template("login.html", msgErro=msgErro)
	return render_template("inicio.html", nome=nomeLogado, medidas=medidas)

# Adição de medidas
@medida_bp.route("/inicio/adicionar", methods=['GET','POST'])
def adicao():
	# Obtendo o token do cookie
	token = request.cookies.get('token')
	if not token:
		# Se o token não estiver presente, redirecionar para a página de login
		return redirect("/login")
	# Envio do formulário
	if request.method == 'POST':
		#Obtendo dados enviados pelo formulário
		dados = request.form
		# Validando dados
		try:
			medida = models.Medida(**dados)
		except ValidationError:
			msgErro = "Preencha os campos corretamente"
			return render_template("adicionar.html",msgErro=msgErro)
		medidaDict = medida.model_dump()
		# Fazendo requisição a API para adcionar medidas
		headers = {'Authorization': f'Bearer {token}'}
		respostaAPI = requests.post(f'{apiurl}/medidas', json=medidaDict, headers=headers)
		if respostaAPI.status_code == 201:
			return render_template("adicionar.html",sucesso=True)
		elif respostaAPI.status_code == 400:
			msgErro = "Preencha os campos corretamente"
			return render_template("adicionar.html",msgErro=msgErro)
		else:
			msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500
			return render_template("adicionar.html",msgErro=msgErro)
	# Renderização da página de adição de medidas
	if request.method == 'GET':
		return render_template("adicionar.html")

# Exclusão de medidas
@medida_bp.route("/inicio/<id>", methods=['POST'])
def exclusao(id):
	# Obtendo o token do cookie
	token = request.cookies.get('token')
	if not token:
		# Se o token não estiver presente, redirecionar para a página de login
		return redirect("/login")
	# Chamando API para deletar medida
	headers = {'Authorization': f'Bearer {token}'}
	respostaAPI = requests.delete(f'{apiurl}/medidas/{id}', headers=headers)
	if respostaAPI.status_code == 200:
		return redirect("/inicio")
	else:
		print(respostaAPI.status_code, respostaAPI.json())
		return redirect("/inicio")

# Edição das medidas
@medida_bp.route("/inicio/editar/<id>", methods=['POST', 'GET'])
def edicao(id):
	# Obtendo o token do cookie
	token = request.cookies.get('token')
	if not token:
		# Se o token não estiver presente, redirecionar para a página de login
		return redirect("/login")	
	#return redirect("/inicio")
	# Envio do formulário
	if request.method == 'POST':
		#Obtendo dados enviados pelo formulário
		dados = request.form
		# Validando dados
		try:
			medida = models.Medida(**dados)
		except ValidationError:
			msgErro = "Preencha os campos corretamente"
			return render_template("editar.html",msgErro=msgErro)
		medidaDict = medida.model_dump()
		# Fazendo requisição a API para atualizar medida
		headers = {'Authorization': f'Bearer {token}'}
		respostaAPI = requests.put(f'{apiurl}/medidas/{id}', json=medidaDict, headers=headers)
		if respostaAPI.status_code == 204:
			return render_template("editar.html",sucesso=True)
		elif respostaAPI.status_code == 400:
			msgErro = "Preencha os campos corretamente"
			return render_template("editar.html",msgErro=msgErro)
		else:
			msgErro = "Ocorreu um erro em nosso servidor, tente novamente" #500, 403 ou 404
			return render_template("editar.html",msgErro=msgErro)
	# Renderização da página de edição de medidas
	if request.method == 'GET':
		# Fazendo requisição a API para atualizar medida
		headers = {'Authorization': f'Bearer {token}'}
		respostaAPI = requests.get(f'{apiurl}/medidas/{id}', headers=headers)
		if respostaAPI.status_code == 200:
			editadas = respostaAPI.json()
			return(render_template("editar.html", editado = editadas))
		else:
			print(respostaAPI.status_code, respostaAPI.json())
			return redirect("/inicio")
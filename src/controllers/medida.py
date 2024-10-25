from flask import Blueprint, request, render_template, redirect
import requests
from src.config.config import apiurl

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
	# Envio do formulário
	if request.method == 'POST':
		logado = "Fulano"
		#Obtendo dados enviados pelo formulário
		dados = request.form
		#data = request.form.get('data')
		#peso = request.form.get('peso')
		#ombro = request.form.get('ombro')
		#peito = request.form.get('peito')
		#braco = request.form.get('braco')
		#antebraco = request.form.get('antebraco')
		#cintura = request.form.get('cintura')
		#quadril = request.form.get('quadril')
		#coxa = request.form.get('coxa')
		#panturrilha = request.form.get('panturrilha')
		
		return render_template("adicionar.html",sucesso=True)
	# Renderização da página de adição de medidas
	if request.method == 'GET':
		return render_template("adicionar.html")

# Exclusão de medidas
@medida_bp.route("/inicio/<id>", methods=['POST'])
def exclusao(id):
	id = int(id)
	
    # Verificação se o usuário logado é o dono da medida
	
	return redirect("/inicio")


# Edição das medidas
@medida_bp.route("/inicio/editar/<id>", methods=['POST', 'GET'])
def edicao(id):
	# Verificação se o usuário logado é o dono da medida	
	#return redirect("/inicio")
	# Envio do formulário
	if request.method == 'POST':
		#Obtendo dados enviados pelo formulário
		dados = request.form
		#data = request.form.get('data')
        #peso = request.form.get('peso')
		#ombro = request.form.get('ombro')
		#peito = request.form.get('peito')
		#braco = request.form.get('braco')
		#antebraco = request.form.get('antebraco')
		#cintura = request.form.get('cintura')
		#quadril = request.form.get('quadril')
		#coxa = request.form.get('coxa')
		#panturrilha = request.form.get('panturrilha')
		
		return render_template("editar.html",sucesso=True)
	# Renderização da página de edição de medidas
	if request.method == 'GET':
		
		editadas = [0,1,2,3,4,5,6,7,8,9]
		return(render_template("editar.html", editado = editadas))
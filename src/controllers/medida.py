from flask import Blueprint, request, render_template, redirect

medida_bp = Blueprint('medida', __name__)

# Início
@medida_bp.route("/inicio", methods=['GET'])
def inicio():
	# Renderização da página de início
	nomeLogado = 'Fulano'
	medidas = [0,1,2,3,4,5,6,7,8,9]
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
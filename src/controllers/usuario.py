from flask import Blueprint, request, render_template

usuario_bp = Blueprint('usuario', __name__)

# Cadastro de usuários
@usuario_bp.route("/cadastro", methods=['POST','GET'])
def cadastro():
	# Envio do formulário
	if request.method == 'POST':
		# Obtendo dados enviados pelo formulário
		dados = request.form
		#usuario = request.form.get('usuario')
		#nome = request.form.get('nome')
		#senha = request.form.get('senha')
		#confirma = request.form.get('confirma')
		
        # Fracasso
		msgErro = "Senhas não coincidem"
		msgErro = "Usuário já existe"
		return render_template("cadastro.html", msgErro=msgErro, dadosForm=dados)
		
        # Sucesso
		return render_template("login.html",sucesso=True)
	# Renderização da página de cadastro
	if request.method == 'GET':
		return render_template("cadastro.html", dadosForm={})
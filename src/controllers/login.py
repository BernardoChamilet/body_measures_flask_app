from flask import Blueprint, redirect, request, render_template

login_bp = Blueprint('login', __name__)

# Login
@login_bp.route("/")
@login_bp.route("/login", methods=['POST','GET'])
def login():
	# Envio do formulário
	if request.method == 'POST':
		# Obtendo dados enviados pelo formulário
		dados = request.form
		#usuario = request.form.get('usuario')
		#senha = request.form.get('senha')
		
		# fracasso
		msgErro = "Usuário ou senha incorreto(os)"
		return render_template("login.html", msgErro=msgErro)
		
		# sucesso
		return redirect("/inicio")
	# Renderização da página de login
	if request.method == 'GET':
		return render_template("login.html")
	
# Logout
@login_bp.route("/sair")
def sair():
	# Lógica de logout
	return redirect("/login")
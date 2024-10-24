from flask import Flask
from src.config.config import port, debug

app = Flask(__name__)

# Carregando variáveis de ambiente
app.config['DEBUG'] = debug
app.config['PORT'] = port

# Adcionando rotas
from src.controllers.login import login_bp
app.register_blueprint(login_bp)

from src.controllers.usuario import usuario_bp
app.register_blueprint(usuario_bp)

from src.controllers.medida import medida_bp
app.register_blueprint(medida_bp)

if __name__ == "__main__":
	app.run()
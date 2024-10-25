from dotenv import load_dotenv
import os
from pathlib import Path

# Caminho absoluto até o diretório principal onde o .env está localizado
env_path = Path(__file__).resolve().parent.parent.parent / '.env'

# Carregando variáveis de ambiente
load_dotenv(dotenv_path=env_path)

port = int(os.getenv('PORT'))

debug = bool(os.getenv('DEBUG'))

apiurl = os.getenv('APIURL')
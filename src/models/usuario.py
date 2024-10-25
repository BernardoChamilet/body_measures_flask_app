from pydantic import BaseModel, Field, model_validator

# Classe para validação de dados de usuário 
class Usuario(BaseModel):
    usuario: str = Field(..., min_length=7)
    nome: str = Field(..., min_length=2)
    senha: str = Field(..., min_length=6)
    confirma: str = Field(..., min_length=6)

    @model_validator(mode='after')
    def verificaSenhas(cls, values):
        if values.senha != values.confirma:
            raise ValueError('As senhas não são iguais')
        return values

# Classe para validação de campos no login
class Login(BaseModel):
    usuario: str
    senha: str
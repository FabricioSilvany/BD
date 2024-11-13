from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.database import db

#Base para criar tabelas no banco de dados.
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, Primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    #Definindo características da classe.
    def __init__(self, nome:str, email:str, senha:str):
        self.nome = nome
        self.senha = senha
        self.email = email

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
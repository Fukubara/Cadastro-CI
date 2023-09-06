import json
from sqlalchemy.orm import Session
from sqlalchemy import select, create_engine
from flask import Flask
from flask_cors import CORS
from flask import request

import jwt
import Server.Models as Models

app = Flask(__name__)
CORS(app)

engine = create_engine("postgresql://Administrador:1qaz!WSX@localhost:5432/Logins", echo=True)


@app.route("/")
def index():
    pass

@app.route("/cadastro")
def register():

    with Session(engine) as session:
        usu = Models.User(
            login="teste",
            senha="1234"
        )

        session.add_all([usu])

        session.commit()

@app.route("/login", methods=["POST"])
def login():
    with Session(engine) as session:
        user = session.query(Models.User).where(Models.User.login == json.loads(request.data)['login']).first()
        if (json.loads(request.data)['senha'] == user.senha):
            return jwt.encode({"status":"logado", "mensagem": "Seja bem vindo à Criptografia"}, "secret", algorithm="HS256")

            
@app.route("/cadastrarPessoa", methods=["POST"])
def cadastrarPessoa():
    req = json.loads(request.data)

    pessoa = Models.Pessoa(req)

    with Session(engine) as session:
        session.add_all([pessoa])

        session.commit()

@app.route("/listarPessoas", methods=["GET"])
def listarPessoas():
    with Session(engine) as session:
        sql = select(Models.Pessoa)
        result = session.scalars(sql)
    return result
from app import app, db
from flask import request, render_template, jsonify, session
from werkzeug.security import check_password_hash
from app.models import Usuario

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        json = request.form
        email = json.get("email")

        if email:
            usuario = db.session.execute(db.select(Usuario).filter_by(email=email)).scalar_one()

            if usuario:
                senha = json.get("senha")
                if check_password_hash(usuario.senha, senha):
                    session["email"] = usuario.email
                    return jsonify(sucesso=True)

        return jsonify(sucesso=False)
    return render_template("home.html")


@app.route("/perfil", methods=['GET'])
def perfil():
    email = session["email"]
    usuario = db.session.execute(db.select(Usuario).filter_by(email=email)).scalar_one()

    return render_template("perfil.html", usuario=usuario)


@app.route("/novo-usuario", methods=['GET', 'POST'])
def novo_usuario():
    if request.method == 'POST':
        json = request.form

        usuario = Usuario(json)

        if usuario.usuario_valido():
            db.session.add(usuario)
            db.session.commit()
            return jsonify(msg="Usuario cadastrado com sucesso!", sucesso=True)

        return jsonify(msg="Não foi possivel validar o usuario", sucesso=False)

    return render_template("novo_usuario.html")


@app.route("/usuarios", methods=['GET'])
def mostra_usuarios():
    usuarios = db.session.execute(db.select(Usuario).order_by(Usuario.nome_usuario)).scalars()
    lista_usuarios = []
    cont = 1

    for usuario in usuarios:
        lista_usuarios.append(usuario.to_json(cont))
        cont += 1

    return render_template("mostra_usuario.html", usuarios=lista_usuarios)


@app.route("/editar", methods=['PUT'])
def editar():
    json = request.json

    email = session["email"]
    usuario = db.session.execute(db.select(Usuario).filter_by(email=email)).scalar_one()
    nome = json.get("usuario")
    email = json.get("email")

    if nome and email:
        usuario.nome_usuario = nome
        usuario.email = email

        db.session.commit()
        session["email"] = email
        return jsonify(sucesso=True)

    return jsonify(sucesso=False)


@app.route("/excluir_usuario/<int:id>", methods=['DELETE'])
def excluir_usuario(id):
    usuario = db.session.execute(db.select(Usuario).filter_by(id=id)).scalar_one()

    if usuario:
        db.session.delete(usuario)
        db.session.commit()

        return jsonify(sucesso=True)

    return jsonify(sucesso=False)

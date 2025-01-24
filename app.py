from flask import Flask, request, jsonify, render_template, redirect
from mysql import connector

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        id = request.form.get("id")
        cliente = request.form.get("cliente")
        cpf = request.form.get("cpf")
        rua = request.form.get("rua")
        bairro = request.form.get("bairro")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")
        contato = request.form.get("contato")

        conect = connector.connect(
            host = "localhost",
            database = "cadastro_tube",
            user = "root",
            password = "382536"
        )

        cursor = conect.cursor()

        dados = (
            id, cliente, cpf, rua, bairro, cidade, uf, contato
        )

        query = """
            insert into cadastro (id, cliente, cpf, rua, bairro, cidade, uf, contato) values (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, dados)

        conect.commit()

        cursor.close()
        conect.close()

        

        return redirect(("/"))
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
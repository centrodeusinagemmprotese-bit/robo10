from flask import Flask, render_template, request
from robot import RegraLance, proximo_lance

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sugestao = None
    if request.method == "POST":
        melhor = float(request.form["melhor"])
        minha = float(request.form["minha"])
        minutos = int(request.form["minutos"])

        regra = RegraLance(
            decremento_min=0.006, tipo_decremento="percentual",
            preco_minimo=9000.00, passo_minimo=5.00,
            janela_final_min=5, agressividade=0.7
        )
        sugestao = proximo_lance(melhor, minha, regra, minutos)

    return render_template("index.html", sugestao=sugestao)

if __name__ == "__main__":
    app.run(debug=True)

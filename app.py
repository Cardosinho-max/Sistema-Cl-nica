from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        paciente = request.form.get("paciente")
        tipo_exame = request.form.get("tipo_exame")
        observacoes = request.form.get("observacoes")
        
        return render_template(
            "index.html",
            paciente=paciente,
            tipo_exame=tipo_exame,
            observacoes=observacoes
        )
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
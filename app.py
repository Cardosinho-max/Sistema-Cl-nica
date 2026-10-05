from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/gerar', methods=['POST'])
def gerar_laudo():
    paciente = request.form.get('paciente')
    idade = request.form.get('idade')
    
    # Captura a natureza do exame (apenas 1 opção)
    natureza = request.form.get('natureza')
    
    # Captura todos os exames marcados
    lista_exames = request.form.getlist('exame')
    exame_texto = ", ".join(lista_exames) if lista_exames else "Nenhum exame selecionado"
    
    conclusao = request.form.get('conclusao')
    
    return render_template(
        'laudo.html', 
        paciente=paciente, 
        idade=idade, 
        natureza=natureza,
        exame=exame_texto, 
        lista_exames=lista_exames, 
        conclusao=conclusao
    )

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
jogo1 = Jogo("Super Mario", 'Açao', 'SNES')
jogo2 = Jogo("Pokemom Gold", 'RPG', 'GBA')
jogo3 = Jogo("Mortal Kombat", 'Luta', 'SNES')
jogo4 = Jogo("Elder Ring", 'RPG', 'PS4')
    
lista =[jogo1, jogo2, jogo3, jogo4]

@app.route('/')
def inicio():
    return render_template('index.html', 
                           titulo='Jogos',
                           jogos = lista)
@app.route('/novo')
def novo_jogo():
    return render_template('novo.html')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
    
lista =[]

# primeira rota do site, vai puxar um html 
# em titulos vai setar no arquivo index a string
# em jogos = lista vai pegar as informações da lista e
# plotar dentro do arquivo index
@app.route('/')
def inicio():
    return render_template('index.html', 
                           titulo='Jogos',
                           jogos = lista)

# arquivo de cadastros, vai abrir tela de cadastros
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

# rota de login da nossa aplicação

@app.route('/login')
def login():
    return render_template('login.html')
app.run(debug=True)
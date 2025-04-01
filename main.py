from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'teste'

class Jogo():
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console
class Usuario():
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha   

usuario1 = Usuario(1, 'Lucas', '123')
usuario2 = Usuario(2, 'Lucas', '123')     
usuario3 = Usuario(3, 'Lucas', '123')   
lista =[]
434-435

# primeira rota do site, vai puxar um html 
# em titulos vai setar no arquivo index a string
# em jogos = lista vai pegar as informações da lista e
# plotar dentro do arquivo index
@app.route('/')
def inicio():
    return render_template('index.html', 
                           titulo='Jogos',
                           jogos = lista,
                           title_head="Lista de Jogos")

# arquivo de cadastros, vai abrir tela de cadastros
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html',
                            title="Cadastro de jogos",
                            title_head="Cadastro")

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('inicio'))

# rota de login da nossa aplicação

@app.route('/login')
def login():
    proxima = request.args.get("proxima")
    return render_template('login.html', proxima=proxima,
                           title_head="Login")

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '123' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' Logado com sucesso')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Senha ou usuario errado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario deslogado')
    return redirect(url_for('inicio'))
app.run(debug=True)
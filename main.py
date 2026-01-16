from flask import Flask, render_template

app = Flask(__name__)



@app.route('/inicio')
def home():
    return render_template('lista.html', titulo="Jogos", inicio="lista de jogos")

# 421

if __name__ == '__main__':
    app.run(debug=True)

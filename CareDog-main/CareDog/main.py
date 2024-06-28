from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import os
import os
import ast
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'edua@123!'

logado = False

#Rota da pagina inicial
@app.route('/')
def home():
    return render_template('index.html')

#Rota de loginPagina
@app.route('/loginPagina', methods=['POST'])
def loginPagina():
    print('ROTA: loginPagina')
    return render_template('login.html')

#Rota de CadastroPagina
@app.route('/CadastroPagina', methods=['POST'])
def CadastroPagina():
    print('ROTA: CadastroPagina')
    return render_template('Cadastro.html')


#Rota de loginUsuario
@app.route('/login', methods=['POST'])
def login():
    print('ROTA: Login')
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    print(f"NOME: {nome}")
    print(f"SENHA: {senha}")
    return redirect('/perfil')

@app.route('/perfil')
def perfil():
    return render_template('perfilPasseador.html')

@app.route('/CadastrarUsuario', methods=['POST'])
def CadastrarUsuario():
    return render_template('tutor_cadastro.html')

if __name__ in "__main__":
    app.run(debug=True)
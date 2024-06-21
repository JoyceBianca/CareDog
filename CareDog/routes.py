#Routes.py
from flask import Flask, render_template, redirect, request, flash, send_from_directory
from __init__ import app
import os
import ast
import mysql.connector

logado = False

#Rota da pagina inicial
@app.route('/')
def home():
    return render_template('index.html')

#Rota de loginPagina
@app.route('/loginRota')
def loginEntrar():
    print('ROTA: loginEntrar')
    return render_template('login.html')


#Rota de loginUsuario
@app.route('/loginUsuario')
def login():
    nome = request.args.get('nome')
    senha = request.args.get('senha')

    print(f"NOME: {nome}")
    print(f"SENHA: {senha}")
    return flash('Login realizado sucesso"')
from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import os
import os
import ast
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Caredog123'

logado = False

#Rota da pagina inicial
@app.route('/')
def home():
    global logado
    logado = False
    return render_template('login.html')

if __name__ in "__main__":
    app.run(debug=True)
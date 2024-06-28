from flask import Flask, render_template, redirect, request, flash, send_from_directory, session
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

#Rota de Cadastroinicial
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


@app.route('/CadastroAvancado', methods=['POST'])
def CadastroAvancado():

    #Trazendo as vavriaveis das sessoes para variaveis dessa funcao
    nome = session.get('nome')
    senha = session.get('senha')
    email = request.form.get('email')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    genero = request.form.get('gender') #é o que tem opcao, testar er se funciona
    cep = request.form.get('cep')
    logradouro = request.form.get('logradouro')
    numeroCasa = request.form.get('numeroCasa')
    complemento = request.form.get('complemento')

    print("ROTA: CadastroAvancado\n")
    print('NOME: ', nome)
    print('SENHA: ', senha)
    print('EMAIL: ', email)
    print('CPF: ', cpf)
    print('TELEFONE: ', telefone)
    print('GENERO: ', genero)
    print('CEP: ', cep)
    print('LOGRGADOURO: ', logradouro)
    print('NUMERO CASA: ', numeroCasa)
    print('COMPLEMENTO: ', complemento)

    try: #Bloco try: O código que pode potencialmente gerar uma exceção é colocado dentro do bloco try. Se uma exceção ocorrer em qualquer lugar dentro do bloco try, o fluxo de execução é imediatamente interrompido e a execução passa para o bloco except.
        connect_BD = mysql.connector.connect(
            host='localhost',
            database='usuarios',
            user='root',
            password='edua@123!'
        )

        if connect_BD.is_connected():
            print('CONECTADO PARA CADASTRO!')
            cursor = connect_BD.cursor()
            #Persistindo do tutor os dados no banco
            cursor.execute(f"INSERT INTO usuario (nome, senha, email, cpf, telefone, genero, cep, logradouro, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nome, senha)) #Uso de parâmetros SQL: Utiliza parâmetros (%s) para inserir valores no SQL, o que ajuda a prevenir ataques de injeção SQL.
            connect_BD.commit()  #Confirmando a alteração
            cursor.close()
            flash(f'{nome} CADASTRADO COM SUCESSO!!')
        else:
            flash('Não foi possível conectar ao banco de dados')

    except mysql.connector.Error as err: #Bloco except: O código dentro do bloco except é executado se uma exceção ocorrer no bloco try. Você pode capturar tipos específicos de exceções ou usar um except genérico para capturar todas as exceções.
        print(f"Erro: {err}")
        flash(f"Erro ao cadastrar usuário: {err}")
    
    finally: #Bloco finally: O código dentro do bloco finally é sempre executado, independentemente de uma exceção ter sido lançada ou não. O bloco finally é comumente usado para liberar recursos, como fechar arquivos ou conexões de banco de dados, garantindo que esses recursos sejam liberados de maneira ordenada.
        if connect_BD.is_connected():
            connect_BD.close()

    return render_template('tutor_cadastro.html')


@app.route('/CadastroInicial', methods=['POST'])
def CadastrarUsuario():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    print("ROTA: CadastroInicial")
    print("NOME: ", nome)
    print("SENHA: ", senha)

     #Armazenando variáveis na sessão
    session['nome'] = nome
    session['senha'] = senha

    return render_template('tutor_cadastro.html')



if __name__ in "__main__":
    app.run(debug=True)
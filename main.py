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
    global logado
    logado = False
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

@app.route('/PerfilPasseador')
def PerfilPasseador():
    global logado
    if logado == True:
        return render_template('perfilPasseador.html')
    elif logado == False:
        return('/')


#Rota de loginUsuario
@app.route('/login', methods=['POST'])
def login():
    global logado

    print('ROTA: Login')
    nome = request.form.get('nome')
    senha = request.form.get('senha')

    print(f"NOME: {nome}")
    print(f"SENHA: {senha}")

    try: #Estrutura try-except-finallyEstrutura try-except-finally
        connect_BD = mysql.connector.connect(
            host='localhost',
            database='CareDog_Usuarios',
            user='root',
            password='edua@123!'
        )

        if connect_BD.is_connected():
            print('CONECTADO!')
            cursor = connect_BD.cursor()
            cursor.execute("select * from tutor;")
            usuariosBD = cursor.fetchall()
        
            #Verificando login
            cont = 0
            for usuario in usuariosBD:
                usuarioNome = str(usuario[1]) #Pegando o segundo elemento da linha da tabela sql que é o nome
                usuarioSenha = str(usuario[2]) 

                cont+=1
                if usuarioNome == nome and usuarioSenha == senha:
                    logado = True
                    return redirect('/PerfilPasseador')
                
                if cont >= len(usuariosBD):
                    flash('USUARIO INVALIDO')
                    print('USUARIO INVALIDO')
                    return render_template('login.html')
            
        else:
            render_template('login.html')

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        flash(f"Erro ao tentar fazer login: {err}")
        return render_template('login.html')
    
    finally:
        if connect_BD.is_connected():
            cursor.close()
            connect_BD.close()


@app.route('/CadastroAvancado', methods=['POST'])
def CadastroAvancado():

    # Dados do Tutor
    # Trazendo as vavriaveis das sessoes para variaveis dessa funcao
    nomeUsuario = session.get('nome')
    senha = session.get('senha')
    PrimeiroNome = str(request.form.get('PrimeiroNome'))
    SegundoNome = str(request.form.get('SegundoNome'))
    nomeCompleto = str(PrimeiroNome + " " + SegundoNome)
    email = request.form.get('email')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')
    genero = request.form.get('gender')
    cep = request.form.get('cep')
    logradouro = request.form.get('logradouro')
    numeroCasa = request.form.get('numeroCasa')
    complemento = request.form.get('complemento')


    # Dados do Cao
    nomeCao = request.form.get('nomeCao')
    raca = request.form.get('raca')
    idadeCao = int(request.form.get('idadeCao'))
    temperamento = request.form.get('temperamento')
    cuidadosEsp = request.form.get('cuidadosEspeciais')

    print("\n\nROTA: CadastroAvancado\n")

    print('DADOS DO TUTOR:')
    print('NOME USUARIO: ', nomeUsuario)
    print('SENHA: ', senha)
    print('NOME COMPLETO: ', nomeCompleto)
    print('EMAIL: ', email)
    print('CPF: ', cpf)
    print('TELEFONE: ', telefone)
    print('GENERO: ', genero)
    print('CEP: ', cep)
    print('LOGRGADOURO: ', logradouro)
    print('NUMERO CASA: ', numeroCasa)
    print('COMPLEMENTO: ', complemento)
    print('-------------------')
    print('DADOS DO CAO')
    print('NOME: ', nomeCao)
    print('RACA: ', raca)
    print('IDADE: ', idadeCao)
    print('TEMPERAMENTO: ', temperamento)
    print('CUIDADOS ESPECIAIS: ', cuidadosEsp)
    print('\n\n')



    try: #Bloco try: O código que pode potencialmente gerar uma exceção é colocado dentro do bloco try. Se uma exceção ocorrer em qualquer lugar dentro do bloco try, o fluxo de execução é imediatamente interrompido e a execução passa para o bloco except.
        connect_BD = mysql.connector.connect(
            host='localhost',
            database='CareDog_Usuarios',
            user='root',
            password='edua@123!'
        )

        if connect_BD.is_connected():
            print('CONECTADO PARA CADASTRO!')
            cursor = connect_BD.cursor()
            #Persistindo do tutor os dados no banco
            cursor.execute(
                "INSERT INTO tutor (nomeUsuario, senha, nomeCompleto, email, cpf, telefone, genero, cep, logradouro, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (nomeUsuario, senha, nomeCompleto, email, cpf, telefone, genero, cep, logradouro, numeroCasa, complemento)
            )
            cursor.execute(
                "INSERT INTO cao (nome, temperamento, raca, idade, cuidados_especiais) VALUES (%s, %s, %s, %s, %s)",
                (nomeCao, temperamento, raca, idadeCao, cuidadosEsp)
            )
            connect_BD.commit()
            cursor.close()
            flash(f'{nomeUsuario} CADASTRADO COM SUCESSO!!')
            print(f'{nomeUsuario} CADASTRADO COM SUCESSO!!')
        else:
            flash('Não foi possível conectar ao banco de dados')
            print('Não foi possível conectar ao banco de dados')

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
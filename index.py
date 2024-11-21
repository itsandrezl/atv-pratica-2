from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_banco(atividade):
 return sqlite3.connect('atividade')

# Página inicial
@app.route('/')
def inicio():
 return render_template('inicio.html')

# Página para cadastro de clientes
@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
 if request.method == 'POST':
  nome = request.form['nome']
  cpf = request.form['cpf']
  email = request.form['email']
  telefone = request.form['telefone']
  
  # Conecta ao banco e insere os dados
  with conectar_banco() as conn:
   conn.execute("INSERT INTO Clientes (NomeCompleto, CPF, Email, Telefone) VALUES (?, ?, ?, ?)", (nome, cpf, email, telefone))
   conn.commit()
  return "Cliente cadastrado com sucesso!"
 return render_template('clientes.html')

# Página para gerenciar solicitações
@app.route('/solicitacoes', methods=['GET', 'POST'])
def solicitacoes():
 if request.method == 'POST':
  descricao = request.form['descricao']
  urgencia = request.form['urgencia']
  cliente_id = request.form['cliente_id']
  
  # Conecta ao banco e registra a solicitação
  with conectar_banco() as conn:
   conn.execute("INSERT INTO Solicitacoes (IDCliente, Descricao, Urgencia, DataAbertura) VALUES (?, ?, ?, ?)", (cliente_id, descricao, urgencia, datetime.now()))
   conn.commit()
  return redirect('/solicitacoes')

 # Exibe a lista de solicitações
 with conectar_banco() as conn:
  solicitacoes = conn.execute("SELECT * FROM Solicitacoes").fetchall()
 return render_template('solicitacoes.html', solicitacoes=solicitacoes)

if __name__ == '__main__':
 app.run(debug=True)
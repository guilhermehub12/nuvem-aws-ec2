from flask import Flask
import mysql.connector

app = Flask(__name__)

css_style = '''
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        h1 {
            color: #333;
        }

        a {
            text-decoration: none;
            background-color: #007BFF;
            color: #fff;
            padding: 10px 20px;
            margin: 10px;
            border-radius: 5px;
            display: inline-block;
        }

        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
    </style>
'''

def consultar_alunos():
    # Conecta no banco
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='engajamente',
        charset='utf8'
    )
    cursor = conn.cursor()

    # Executa uma consulta no banco
    cursor.execute('SELECT * FROM alunos')
    resultados = cursor.fetchall()

    # Fecha a conexão com o banco
    conn.close()

    return resultados

def consultar_professores():
    # Conecta no banco
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='engajamente'
    )
    cursor = conn.cursor()

    # Executa uma consulta no banco
    cursor.execute('SELECT * FROM professores')
    resultados = cursor.fetchall()

    # Fecha a conexão com o banco
    conn.close()

    return resultados

@app.route('/')
def rota_padrao():
    return f'''<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Engajamente</title>
    <meta charset="utf-8">
    {css_style}
  </head>
  <body>
    <h1>Projeto EngajaMente</h1>
    <a href="/alunos">Mostrar Alunos</a>
    <a href="/professores">Mostrar Professores</a>
  </body>
</html>
'''

# Rota para mostrar os dados dos alunos
@app.route('/alunos')
def mostrar_dados_alunos():
    # Consulte o banco de dados
    resultados = consultar_alunos()

    # Converta os resultados em HTML
    html = f'''<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Alunos</title>
    <meta charset="utf-8">
    {css_style}
  </head>
  <body>
    <h1>Alunos:</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Matrícula</th>
            <th>Nome</th>
            <th>Idade</th>
            <th>Curso</th>
        </tr>
    '''
    for resultado in resultados:
        html += f'''
        <tr>
            <td>{resultado[0]}</td>
            <td>{resultado[1]}</td>
            <td>{resultado[2]}</td>
            <td>{resultado[3]}</td>
            <td>{resultado[4]}</td>
        </tr>
        '''
    html += '''
    </table>
    <a href="/">Voltar Início</a>
  </body>
</html>
'''
    return html

# Rota para mostrar os dados dos professores
@app.route('/professores')
def mostrar_dados_professores():
    # Consulte o banco de dados
    resultados = consultar_professores()

    # Converta os resultados em HTML
    html = f'''<!DOCTYPE html>
<html lang="pt-br">
  <head>
    <title>Professores</title>
    <meta charset="utf-8">
    {css_style}
  </head>
  <body>
    <h1>Professores:</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Título</th>
            <th>Curso</th>
        </tr>
    '''
    for resultado in resultados:
        html += f'''
        <tr>
            <td>{resultado[0]}</td>
            <td>{resultado[1]}</td>
            <td>{resultado[2]}</td>
            <td>{resultado[3]}</td>
        </tr>
        '''
    html += '''
    </table>
    <a href="/">Voltar Início</a>
  </body>
</html>
'''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')


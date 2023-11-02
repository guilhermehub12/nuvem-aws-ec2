from flask import Flask, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

def consultar_alunos():
    # conecta no banco
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='engajamente'
    )
    cursor = conn.cursor()

    # Executa uma consulta no banco
    cursor.execute('SELECT * FROM alunos')
    resultados = cursor.fetchall()

    # Fecha a conexão com o banco
    conn.close()

    return resultados

def consultar_professores():
    # conecta no banco
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
    return '''
    <h1>Projeto EngajaMente</h1>
    <a href="/alunos">Mostrar Alunos</a>
    <form method="get" action="/alunos">
        <button type="submit">Mostrar Alunos</button>
    </form>
    <form method="get" action="/professores">
        <button type="submit">Mostrar Professores</button>
    </form>
    '''

# Rota para mostrar os dados dos alunos
@app.route('/alunos')
def mostrar_dados_alunos():
    # Consulte o banco de dados
    resultados = consultar_alunos()

    # Converta os resultados em HTML
    html = '<h1>Alunos:</h1>'
    for resultado in resultados:
        html += f'<p>{resultado}</p>'
    html += '<form method="get" action="/">
                <button type="submit">Voltar</button>
            </form>'
    return html

# Rota para mostrar os dados dos professores
@app.route('/professores')
def mostrar_dados_professores():
    # Consulte o banco de dados
    resultados = consultar_professores()

    # Converta os resultados em HTML
    html = '<h1>Professores:</h1>'
    for resultado in resultados:
        html += f'<p>{resultado}</p>'
    html += '<form method="get" action="/">
                <button type="submit">Voltar</button>
            </form>'
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0')


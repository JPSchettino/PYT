from flask import Flask, redirect
import dash
from dash import dcc, html

# Criar o servidor Flask
server = Flask(__name__)

# Importar os aplicativos Dash
from app import create_app as recrutamento_create_app
from sens import create_app as sensorial_create_app

# Inicializar os aplicativos Dash e integrá-los com o servidor Flask
recrutamento_app = recrutamento_create_app(server, '/recrutamento/')
sensorial_app = sensorial_create_app(server, '/analise-sensorial/')

# Adicionar as rotas dos aplicativos Dash
@server.route('/')
def redirect_to_recrutamento():
    return redirect('/recrutamento/')

@server.route('/recrutamento/')
def render_recrutamento():
    return recrutamento_app.index()

@server.route('/analise-sensorial/')
def render_analise_sensorial():
    return sensorial_app.index()

# Página não encontrada
@server.errorhandler(404)
def page_not_found(e):
    return "404: Página não encontrada", 404

# Rodar o servidor Flask
if __name__ == '__main__':
    server.run(debug=True)

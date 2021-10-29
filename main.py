import os
'''
import dash
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicializa():
   diretorio_projeto = os.getcwd()
   diretorio_fotos = f'{diretorio_projeto}/static/fotos'
   diretorio_fotos_portfolio = os.path.join(diretorio_fotos, 'portfolio')
   lista_fotos_header = [arquivo_foto for arquivo_foto in os.listdir(diretorio_fotos)
                         if os.path.isfile(os.path.join(diretorio_fotos, arquivo_foto))]
   lista_fotos_portfolio = [arquivo_foto for arquivo_foto in os.listdir(diretorio_fotos_portfolio)
                         if os.path.isfile(os.path.join(diretorio_fotos_portfolio, arquivo_foto))]
   return render_template('template.html',
                          lista_fotos_header=lista_fotos_header,
                          lista_fotos_portfolio=lista_fotos_portfolio)


def achar_porta_livre():
   import socket
   from contextlib import closing
   '''
   https://stackoverflow.com/questions/1365265/on-localhost-how-do-i-pick-a-free-port-number
   '''
   with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
      s.bind(('', 0))
      s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      return s.getsockname()[1]

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=achar_porta_livre())

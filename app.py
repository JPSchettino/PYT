import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt
from  plot import create_bar_chart, create_pie_chart, create_pie_chart2, create_horizontal_bar_chart,create_separated_horizontal_bar_chart, create_grouped_horizontal_bar_chart
from data_pipeline import filter_data, stack_dataframe
from layout import recrutamento_layout
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class DataManager:
    def __init__(self):
        self.sales = pd.read_csv('Biscoito_doce_Recheado.csv')  # Carregar a base de dados padrão

    def update_data(self, selected_base):
        if selected_base == 'Biscoito Doce Recheado':
            self.sales = pd.read_csv('Biscoito_doce_Recheado.csv')
        elif selected_base == 'Wafer':
            self.sales = pd.read_csv('Wafer.csv')

    def get_data(self):
        return self.sales

data_manager = DataManager()

def get_unique_options(df, column_name):
    unique_options = df[column_name].dropna().unique().tolist()
    unique_options.append("Todas as categorias")
    return unique_options

# Carregar a base de dados inicial
sales = data_manager.get_data()

# Obter as opções únicas de cada coluna mencionada
faixa_etaria_options = get_unique_options(sales, 'Faixa etária:')
se_declara_options = get_unique_options(sales, 'Você se declara:')
classe_eco_servicos_options = get_unique_options(sales, 'Classe Econômica com Serviços')
reside_sp_options = get_unique_options(sales, 'Você reside na cidade de São Paulo?')
tem_filhos_options = get_unique_options(sales, 'Você tem filhos?')
resposta_selecionada_options = get_unique_options(sales, 'Resposta Selecionada')

# Importe o módulo para adicionar estilos externos
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', '/assets/styles.css']


def create_app(server, url_base_pathname):
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server, url_base_pathname=url_base_pathname)

    app.layout = recrutamento_layout(faixa_etaria_options, se_declara_options, classe_eco_servicos_options,
                                     reside_sp_options, tem_filhos_options, resposta_selecionada_options)

    @app.callback(
        Output('dummy-output', 'children'),
        [Input('base_de_dados', 'value')]
    )
    def update_data(selected_base):
        data_manager.update_data(selected_base)
        return None



    @app.callback(
        Output('bar_chart1', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_bar_chart(filtered_df, 'Faixa Etária', 'Faixa etária:')




    @app.callback(Output('donut_chart', 'figure'),
                [
                    Input('Faixa_etaria', 'value'),
                    Input('Segment', 'value'),
                    Input('Classe_eco_servicos', 'value'),
                    Input('Reside_sp', 'value'),
                    Input('Tem_filhos', 'value'),
                    Input('Resposta_selecionada', 'value')
                ])
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_pie_chart(filtered_df, 'Gênero', 'Você se declara:')

    @app.callback(
        Output('total_respostas', 'children'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_text(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        

        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        total_individuals = len(filtered_df)

        return [

            html.P('{0:,}'.format(total_individuals),
                style={'textAlign': 'center',
                        'color': '#19AAE1',
                        'fontSize': 25,
                        'margin-top': '17px'}
                ),
        ]







    @app.callback(
        Output('bar_chart2', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )

    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_bar_chart(filtered_df, 'Renda Familiar', 'Qual das oções a seguir melhor descreve a sua rende mensal familiar?')




    @app.callback(
        Output('line_chart', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )

    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_horizontal_bar_chart(filtered_df, 'Distribuição por Profissão', 'Você trabalha em algum dos seguimentos listados abaixo?')



    @app.callback(
        Output('pie_chart', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_pie_chart(filtered_df, 'Classe Econômica', 'Classe Econômica com Serviços')


    'Qual a sua escolaridade?'

    @app.callback(
        Output('bar_chart3', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_horizontal_bar_chart(filtered_df, ' Escolaridade', 'Qual a sua escolaridade?',left = 180)



    @app.callback(
        Output('donut_chart2', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_pie_chart(filtered_df, 'Têm filhos?', 'Você tem filhos?')


    @app.callback(
        Output('pie_chart_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_pie_chart(filtered_df, 'Você participou de alguma pesquisa recentemente?', 'Você participou nos últimos seis meses de alguma pesquisa, entrevista ou estudo direcionado a avaliação de alimentos ou bebidas?')


    'Qual a sua escolaridade?'

    @app.callback(
        Output('bar_chart3_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = 'Quais das opções abaixo se aplicam a você?'):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df.info(10)
        return create_horizontal_bar_chart(stacked_df, 'Aptidão para a avaliação', y_column)



    @app.callback(
        Output('donut_chart2_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        return create_pie_chart(filtered_df, 'Renda', 'Qual das oções a seguir melhor descreve a sua rende mensal familiar?')






    @app.callback(
        Output('h_bar_chart1_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = 'Quais sabores de biscoitos doces recheados você consome?'):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df.info(10)
        return create_horizontal_bar_chart(stacked_df, 'Quais sabores de biscoitos doces recheados você consome?', y_column)

    @app.callback(
        Output('h_bar_chart2_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = 'Qual a sua frequência de consumo de biscoitos doces recheados?'):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df.info(10)
        return create_horizontal_bar_chart(stacked_df, 'Frequência de consumo', y_column)




    #special plot

    @app.callback(
        Output('g_h_bar_chart1_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = 'Quais sabores de biscoitos doces recheados você NÃO consome?'):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df = stack_dataframe(stacked_df, "Quais sabores de biscoitos doces recheados você consome?")
        stacked_df.info(10)
        return create_separated_horizontal_bar_chart(stacked_df, 'Não Consome VS Consome', y_column,"Quais sabores de biscoitos doces recheados você consome?")

   
   
   
   
   
    @app.callback(
        Output('g_h_bar_chart2_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = 'Temos abaixo uma lista de diferentes alimentos para o consumo'):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df.info(10)
        return create_horizontal_bar_chart(stacked_df, 'Quais alimentos você consome', y_column)



    @app.callback(
        Output('g_h_bar_chart3_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = "Em quais ocasiões você consome"):
        sales = data_manager.get_data()
        filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
        stacked_df = stack_dataframe(filtered_df, y_column)
        stacked_df.info(10)
        return create_horizontal_bar_chart(stacked_df, "Em quais ocasiões você consome {selected_base}", y_column)
    


    @app.callback(
        Output('g_h_bar_chart4_', 'figure'),
        [
            Input('Faixa_etaria', 'value'),
            Input('Segment', 'value'),
            Input('Classe_eco_servicos', 'value'),
            Input('Reside_sp', 'value'),
            Input('Tem_filhos', 'value'),
            Input('Resposta_selecionada', 'value')
        ]
    )
    def update_graph(faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada,y_column = "Quais marcas de biscoitos doces recheados você consome ou já consumiu?"):
            sales = data_manager.get_data()
            filtered_df = filter_data(sales, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada)
            stacked_df = stack_dataframe(filtered_df, y_column)
            stacked_df.info(10)
            return create_horizontal_bar_chart(stacked_df, "Quais marcas de {selected_base} você consome?", y_column)


    return app





#Quais marcas de biscoitos doces recheados você consome ou já consumiu?


if __name__ == '__main__':
    app = create_app(server=None, url_base_pathname='/')
    app.run_server(debug=True)




    #"Temos abaixo uma lista de diferentes alimentos para o consumo","Em quais ocasiões você consome"
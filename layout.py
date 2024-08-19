from dash import html, dcc
import dash_core_components as dcc
import dash_html_components as html

def recrutamento_layout(faixa_etaria_options, se_declara_options, classe_eco_servicos_options,
                  reside_sp_options, tem_filhos_options, resposta_selecionada_options):

    layout = html.Div([

        # Header Section
        html.Div([
            html.Img(src='assets\Bauducco-logo-9890473269-seeklogo.com.png', className='header-logo'),  # Add the logo image
            html.Div([
                html.H1('Recrutamento', className='header-title'),
                html.P('Acompanhe o recrutamento do achocolatado', className='header-subtitle')
            ], className="header-text"),
            html.Div([
                html.Div([
                    html.Img(src='assets\pessoas3.png', className='header-icon'),  # Add icons
                    html.A('Recrutamento de Avaliadores', href='/recrutamento', className='header-link')
                ], className='header-link-container')

            ], className='header-links')
        ], className="header"),

        # Database Selection and Total Responses Counter Section
        html.Div([
            html.Div([
                html.P('Dia a dia do recrutamento, para visualizar o andamento', className='label'),
                dcc.Dropdown(
                    id='base_de_dados',
                    options=[
                        {'label': 'Achocolatado-19/08', 'value': 'Achocolatado-19/08'},
                        {'label': 'Achocolatado-16/08', 'value': 'Achocolatado-16/08'},
                        {'label': 'Achocolatado-15/08', 'value': 'Achocolatado-15/08'}
                    ],
                    value="Achocolatado-15/08",
                    className='dropdown-2'
                )
            ], className='container'),
            html.Div([
                html.H4("Total de Respostas:"),
                html.H2(id='total_respostas', className='total-responses')
            ], className='total-responses-container')
        ], className="row flex-display selection-counter"),

        # Dropdown Menus Section
        html.Div([
            html.Div([
                html.P('Faixa Etária', className='label'),
                dcc.Dropdown(id='Faixa_etaria', options=faixa_etaria_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column"),

            html.Div([
                html.P('Gênero', className='label'),
                dcc.Dropdown(id='Segment', options=se_declara_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column"),

            html.Div([
                html.P('Classe Econômica com Serviços', className='label'),
                dcc.Dropdown(id='Classe_eco_servicos', options=classe_eco_servicos_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column"),

            html.Div([
                html.P('Você reside na cidade de São Paulo?', className='label'),
                dcc.Dropdown(id='Reside_sp', options=reside_sp_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column"),

            html.Div([
                html.P('Você tem filhos?', className='label'),
                dcc.Dropdown(id='Tem_filhos', options=tem_filhos_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column"),

            html.Div([
                html.P('Resposta Selecionada', className='label'),
                dcc.Dropdown(id='Resposta_selecionada', options=resposta_selecionada_options, value="Todas as categorias", className='dropdown')
            ], className="dropdown-column")
        ], className="dropdown-container row flex-display"),

        html.Div(id='dummy-output'),

        # Charts Section
        html.Div([
            html.Div([
                dcc.Graph(id='donut_chart', config={'displayModeBar': 'hover'}, style={'height': '450px'})
            ], className='chart-container four columns'),

            html.Div([
                dcc.Graph(id='bar_chart1', config={'displayModeBar': 'hover'}, style={'height': '450px'})
            ], className='chart-container eight columns')
        ], className="row flex-display"),

        html.Div([
            html.Div([
                dcc.Graph(id='bar_chart3', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container four columns'),

                        html.Div([
                dcc.Graph(id='bar_chart2', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container four columns'),

            html.Div([
                dcc.Graph(id='pie_chart', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container four columns')
        ], className="row flex-display"),

        html.Div([
            html.Div([
                dcc.Graph(id='line_chart', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container six columns'),

            html.Div([
                dcc.Graph(id='donut_chart2_', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container six columns')
        ], className="row flex-display"),

        html.Div([
            html.Div([
                dcc.Graph(id='pie_chart_', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container six columns'),

            html.Div([
                dcc.Graph(id='h_bar_chart2_', config={'displayModeBar': 'hover'}, style={'height': '550px'})
            ], className='chart-container six columns')
        ], className="row flex-display"),

        


        

    ], id="mainContainer", style={"display": "flex", "flex-direction": "column"})
  

    return layout

































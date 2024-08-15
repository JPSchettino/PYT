import plotly.graph_objs as go
import pandas as pd

def create_bar_chart(df, title, column_name):
    counts = df[column_name].value_counts().reset_index()
    counts.columns = [column_name, 'Count']
    counts['Percentage'] = (counts['Count'] / counts['Count'].sum()) * 100

    data = [
        go.Bar(
            x=counts[column_name],
            y=counts['Count'],
            text=counts.apply(lambda row: f"({row['Percentage']:.2f}%)", axis=1),
            texttemplate='%{text}',
            textposition='auto',
            orientation='v',
            marker=dict(color='#19AAE1'),

            hoverinfo='text',
            hovertext=
            f'<b>Contagem</b>: ' + counts['Count'].astype(str) + '<br>' +
            '<b>Percentagem</b>: ' + counts['Percentage'].astype(str) + '%<br>'
        )
    ]

    layout = go.Layout(
        plot_bgcolor='White',
        paper_bgcolor='White',
        title={
            'text': title,
            'y': 0.99,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        titlefont={
            'color': '#666666',
            'size': 20  # Increased title size
        },

        hovermode='closest',
        margin=dict(t=70, r=40, l=40, b=150),  # Adjusted margins for better spacing

        xaxis=dict(
            title='',  # Added title for the x-axis
            titlefont=dict(
                family='sans-serif',
                size=16,
                color='Black'
            ),
            showline=False,
            showgrid=False,
            showticklabels=True,
            linecolor='Black',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='sans-serif',
                size=17,  # Increased label size
                color='Black'
            )
        ),

        yaxis=dict(
            title='',  # Title translated to Portuguese
            titlefont=dict(
                family='sans-serif',
                size=16,
                color='Black'
            ),
            color='Black',
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='Black',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='sans-serif',
                size=14,  # Increased label size
                color='Black'
            )
        ),

        legend=dict(
            orientation='h',
            bgcolor='#1f2c56',
            x=0.5,
            y=-0.2,
            xanchor='center',
            yanchor='top',
            font=dict(
                size=16,  # Set legend text size
                color='Black'
            )
        ),

        font=dict(
            family="sans-serif",
            size=19,
            color='Black'
        )
    )

    return {'data': data, 'layout': layout}






def create_pie_chart(df, title, column_name):
    counts = df[column_name].value_counts()
    labels = counts.index.tolist()
    values = counts.values.tolist()
    colors = ['#30C9C7', '#7A45D1', 'orange', '#FF6347', '#FFD700']

    return {
        'data': [go.Pie(labels=labels,
                        values=values,
                        marker=dict(colors=colors),
                        hoverinfo='label+value+percent',
                        textinfo='percent',
                        textfont=dict(size=18),
                        texttemplate='<br>%{percent}',
                        textposition='auto',
                        hole=.7,
                        rotation=160,
                        insidetextorientation='radial',
                        )],
        'layout': go.Layout(
            plot_bgcolor='White',
            paper_bgcolor='White',
            hovermode='x',
            title={
                'text': title,
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            titlefont={
                'color': '#666666',
                'size': 20
            },
          legend=dict(
                orientation='h',  # Orientação da legenda ('v' para vertical, 'h' para horizontal)
                bgcolor='white',  # Cor de fundo da legenda
                bordercolor='black',  # Cor da borda da legenda
                borderwidth=0,  # Largura da borda da legenda
                font=dict(
                    family="sans-serif",  # Família da fonte da legenda
                    size=12,  # Tamanho da fonte da legenda
                    color='Black'  # Cor da fonte da legenda
                ),
                xanchor='left',  # Ancoragem horizontal da legenda ('auto', 'left', 'center', 'right')
                yanchor='bottom',  # Ancoragem vertical da legenda ('auto', 'top', 'middle', 'bottom')
                y = -0.01, # Posição vertical da legenda (valor entre -2 e 3, onde 0 é o centro do gráfico)
                x = 1,

                #traceorder='normal',  # Ordem das entradas na legenda ('normal', 'reversed', 'grouped', 'reversed+grouped')
                #itemclick='toggle',  # Comportamento ao clicar na entrada da legenda ('toggle', 'toggleothers', False)
                itemdoubleclick='toggleothers',  # Comportamento ao dar duplo clique na entrada da legenda ('toggle', 'toggleothers', False)
                valign='bottom',  # Alinhamento vertical do texto da legenda ('top', 'middle', 'bottom')
                tracegroupgap=0  # Espaço entre grupos de traços na legenda
            ),
            font=dict(
                family="sans-serif",
                size=12,
                color='Black'
            )
        ),
    }




def create_pie_chart2(df, title, column_name):
    counts = df[column_name].value_counts()
    labels = counts.index.tolist()
    values = counts.values.tolist()
    colors = ['#FFA07A', '#20B2AA', '#778899', '#FF6347', '#4682B4']

    return {
        'data': [
            go.Pie(
                labels=labels,
                values=values,
                hoverinfo='label+percent+value',
                textinfo='label+percent',
                textfont=dict(size=16),
                marker=dict(colors=colors),
                hole=.3
            )
        ],
        'layout': go.Layout(
            plot_bgcolor='White',
            paper_bgcolor='White',
            title={
                'text': title,
                'y': 0.93,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            titlefont={
                'color': '#666666',
                'size': 20
            },
          legend=dict(
                orientation='h',  # Orientação da legenda ('v' para vertical, 'h' para horizontal)
                bgcolor='white',  # Cor de fundo da legenda
                bordercolor='black',  # Cor da borda da legenda
                borderwidth=1,  # Largura da borda da legenda
                font=dict(
                    family="sans-serif",  # Família da fonte da legenda
                    size=102,  # Tamanho da fonte da legenda
                    color='Black'  # Cor da fonte da legenda
                ),
                xanchor='right',  # Ancoragem horizontal da legenda ('auto', 'left', 'center', 'right')
                yanchor='bottom',  # Ancoragem vertical da legenda ('auto', 'top', 'middle', 'bottom')
              # Posição vertical da legenda (valor entre -2 e 3, onde 0 é o centro do gráfico)
                #traceorder='normal',  # Ordem das entradas na legenda ('normal', 'reversed', 'grouped', 'reversed+grouped')
                #itemclick='toggle',  # Comportamento ao clicar na entrada da legenda ('toggle', 'toggleothers', False)
                itemdoubleclick='toggleothers',  # Comportamento ao dar duplo clique na entrada da legenda ('toggle', 'toggleothers', False)
                valign='middle',  # Alinhamento vertical do texto da legenda ('top', 'middle', 'bottom')
                tracegroupgap=0  # Espaço entre grupos de traços na legenda
            ),

            font=dict(
                family="sans-serif",
                size=13,
                color='Black'
            )
        )
    }




def create_horizontal_bar_chart(df, title, column_name, left=240):
    # Conta a frequência de cada valor na coluna especificada e calcula as porcentagens
    counts = df[column_name].value_counts().reset_index()
    counts.columns = [column_name, 'Count']
    counts['Percentage'] = (counts['Count'] / counts['Count'].sum() * 100).round(2)

    # Função para gerar os dados ordenados
    def get_data(sorted_counts):
        return [
            go.Bar(
                y=sorted_counts[column_name],  # Valores para o eixo y (categorias)
                x=sorted_counts['Count'],  # Valores para o eixo x (contagens)
                text=sorted_counts.apply(lambda row: f'({row["Percentage"]}%)', axis=1),  # Texto para exibir na barra
                texttemplate='%{text}',  # Formato do texto
                textposition='outside',  # Posição do texto (fora da barra)
                textfont=dict(
                    family='Arial',  # Fonte do texto
                    size=18,  # Tamanho da fonte do texto
                    color='Black'  # Cor do texto
                ),
                orientation='h',  # Barra horizontal
                marker=dict(color='#19AAE1'),  # Cor da barra
                hoverinfo='text',  # Informação mostrada ao passar o mouse
                hovertext=(
                    f'<b>Countagem</b>: ' + sorted_counts['Count'].astype(str) + '<br>' +
                    '<b>Percentagem</b>: ' + sorted_counts['Percentage'].astype(str) + '%'
                )  # Texto de hover
            )
        ]

    # Dados iniciais
    data = get_data(counts)

    # Configura o layout do gráfico
    layout = go.Layout(
        plot_bgcolor='White',  # Cor de fundo do gráfico
        paper_bgcolor='White',  # Cor de fundo do papel
        title={
            'text': title,  # Título do gráfico
            'y': 0.95,  # Posição vertical do título
            'x': 0.5,  # Posição horizontal do título
            'xanchor': 'center',  # Ancoragem horizontal do título
            'yanchor': 'top',  # Ancoragem vertical do título
            'font': {
                'color': '#666666',  # Cor do título
                'size': 20  # Tamanho do título
            }
        },
        margin=dict(t=100, r=40, b=40, l=left),  # Margens do gráfico
        hovermode='closest',  # Modo de hover
        xaxis=dict(
            showline=False,  # Mostrar linha do eixo x
            showgrid=False,  # Mostrar grade do eixo x
            showticklabels=True,  # Mostrar rótulos dos ticks
            linecolor='Black',  # Cor da linha do eixo x
            linewidth=1,  # Largura da linha do eixo x
            ticks='outside',  # Posição dos ticks
            tickfont=dict(
                family='Arial',  # Fonte dos ticks
                size=16,  # Tamanho da fonte dos ticks
                color='Black'  # Cor dos ticks
            ),
            title='',  # Título do eixo x
            titlefont=dict(
                family='Arial',  # Fonte do título do eixo x
                size=15,  # Tamanho da fonte do título do eixo x
                color='Black'  # Cor do título do eixo x
            )
        ),
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='Black',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=16,
                color='Black'
            ),
            tickangle=0  # Inclinar os rótulos dos ticks a 45 graus
        ),
        font=dict(
            family="sans-serif",  # Fonte padrão do gráfico
            size=19,  # Tamanho da fonte padrão
            color='black'  # Cor da fonte padrão
        ),
        annotations=[
            dict(
                text='',  # Texto da anotação
                showarrow=False,  # Não mostrar seta
                xref='paper',  # Referência do eixo x
                yref='paper',  # Referência do eixo y
                x=0.5,  # Posição x da anotação
                y=-0.15,  # Posição y da anotação
                font=dict(
                    family='Arial',  # Fonte do texto
                    size=12,  # Tamanho da fonte
                    color='Black'  # Cor do texto
                ),
                align='center'  # Alinhamento do texto
            )
        ],
updatemenus=[
    dict(
        buttons=list([
            dict(
                args=[
                    {
                        'y': [counts.sort_values(by='Count', ascending=False)[column_name]],
                        'x': [counts.sort_values(by='Count', ascending=False)['Count']],
                        'text': [counts.sort_values(by='Count', ascending=False).apply(lambda row: f'({row["Percentage"]}%)', axis=1)],
                        'orientation': 'h'
                    }
                ],
                label='↑',
                method='update'
            ),
            dict(
                args=[
                    {
                        'y': [counts.sort_values(by='Count', ascending=True)[column_name]],
                        'x': [counts.sort_values(by='Count', ascending=True)['Count']],
                        'text': [counts.sort_values(by='Count', ascending=True).apply(lambda row: f' ({row["Percentage"]}%)', axis=1)],
                        'orientation': 'h'
                    }
                ],
                label='↓',
                method='update'
            )
        ]),
        direction='down', # 'left', 'right', 'up', 'down' - direção da lista de botões
        showactive=True,  # True, False - se o botão ativo deve ser destacado
        x=1.4,  # posição horizontal do botão
        xanchor='left',  # 'auto', 'left', 'center', 'right' - ancoragem horizontal do botão
        y=1.2,  # posição vertical do botão
        yanchor='top',  # 'auto', 'top', 'middle', 'bottom' - ancoragem vertical do botão
        bgcolor='rgba(0,0,0,0)',  # cor de fundo do botão
        bordercolor='Black',  # cor da borda do botão
        font=dict(
            color='Black'  # cor do texto do botão
        ),
        # Parâmetros adicionais comentados:
        # active=0,  # Índice do botão ativo inicialmente
        # borderwidth=1,  # Largura da borda do botão
        # font=dict(
        #     color='Black',  # Cor do texto do botão
        #     family='Arial',  # Família da fonte
        #     size=12  # Tamanho da fonte
        # ),
        # pad=dict(
        #     b=5,  # Espaço (padding) abaixo do botão
        #     l=5,  # Espaço (padding) à esquerda do botão
        #     r=5,  # Espaço (padding) à direita do botão
        #     t=5   # Espaço (padding) acima do botão
        # ),
        type='buttons'  # Tipo de controle ('buttons', 'dropdown', 'sliders')
    ),
]





    )

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(transition_duration=500)

    return fig



def create_separated_horizontal_bar_chart(df, title, column_yes, column_no):
    # Remove linhas com valores nulos nas colunas especificadas
    df = df[(df[column_yes].notna()) | (df[column_no].notna())]

    # Calcular contagens e porcentagens para a coluna 'Consome'
    counts_yes = df[column_yes].value_counts().reset_index()
    counts_yes.columns = [column_yes, 'Contagem Consome']
    counts_yes['Porcentagem Consome'] = (counts_yes['Contagem Consome'] / counts_yes['Contagem Consome'].sum() * 100).round(2)

    # Calcular contagens e porcentagens para a coluna 'Não Consome'
    counts_no = df[column_no].value_counts().reset_index()
    counts_no.columns = [column_no, 'Contagem Não Consome']
    counts_no['Porcentagem Não Consome'] = (counts_no['Contagem Não Consome'] / counts_no['Contagem Não Consome'].sum() * 100).round(2)

    # Renomear colunas para facilitar a combinação dos dataframes
    counts_yes = counts_yes.rename(columns={column_yes: 'Sabor'})
    counts_no = counts_no.rename(columns={column_no: 'Sabor'})
    counts_yes['Tipo'] = 'Consome'
    counts_no['Tipo'] = 'Não Consome'
    
    # Combinar ambos os dataframes de contagens
    combined_counts = pd.concat([counts_yes, counts_no])

    # Criar dados separados para 'Consome' e 'Não Consome'
    data = []
    for tipo, df_tipo in combined_counts.groupby('Tipo'):
        data.append(
            go.Bar(
                y=df_tipo['Sabor'],  # Valores para o eixo y (sabores)
                x=df_tipo[f'Contagem {tipo}'],  # Valores para o eixo x (contagens)
                name=tipo,  # Nome do tipo ('Consome' ou 'Não Consome')
                orientation='h',  # Barra horizontal
                marker=dict(color='#19AAE1' if tipo == 'Consome' else '#FFA07A'),  # Cor da barra
                text=df_tipo.apply(lambda row: f'({row[f"Porcentagem {tipo}"]}%)', axis=1),  # Texto para exibir na barra
                textposition='outside',  # Posição do texto (fora da barra)
                hoverinfo='text',  # Informação mostrada ao passar o mouse
                hovertext=(
                    f'<b>Contagem {tipo}</b>: ' + df_tipo[f'Contagem {tipo}'].astype(str) + '<br>' +
                    f'<b>Porcentagem {tipo}</b>: ' + df_tipo[f'Porcentagem {tipo}'].astype(str) + '%'
                ),  # Texto de hover
                width=0.8  # Aumentar a espessura das barras
            )
        )

    # Configura o layout do gráfico
    layout = go.Layout(
        barmode='stack',  # Modo de barras empilhadas
            plot_bgcolor='White',
            paper_bgcolor='White',
        title={
            'text': title,  # Título do gráfico
            'y': 0.95,  # Posição vertical do título
            'x': 0.5,  # Posição horizontal do título
            'xanchor': 'center',  # Ancoragem horizontal do título
            'yanchor': 'top',  # Ancoragem vertical do título
            'font': {
                'color': '#666666',  # Cor do título
                'size': 25  # Tamanho do título
            }
        },
        margin=dict(t=100, r=40, b=40, l=240),  # Margens do gráfico
        hovermode='closest',  # Modo de hover
        xaxis=dict(
            showline=True,  # Mostrar linha do eixo x
            showgrid=True,  # Mostrar grade do eixo x
            showticklabels=True,  # Mostrar rótulos dos ticks
            linecolor='Black',  # Cor da linha do eixo x
            linewidth=1,  # Largura da linha do eixo x
            ticks='outside',  # Posição dos ticks
            tickfont=dict(
                family='Arial',  # Fonte dos ticks
                size=12,  # Tamanho da fonte dos ticks
                color='black'  # Cor dos ticks
            ),
            title='<b></b>',  # Título do eixo x
            titlefont=dict(
                family='Arial',  # Fonte do título do eixo x
                size=18,  # Tamanho da fonte do título do eixo x
                color='black'  # Cor do título do eixo x
            ),
             
        ),
        yaxis=dict(
            showline=True,  # Mostrar linha do eixo y
            showgrid=False,  # Mostrar grade do eixo y
            showticklabels=True,  # Mostrar rótulos dos ticks
            linecolor='Black',  # Cor da linha do eixo y
            linewidth=1,  # Largura da linha do eixo y
            ticks='outside',  # Posição dos ticks
            tickfont=dict(
                family='Bold',  # Fonte dos ticks
                size=12,  # Tamanho da fonte dos ticks
                color='Black'  # Cor dos ticks
            )
        ),
        legend=dict(
            x=0.5,  # Posição horizontal da legenda
            y=-0.2,  # Posição vertical da legenda
            xanchor='center',  # Ancoragem horizontal da legenda
            yanchor='top',  # Ancoragem vertical da legenda
            orientation='h',  # Orientação da legenda (horizontal)
            font=dict(
                family='Arial',  # Fonte da legenda
                size=20,  # Tamanho da fonte da legenda
                color='Black'  # Cor da legenda
            )
        ),
        font=dict(
            family="sans-serif",  # Fonte padrão do gráfico
            size=20,  # Tamanho da fonte padrão
            color='Black'  # Cor da fonte padrão
        ),
        updatemenus=[  # Adiciona botões de atualização
            dict(
                buttons=list([
                    dict(
                        args=[{'y': [counts_yes.sort_values(by='Contagem Consome', ascending=True)['Sabor']],
                               'x': [counts_yes.sort_values(by='Contagem Consome', ascending=True)['Contagem Consome']],
                               'text': [counts_yes.sort_values(by='Contagem Consome', ascending=True).apply(lambda row: f'({row["Porcentagem Consome"]}%)', axis=1)],
                               'orientation': 'h'}],
                        label='↑',
                        method='update'
                    ),
                    dict(
                        args=[{'y': [counts_yes.sort_values(by='Contagem Consome', ascending=False)['Sabor']],
                               'x': [counts_yes.sort_values(by='Contagem Consome', ascending=False)['Contagem Consome']],
                               'text': [counts_yes.sort_values(by='Contagem Consome', ascending=False).apply(lambda row: f'({row["Porcentagem Consome"]}%)', axis=1)],
                               'orientation': 'h'}],
                        label='↓',
                        method='update'
                    )
                ]),
        direction='down', # 'left', 'right', 'up', 'down' - direção da lista de botões
        showactive=True,  # True, False - se o botão ativo deve ser destacado
        x=1.4,  # posição horizontal do botão
        xanchor='left',  # 'auto', 'left', 'center', 'right' - ancoragem horizontal do botão
        y=1.2,  # posição vertical do botão
        yanchor='top',  # 'auto', 'top', 'middle', 'bottom' - ancoragem vertical do botão
        bgcolor='rgba(0,0,0,0)',  # cor de fundo do botão
        bordercolor='Black',  # cor da borda do botão
        font=dict(
            color='Black'  # cor do texto do botão
        ),
        # Parâmetros adicionais comentados:
        # active=0,  # Índice do botão ativo inicialmente
        # borderwidth=1,  # Largura da borda do botão
        # font=dict(
        #     color='Black',  # Cor do texto do botão
        #     family='Arial',  # Família da fonte
        #     size=12  # Tamanho da fonte
        # ),
        # pad=dict(
        #     b=5,  # Espaço (padding) abaixo do botão
        #     l=5,  # Espaço (padding) à esquerda do botão
        #     r=5,  # Espaço (padding) à direita do botão
        #     t=5   # Espaço (padding) acima do botão
        # ),
        type='buttons'  # Tipo de controle ('buttons', 'dropdown', 'sliders')
    ),
]
    )

    # Retorna os dados e o layout configurados
    return {'data': data, 'layout': layout}



def create_grouped_horizontal_bar_chart(df, title, column_yes, column_no):
    # Calculate counts and percentages for the 'Yes' column
    df = df[(df[column_yes].notna()) | (df[column_no].notna())]

    counts_yes = df[column_yes].value_counts().reset_index()
    counts_yes.columns = [column_yes, 'Contagem Consome']
    counts_yes['Porcentagem Consome'] = (counts_yes['Contagem Consome'] / counts_yes['Contagem Consome'].sum() * 100).round(2)

    # Calculate counts and percentages for the 'No' column
    counts_no = df[column_no].value_counts().reset_index()
    counts_no.columns = [column_no, 'Contagem Não Consome']
    counts_no['Porcentagem Não Consome'] = (counts_no['Contagem Não Consome'] / counts_no['Contagem Não Consome'].sum() * 100).round(2)

    # Merge the counts dataframes on the category names
    counts = pd.merge(counts_yes, counts_no, left_on=column_yes, right_on=column_no, how='outer').fillna(0)
    counts[column_yes] = counts[column_yes].combine_first(counts[column_no])
    
    data = [
        go.Bar(
            y=counts[column_yes],
            x=counts['Contagem Consome'],
            name='Consome',
            orientation='h',
            marker=dict(color='#19AAE1'),
            text=counts.apply(lambda row: f'{row["Contagem Consome"]} ({row["Porcentagem Consome"]}%)', axis=1),
            textposition='outside',
            hoverinfo='text',
            hovertext=
            
            f'<b>Contagem</b>: ' + counts['Contagem Consome'].astype(str) + '<br>' +
            '<b>Porcentagem</b>: ' + counts['Porcentagem Consome'].astype(str) + '%'
        ),
        go.Bar(
            y=counts[column_yes],
            x=counts['Contagem Não Consome'],
            name='Não Consome',
            orientation='h',
            marker=dict(color='#FFA07A'),
            text=counts.apply(lambda row: f'{row["Contagem Não Consome"]} ({row["Porcentagem Não Consome"]}%)', axis=1),
            textposition='outside',
            hoverinfo='text',
            hovertext=
            
            f'<b>Contagem</b>: ' + counts['Contagem Não Consome'].astype(str) + '<br>' +
            '<b>Porcentagem</b>: ' + counts['Porcentagem Não Consome'].astype(str) + '%'
        )
    ]

    layout = go.Layout(
        barmode='group',
        plot_bgcolor='White',
        paper_bgcolor='White',
        title={
            'text': title,
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {
                'color': 'black',
                'size': 20
            }
        },
        margin=dict(t=100, r=40, b=40, l=240),
        hovermode='closest',
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='Black',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            ),
            title='<b></b>',
            titlefont=dict(
                family='Arial',
                size=15,
                color='black'
            )
        ),
        yaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor='Black',
            linewidth=1,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='black'
            )
        ),
        legend=dict(
            x=0.5,
            y=-0.2,
            xanchor='center',
            yanchor='top',
            orientation='h',
            font=dict(
                family='Arial',
                size=12,
                color='black'
            )
        ),
        font=dict(
            family="sans-serif",
            size=15,
            color='black'
        )
    )

    return {'data': data, 'layout': layout}
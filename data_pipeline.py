
def filter_data(df, faixa_etaria, segment, classe_eco_servicos, reside_sp, tem_filhos, resposta_selecionada):
    # Remove linhas onde as colunas especificadas são nulas

    filtered_df = df

    if faixa_etaria != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Faixa etária:'] == faixa_etaria]

    if segment != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Você se declara:'] == segment]

    if classe_eco_servicos != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Classe Econômica com Serviços'] == classe_eco_servicos]

    if reside_sp != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Você reside na cidade de São Paulo?'] == reside_sp]

    if tem_filhos != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Você tem filhos?'] == tem_filhos]

    if resposta_selecionada != "Todas as categorias":
        filtered_df = filtered_df[filtered_df['Resposta Selecionada'] == resposta_selecionada]

    return filtered_df


def stack_dataframe(df, y_column):
    # Dividir as respostas múltiplas em linhas separadas
    stacked_df = df.set_index([col for col in df.columns if col != y_column])[y_column].str.split(',', expand=True).stack().reset_index(level=-1, drop=True).reset_index()
    stacked_df.rename(columns={stacked_df.columns[-1]: y_column}, inplace=True)
    #stacked_df.columns = list(df.columns)
    stacked_df.info(10)

    return stacked_df
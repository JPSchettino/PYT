# Dash Dashboard Project

## Visão Geral

Este projeto utiliza o framework Dash em Python para criar um dashboard interativo. O dashboard é projetado para visualizar e analisar dados, fornecendo insights úteis de maneira eficiente e intuitiva.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

## Descrição dos Arquivos

- **app.py**: Arquivo principal do projeto. Responsável por inicializar o aplicativo Dash e integrar todas as dependências necessárias.
- **data_pipeline.py**: Contém funções para transformação e filtragem dos dados, preparando-os para visualização.
- **index.py**: Exemplo de visualizações que foi deprecado, mas está mantido no projeto para referência futura.
- **layout.py**: Define o layout HTML do dashboard, estruturando a interface do usuário.
- **plot.py**: Inclui funções para criação e personalização de gráficos.
- **requirements.txt**: Lista de pacotes e bibliotecas necessários para rodar o projeto.
- **Wafer_Recrut.csv**: Base de dados utilizada para testar e validar as funcionalidades do dashboard.
- **train.csv**: Dados destinados ao modelo de IA, que ainda está em desenvolvimento.
- **assets/**: Diretório que contém arquivos CSS, incluindo o `styles.css` para estilização da página de IA.

## Começando

Para começar a usar o projeto, siga os passos abaixo:

1. Clone o repositório para sua máquina local:
   ```sh
   git clone https://github.com/JPSchettino/Dash_recrutamento.git


2. Navegue até o diretório do projeto:
   ```sh
   cd Dash_recrutamento


3. Crie um ambiente virtual
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`

4. Instale as dependências:
   ```sh
   pip install -r requirements.txt


5. Execute o aplicativo:
   ```sh
   python app.py

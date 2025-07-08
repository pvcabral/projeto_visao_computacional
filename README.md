# Projeto de Visao Computacional

## 1. Introdução 
Diante do aumento da digitalização de documentos, a extração de informações contidas em imagens se torna uma tarefa cada vez mais relevante. Este projeto visa desenvolver uma aplicação que permita a extração de dados de documentos digitalizados de Engenharia Civil, utilizando técnicas de visão computacional e processamento de imagem.
O foco principal é otimizar a extração de informações de documentos de Engenharia Civil, facilitando o acesso e a manipulação de dados contidos PDFs com informações relevantes do projeto, como Autor, revisão, data, entre outros.

## 1.1 Problema 
Com a alta demanda da Engenharia Civil, torna-se imprecidível uma otimização nos processos de transformação de documentos digitalizados em informações úteis, visto que a maioria dos documentos são digitalizados e armazenados em PDF, o que dificulta a extração de dados relevantes para análise e tomada de decisão. A necessidade de uma solução que permita a extração eficiente e precisa de informações contidas nesses documentos é evidente, visando reduzir o tempo gasto na busca e organização de dados essenciais para os projetos.
Atualmente, a extração dessas inforamções é feita de forma manual, o que demanda tempo e pode levar a erros humanos. A automação desse processo é crucial para aumentar a eficiência e a precisão na manipulação de dados, permitindo que os profissionais da área se concentrem em atividades mais estratégicas e menos operacionais.

## 1.2 Objetivo 

Utilizar técnicas de visão computacional na extração de informações em imagens de documentos digitalizados com o intuito de otimizar processos adminstrativos.  

## 2. Desenvolvimento

### Etapa 1:
- Transformar o PDF em imagem, utilizando a biblioteca pdf2image.
- Criar lógica para o usuário selecionar as coordenadas para a imagem dar um "zoom" na área de interesse, utilizando a biblioteca OpenCV ou Matplotlib.

### Etapa 2:
- Utilizar a biblioteca Tesseract OCR para realizar a extração de texto da imagem.
- Solicitar ao usuário quais textos serão extraídos, tendo como chave o primeiro caracter, e o segundo o seu valor. 
- Montar um DataFrame com as informações extraídas, utilizando a biblioteca Pandas e os.

### Etapa 3 (opcional):
- Armazenar os arquivos exportados pelos usuários em um banco de dados para posteriormente serem utilizados em análises mais complexas, criando uma Machine learning que reconheça os arquivos, e possa selecionar a área em que está o texto de interesse, e extrair as informações de forma automática, sem a necessidade de intervenção do usuário.

## 2.1 Detalhes de implementação 

A aplicação proporciona uma interface voltada para usabilidade do usuário, sendo liberado a sua escolha as informações que deseja utilizar, por meio de planilhas Excel ou CSV, assim, sendo sua implementação feita no streamlit, devida a sua capacidade de elaboração de protótipos de forma rápida e com qualidade. 

## 2.2 Técnicas utilizadas 

## 3. Resultados 

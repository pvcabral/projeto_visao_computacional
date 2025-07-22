# Detecção e coleta de informações em documentos técnicos

## 📜 Sumário 

- [Estrutura do projeto]()
- [Introdução]()
- [Desenvolvimento]()
    - [Aquisição dos documentos]()
    - [Processamento dos documentos]()
    - [Utilizando machine learning - Implementação futura]()
- [Conclusão]()
- [Principais Tecnologias utilizadas]()
- [Como Executar](#-como-executar)
- [Equipe do Projeto](#--equipe-do-projeto)
- [Referências Bibliográficas](#-referências-bibliográficas)

## 🗂️ Estrutura do projeto



## 📌 Introdução 
  
Diante do aumento da digitalização de documentos no contexto da Engenharia Civil, torna-se uma prática comum fazer a extração dessas informações de forma manual, o que demanda tempo e pode levar a erros humanos. Visando reduzir o tempo gasto na busca e organização de dados essenciais para os projetos, buscamos desenvolver uma aplicação que permita a extração dos dados de documentos digitalizados, utilizando técnicas de visão computacional e reconhecimento óptico de caracteres (OCR) para a automação desse processo, aumentando assim a eficiência e precisão na manipulação de dados e permitindo que os profissionais da área se concentrem em atividades estratégicas. 

## ⚙️ Desenvolvimento

Este projeto propõe uma metodologia para a extração semi-automatizada de informações essenciais de documentos técnicos da engenharia civil, fornecidos em formato PDF oriundos de digitalização. O processo visa converter as páginas digitalizadas em um formato passível de análise, permitir a seleção de áreas de interesse e, por fim, extrair o texto contido nessas regiões para posterior organização em um formato estruturado (CSV).

### Aquisição e Pré-processamento de Documentos

A primeira etapa concentra-se na aquisição e preparação dos arquivos PDF para análise.

***Entrada de Dados:*** O sistema permitirá o upload de arquivos PDF pelo usuário. É necessário que esses PDFs sejam de documentos digitalizados, característicos de plantas de projetos, relatórios antigos ou formulários preenchidos manualmente.

***Conversão para Imagem:*** Cada página do PDF será convertida em um objeto de imagem rasterizada. Para isso, será utilizada a biblioteca pdf2image, que age como wrapper para a ferramenta Poppler. Essa etapa é fundamental, pois as operações de seleção de área e OCR são otimizadas para trabalhar com dados visuais (pixels). A conversão resultará em uma lista de objetos PIL.Image.Image, cada um representando uma página do documento original.

***Melhoria da Qualidade da Imagem (Futura implementação):*** Embora o pdf2image já renderize as páginas, pré-processamentos adicionais podem ser aplicados às imagens resultantes para otimizar o desempenho do OCR. Isso pode incluir:

***Binarização:*** Conversão da imagem para preto e branco puro para aumentar o contraste entre texto e fundo.

***Remoção de Ruído:*** Aplicação de filtros para eliminar artefatos ou manchas presentes na digitalização.

***Deskewing (Endireitamento):*** Correção de pequenas inclinações na imagem para garantir que o texto esteja perfeitamente alinhado.

***Resolução:*** Ajuste da DPI da imagem, se necessário, para garantir que os caracteres tenham detalhes suficientes para o reconhecimento.

### Seleção Interativa de Áreas de Interesse (ROI)

Na segunda etapa será implementado a interação do usuário para definir as regiões das quais as informações serão extraídas.

***Interface de Anotação Visual:*** Será implementada uma interface interativa utilizando a biblioteca streamlit-image-annotation em conjunto com o Streamlit.

***Definição de Retângulos (Bounding Boxes):*** O usuário será capaz de desenhar livremente o retângulo (bounding boxes) sobre a imagem da página. Esse retângulo representará uma região de interesse da qual o texto será extraído.

***Captura de Coordenadas:*** Para o retângulo desenhado, o streamlit-image-annotation retornará um conjunto de coordenadas geométricas (x, y, width, height), representando o canto superior esquerdo e as dimensões da área selecionada. Essas coordenadas serão armazenadas temporariamente no st.session_state para persistência durante a sessão do usuário e para uso nas etapas posteriores.

### Extração de Texto via OCR

Com as áreas de interesse definidas, o foco se volta para a conversão do conteúdo visual em texto legível por máquina.

***Recorte da Imagem:*** Utilizando as coordenadas obtidas na etapa anterior, cada área selecionada será recortada da imagem original da página. Essa etapa é crucial, pois focar o OCR em uma área menor e relevante melhora significativamente a precisão e a velocidade. A biblioteca Pillow (PIL) será utilizada para realizar essas operações de recorte (.crop()).

***Aplicação de OCR:*** O mecanismo de Reconhecimento Óptico de Caracteres será aplicado a imagem recortada. Será utilizada uma implementação de OCR, como o Tesseract OCR Engine (acessado via pytesseract em Python). O Tesseract analisará os pixels da imagem recortada e tentará identificar os caracteres, transformando-os em uma string de texto.

***Pós-processamento de Texto (implementação futura):*** O texto bruto extraído pelo OCR pode conter ruídos ou erros. Etapas de pós-processamento podem ser consideradas:

- ***Limpeza de Caracteres:*** Remoção de caracteres inválidos ou símbolos estranhos.

- ***Correção Simples:*** Correção de erros ortográficos comuns (se um dicionário for aplicável).

- ***Normalização:*** Padronização de formatos (ex: datas, números).

### Geração de Saída Estruturada (CSV)

A fase final do projeto consiste na organização das informações extraídas em um formato de fácil manipulação e análise.

***Associação de Dados:*** O texto extraído de cada área selecionada será associado a um identificador ou rótulo definido pelo usuário.

***Criação do CSV:*** As informações extraídas e seus respectivos rótulos serão compiladas em uma estrutura tabular. A biblioteca pandas será utilizada para criar um DataFrame, facilitando a organização dos dados.

***Exportação:*** O DataFrame será exportado para um arquivo CSV, permitindo que os usuários baixem os dados estruturados para uso em planilhas, bancos de dados ou outras ferramentas de análise.


### Utilizando machine learning (Implementação futura):

- Armazenar os arquivos exportados pelos usuários em um banco de dados para posteriormente serem utilizados em análises mais complexas, criando uma Machine learning que reconheça os arquivos, e possa selecionar a área em que está o texto de interesse, e extrair as informações de forma automática, sem a necessidade de intervenção do usuário.

## ✅ Conclusão 



### 🛠️ Principais Tecnologias utilizadas 
<hr>

- Python 3.12 
- Streamlit
- PDF2image
- Stremalit-Components 
    - streamlit-image-coordinates

### 🚀 Como Executar 
<hr>

~~~BASH

# Clone o repositório 
git clone https://github.com/pvcabral/projeto_visao_computacional.git 

cd projeto_visao_computacional 

# Criando a virtualenv 
python3 -m venv .venv 

# Ativando a virtualenv
source .venv/bin/acivate 

# Instalando as libs
pip install -r requirements.txt 

# Rodando o projeto 
streamlit run app.py


~~~

### 👥  Equipe do Projeto 
<hr>

O desenvolvimento do projeto é realizado por alunos da disciplina de Visão Computacional, ministrada pelo professor Helton Maia da ECT/UFRN: 

Professor Orientador: [Helton Maia](https://heltonmaia.com/) <br>
Aluno: [Paulo Medeiros](https://github.com/pvcabral) <br>
Aluno: [João Victor](https://github.com/BR-Jv)

### 📚 Referências Bibliográficas 
<hr>

- [Streamlit documentation](https://docs.streamlit.io/)

- [Streamlit-Image-Coordinates](https://github.com/blackary/streamlit-image-coordinates)

- [O que é reconhecimento de caractere ópitico(OCR) ?](https://aws.amazon.com/pt/what-is/ocr/)

# Detecção e coleta de informações em documentos técnicos

## 📜 Sumário 

## 🗂️ Estrutura do projeto

## 📌 Introdução 
  
Diante do aumento da digitalização de documentos no contexto da Engenharia Civil,  tornase uma prática comum fazer a extração dessas informações de forma manual, o que demanda tempo e pode levar a erros humanos. Visando reduzir o tempo gasto na busca e organização de dados essenciais para os projetos buscamos desenvolver uma aplicação que permita a extração de dados de documentos digitalizados do contexto da Engenharia Civil, utilizando técnicas de visão computacional e reconhecimento de caractere óptico(OCR) para a automação do processo de extração, assim, aumentando a eficiência e  precisão na manipulação de dados, permitindo que os profissionais da área se concentrem em atividades estratégicas. 

## ⚙️ Desenvolvimento

A aplicação proporciona uma interface voltada para usabilidade do usuário, sendo liberado a sua escolha as informações que deseja utilizar, por meio de planilhas Excel ou CSV, assim, sua implementação é feita no streamlit, devida a sua capacidade de elaboração de protótipos de forma rápida e com qualidade. Assim dividmos a aplicação em 3 etapas : 


### 🔹 Aquisição dos documentos:

- Transformar o PDF em imagem, utilizando a biblioteca pdf2image.
- Criar lógica para o usuário selecionar as coordenadas para a imagem dar um "zoom" na área de interesse, utilizando a biblioteca OpenCV ou Matplotlib.

### 🔹 Processamento dos documentos:

- Utilizar a biblioteca Tesseract OCR para realizar a extração de texto da imagem.
- Solicitar ao usuário quais textos serão extraídos, tendo como chave o primeiro caracter, e o segundo o seu valor. 
- Montar um DataFrame com as informações extraídas, utilizando a biblioteca Pandas e os.

### 🔹 Utilizando machine learning (Implementação posterior):

- Armazenar os arquivos exportados pelos usuários em um banco de dados para posteriormente serem utilizados em análises mais complexas, criando uma Machine learning que reconheça os arquivos, e possa selecionar a área em que está o texto de interesse, e extrair as informações de forma automática, sem a necessidade de intervenção do usuário.

## ✅ Conclusão 

### 🛠️ Principais Tecnolgias utilizadas 

- Python 3.12 
- Streamlit
- PDF2image
- Stremalit-Components 
    - streamlit-image-coordinates

### 🚀 Como Executar 

### 👥  Equipe do Projeto 

O desenvolvimento do projeto é realizado por alunos da disciplina de Visão Computacional, ministrada pelo professor Helton Maia da ECT/UFRN: 

Professor Orientador: [Helton Maia](https://heltonmaia.com/) <br>
Aluno: [Paulo Medeiros](https://github.com/pvcabral) <br>
Aluno: [João Victor](https://github.com/BR-Jv)

### 📚 Referências Bibliográficas 

- [Streamlit documentation](https://docs.streamlit.io/)

- [Streamlit-Image-Coordinates](https://github.com/blackary/streamlit-image-coordinates)

- [O que é reconhecimento de caractere ópitico(OCR) ?](https://aws.amazon.com/pt/what-is/ocr/)
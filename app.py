from streamlit_image_coordinates import streamlit_image_coordinates
from pdf2image import convert_from_bytes
from PIL import ImageDraw, Image
import pandas as pd
import streamlit as st 
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"

#! Melhorar esse argumento 
def get_rectangle_coords(points: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int, int]:
    """
        Função com as coordenadas da Bounding Boxe
    """
    point1, point2 = points
    minx = min(point1[0], point2[0])
    miny = min(point1[1], point2[1])
    maxx = max(point1[0], point2[0])
    maxy = max(point1[1], point2[1])
    return (
        minx,
        miny,
        maxx,
        maxy,
    )

# Inicializa lista de campos na sessão
if "campos_definidos" not in st.session_state:
    st.session_state["campos_definidos"] = []

st.set_page_config(layout="wide")

st.title("📝 Extração de Campos de PDF")

# Entrada do PDF
uploaded_file = st.file_uploader("Escolha um PDF", type="pdf") # Define os tipos aceitos

# Pré-processamento
if uploaded_file is not None: 

    st.success("PDF carregado! Processando...")

    bytes_data = uploaded_file.getvalue()
    # retorna uma lista de objetos -> (Pillow Image)
    images = convert_from_bytes(bytes_data)
   
    st.subheader("Página do PDF convertidas para imagens:")

    if images: 
        
        if "coordinates" not in st.session_state:
            st.session_state["coordinates"] = None

        imgClass = images[0]
    
        # imgResize = imgClass.resize((3000, 3000), resample=Image.BICUBIC) # Define um tamanho pra imagem 
        # img = imgResize.transpose(Image.ROTATE_0) # Rotaciona a imagem 90 graus no sentido anti-horário
        draw = ImageDraw.Draw(imgClass)
        # Aplica um "zoom negativo" (afastamento) na imagem
        zoom_out_factor = 0.55  # 55% do tamanho original (ajuste conforme necessário)
        new_size = (int(imgClass.width * zoom_out_factor), int(imgClass.height * zoom_out_factor))
        imgClass = imgClass.resize(new_size, resample=Image.BICUBIC)

        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"]) # contém tupla com coordenadas 
            draw.rectangle(coords, fill=None, outline="green", width=2) 

        cols = st.columns([9, 3])
        with cols[0]:
            value = streamlit_image_coordinates(imgClass, key="rectangle", click_and_drag=True)
        
        if value is not None:
            point1 = value["x1"], value["y1"]
            point2 = value["x2"], value["y2"]

            print(point1, point2)

            if ( point1[0] != point2[0] and point1[1] != point2[1] and st.session_state["coordinates"] != ((point1, point2))):
                st.session_state["coordinates"] = ((point1, point2))
                st.rerun()
        
        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"])
            new_image = imgClass.crop(coords)
            new_image = new_image.resize(
                (int(new_image.width * 1.5), int(new_image.height * 1.5))
            )
            with cols[1]:
                st.image(new_image)
            
            # *** Inserção para salvar campos ***
            st.write("📌 Coordenadas:", coords)

            drawing_title_text = pytesseract.image_to_string(new_image).strip()
            st.write("🔍 Texto extraído:", drawing_title_text)

            nome_campo = st.text_input("Nome do campo", key="nome_campo_input")

            if st.button("💾 Salvar campo"):
                if nome_campo and coords:
                    st.session_state["campos_definidos"].append({
                        "nome": nome_campo,
                        "coords": coords,
                        "texto": drawing_title_text
                    })
                    st.success(f"Campo '{nome_campo}' salvo com sucesso!")

    # *** Mostrar os campos salvos ***
    if st.session_state["campos_definidos"]:
        st.subheader("📋 Campos definidos:")
        for campo in st.session_state["campos_definidos"]:
            st.write(f"**{campo['nome']}**")
            st.write(f"- Coordenadas: {campo['coords']}")
            st.write(f"- Texto extraído: `{campo['texto']}`")

        if st.button("📥 Exportar para CSV"):
            # Cria um dicionário com nome do campo como chave e texto como valor
            dados_dict = {
                campo["nome"]: campo["texto"]
                for campo in st.session_state["campos_definidos"]
            }

            # Gera um DataFrame com uma única linha
            df = pd.DataFrame([dados_dict])

            # Exibe o DataFrame na interface
            st.dataframe(df)

            # Prepara CSV
            csv = df.to_csv(index=False).encode('utf-8')

            # Botão para baixar CSV
            st.download_button(
                label="⬇️ Baixar CSV com os campos",
                data=csv,
                file_name="campos_extraidos.csv",
                mime="text/csv"
            )

print("rodando...")

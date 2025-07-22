from streamlit_image_coordinates import streamlit_image_coordinates
from pdf2image import convert_from_bytes
from PIL import ImageDraw, Image
import streamlit as st 


#! Melhorar esse argumento 
def get_rectangle_coords( points: tuple[tuple[int, int], tuple[int, int]]) -> tuple[int, int, int, int]:
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

st.set_page_config(layout="wide")

st.title("App simples")

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
    
        imgResize = imgClass.resize((3000, 3000), resample=Image.BICUBIC) # Define um tamanho pra imagem 
        img = imgResize.transpose(Image.ROTATE_90)
        draw = ImageDraw.Draw(img)

        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"]) # contém tupla com coordenadas 
            draw.rectangle(coords, fill=None, outline="green", width=2) 

        cols = st.columns([9, 3])
        with cols[0]:
            value = streamlit_image_coordinates(img, key="rectangle", click_and_drag=True)
        
        if value is not None:
            point1 = value["x1"], value["y1"]
            point2 = value["x2"], value["y2"]

            if ( point1[0] != point2[0] and point1[1] != point2[1] and st.session_state["coordinates"] != (point1, point2)):
                st.session_state["coordinates"] = (point1, point2)
                st.rerun()
        
            if st.session_state["coordinates"]:
                coords = get_rectangle_coords(st.session_state["coordinates"])
                new_image = img.crop(coords)
                new_image = new_image.resize(
                    (int(new_image.width * 1.5), int(new_image.height * 1.5))
                )
                with cols[1]:
                    st.image(new_image)
            
            st.write(coords) # Coordenadas do retangulo do retangulo selecionado

print("rodando...")
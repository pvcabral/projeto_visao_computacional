from streamlit_image_coordinates import streamlit_image_coordinates
from pdf2image import convert_from_bytes
from PIL import ImageDraw
import streamlit as st 



def get_rectangle_coords(
    points: tuple[tuple[int, int], tuple[int, int]],
) -> tuple[int, int, int, int]:
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
uploads = st.file_uploader("Escolha um PDF", type="pdf")

if uploads is not None: 
    st.success("PDF carregado! Processando...")
    content = uploads.read()
    images = convert_from_bytes(content)
    st.subheader("Página do PDF convertidas para imagens:")

    if images: 
        if "coordinates" not in st.session_state:
            st.session_state["coordinates"] = None
        img = images[0]
        draw = ImageDraw.Draw(img)
        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"])
            draw.rectangle(coords, fill=None, outline="green", width=2)
        
        cols = st.columns([9, 4])
        with cols[0]:
            value = streamlit_image_coordinates(img, key="rectangle", click_and_drag=True)
        
        if value is not None:
            point1 = value["x1"], value["y1"]
            point2 = value["x2"], value["y2"]
        
        if (
            point1[0] != point2[0]
            and point1[1] != point2[1]
            and st.session_state["coordinates"] != (point1, point2)
        ):
            st.session_state["coordinates"] = (point1, point2)
            st.rerun()
        
        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"])
            new_image = img.crop(coords)
            new_image = new_image.resize(
                (int(new_image.width * 1.5), int(new_image.height * 1.5))
            )
            with cols[1]:
                st.image(new_image, use_container_width=True)
            
        st.write(coords)


# Use o comando streamlit run app.py para rodar o script

print("rodando...")
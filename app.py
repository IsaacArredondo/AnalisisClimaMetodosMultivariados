import streamlit as st
import pandas as pd
import folium
import geopandas as gpd
from streamlit_folium import folium_static
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Credenciales válidas (puedes cambiarlas según tus necesidades)
USUARIO_VALIDO = "SIMA"
CONTRASEÑA_VALIDA = "Tienen100"

def mostrar_mapa():
    # Carga de datos
    data = pd.read_excel('coordenadas.xlsx')
    st.write(data)

    # Lee el Shapefile con GeoPandas
    nuevoleon = gpd.read_file('./conjunto_de_datos/19ent.shp')

    # Crea un mapa centrado en Nuevo Leon
    m = folium.Map(location=[25.6487734,-100.6149495], zoom_start=7)

    # Añade los límites de Nuevo Leon al mapa
    folium.GeoJson(nuevoleon).add_to(m)

    estaciones_especiales = ["Santa Catarina", "Tec de Nuevo León", "Obispado", "Universidad"]

    for idx, row in data.iterrows():
        # Determina el color del marcador basado en la Clave_Estacion
        color = "green" if row['Clave_Estacion'] not in estaciones_especiales else "red"
        
        folium.Marker(location=[row['Latitud'], row['Longitud']], 
                      icon=folium.Icon(color=color),
                      popup=row['Clave_Estacion']).add_to(m)

    # Muestra el mapa en Streamlit
    folium_static(m)

def mostrar_bienvenida():
    st.title('Bienvenido/a a nuestra aplicación')
    
    # Añadir imagen (asegúrate de tener una imagen llamada "bienvenida.jpg" en la misma carpeta que tu script)
    st.image("bienvenida.jpg", use_column_width=True)
    
    st.write("""
    Este es un espacio donde podrás visualizar diferentes datos y gráficos relacionados con el clima de Nuevo León y estadísticas. 
    Navega a través de las diferentes pestañas para explorar el contenido. ¡Esperamos que sea de tu agrado!
    """)

def mostrar_e1():
    st.title('Estaciónn Obispado')
    
    # Añadir imagen (asegúrate de tener una imagen llamada "bienvenida.jpg" en la misma carpeta que tu script)
    st.image("E1/img1.png", use_column_width=True)
    st.image("E1/img2.png", use_column_width=True)
    st.image("E1/img3.png", use_column_width=True)
    st.image("E1/img4.png", use_column_width=True)
    st.image("E1/img5.png", use_column_width=True)
    st.image("E1/img6.png", use_column_width=True)
    st.image("E1/img7.png", use_column_width=True)
    st.image("E1/img8.png", use_column_width=True)
    st.image("E1/img9.png", use_column_width=True)
    st.image("E1/img10.png", use_column_width=True)
    st.image("E1/img11.png", use_column_width=True)
    st.image("E1/img12.png", use_column_width=True)
    st.image("E1/img13.png", use_column_width=True)
    st.image("E1/img14.png", use_column_width=True)
    st.image("E1/img15.png", use_column_width=True)
    st.image("E1/img16.png", use_column_width=True)

def mostrar_e2():
    st.title('Estación Santa Catarina')
    
    # Añadir imagen (asegúrate de tener una imagen llamada "bienvenida.jpg" en la misma carpeta que tu script)
    st.image("E2/img1.png", use_column_width=True)
    st.image("E2/img2.png", use_column_width=True)
    st.image("E2/img3.png", use_column_width=True)
    st.image("E2/img4.png", use_column_width=True)
    st.image("E2/img5.png", use_column_width=True)
    st.image("E2/img6.png", use_column_width=True)
    st.image("E2/img7.png", use_column_width=True)
    st.image("E2/img8.png", use_column_width=True)
    st.image("E2/img9.png", use_column_width=True)
    st.image("E2/img10.png", use_column_width=True)
    st.image("E2/img11.png", use_column_width=True)
    st.image("E2/img12.png", use_column_width=True)
    st.image("E2/img13.png", use_column_width=True)
    st.image("E2/img14.png", use_column_width=True)
    st.image("E2/img15.png", use_column_width=True)
    st.image("E2/img16.png", use_column_width=True)

def mostrar_e3():
    st.title('Estación TEC NL')
    
    # Añadir imagen (asegúrate de tener una imagen llamada "bienvenida.jpg" en la misma carpeta que tu script)
    st.image("E3/img1.png", use_column_width=True)
    st.image("E3/img2.png", use_column_width=True)
    st.image("E3/img3.png", use_column_width=True)
    st.image("E3/img4.png", use_column_width=True)
    st.image("E3/img5.png", use_column_width=True)
    st.image("E3/img6.png", use_column_width=True)
    st.image("E3/img7.png", use_column_width=True)
    st.image("E3/img8.png", use_column_width=True)
    st.image("E3/img9.png", use_column_width=True)
    st.image("E3/img10.png", use_column_width=True)
    st.image("E3/img11.png", use_column_width=True)
    st.image("E3/img12.png", use_column_width=True)
    st.image("E3/img13.png", use_column_width=True)
    st.image("E3/img14.png", use_column_width=True)
    st.image("E3/img15.png", use_column_width=True)
    st.image("E3/img16.png", use_column_width=True)
def mostrar_e4():
    st.title('Estación Universidad')
    
    # Añadir imagen (asegúrate de tener una imagen llamada "bienvenida.jpg" en la misma carpeta que tu script)
    st.image("E4/img1.png", use_column_width=True)
    st.image("E4/img2.png", use_column_width=True)
    st.image("E4/img3.png", use_column_width=True)
    st.image("E4/img4.png", use_column_width=True)
    st.image("E4/img5.png", use_column_width=True)
    st.image("E4/img6.png", use_column_width=True)
    st.image("E4/img7.png", use_column_width=True)
    st.image("E4/img8.png", use_column_width=True)
    st.image("E4/img9.png", use_column_width=True)
    st.image("E4/img10.png", use_column_width=True)
    st.image("E4/img11.png", use_column_width=True)
    st.image("E4/img12.png", use_column_width=True)
    st.image("E4/img13.png", use_column_width=True)
    st.image("E4/img14.png", use_column_width=True)
    st.image("E4/img15.png", use_column_width=True)
    st.image("E4/img16.png", use_column_width=True)

def login():
    st.sidebar.title("Inicio de sesión")
    usuario = st.sidebar.text_input("Usuario")
    contraseña = st.sidebar.text_input("Contraseña", type='password')
    if st.sidebar.button("Iniciar sesión"):
        if usuario == USUARIO_VALIDO and contraseña == CONTRASEÑA_VALIDA:
            st.session_state.autenticado = True
        else:
            st.sidebar.error("Credenciales inválidas")

def main():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if st.session_state.autenticado:
        st.sidebar.title("Navegación")
        opciones = ["Bienvenida", "Mapa de Nuevo León", "Estación Obispado", "Estación Santa Catarina", "Estación TEC NL", "Estación Universidad"]
        seleccion = st.sidebar.selectbox("Elige una sección:", opciones)

        if st.sidebar.button("Cerrar sesión"):
            st.session_state.autenticado = False
            st.experimental_rerun()

        if seleccion == "Bienvenida":
            mostrar_bienvenida()
        elif seleccion == "Mapa de Nuevo León":
            mostrar_mapa()
        elif seleccion == "Estación Obispado":
            mostrar_e1()
        elif seleccion == "Estación Santa Catarina":
            mostrar_e2()
        elif seleccion == "Estación TEC NL":
            mostrar_e3()
        elif seleccion == "Estación Universidad":
            mostrar_e4()
    else:
        login()

if __name__ == "__main__":
    main()

import streamlit as st
from data import init_db, add_measurement, get_measurements
from data import plot_weight_graph
from datetime import date

st.set_page_config(page_title="Suivi Poids & Mesures", layout="centered")

st.title("📉 Suivi de Poids & Mesures")

# Initialisation de la BDD
init_db()

with st.form("new_data_form"):
    st.subheader("➕ Ajouter une mesure")
    selected_date = st.date_input("📅 Date", value=date.today())
    col1, col2, col3 = st.columns(3)
    with col1:
        poids = st.number_input("Poids (kg)", step=0.05, format="%.2f")
    with col2:
        taille = st.number_input("Tour de taille (cm)", step=0.5, format="%.1f")
    with col3:
        poitrine = st.number_input("Tour de poitrine (cm)", step=0.5, format="%.1f")
    submitted = st.form_submit_button("Ajouter")
    if submitted:
        add_measurement(selected_date, poids, taille, poitrine)
        st.success("Mesure ajoutée avec succès.")

st.divider()
st.subheader("📊 Évolution du poids")
measurements_df = get_measurements()
if not measurements_df.empty:
    plot_weight_graph(measurements_df)
else:
    st.info("Aucune donnée pour le moment.")

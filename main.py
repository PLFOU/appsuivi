import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import date

DB_PATH = "poids_tracker.db"

# Connexion à la base
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM measures ORDER BY date", conn, parse_dates=['date'])
    conn.close()
    return df

def insert_data(selected_date, poids, taille, poitrine):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO measures (date, poids, taille, poitrine)
        VALUES (?, ?, ?, ?)
    """, (selected_date.isoformat(), poids, taille, poitrine))
    conn.commit()
    conn.close()

st.title("📊 Suivi des mesures corporelles")

st.sidebar.header("Ajouter une nouvelle mesure")
col1, col2, col3 = st.sidebar.columns(3)

# Choix de la date
selected_date = st.sidebar.date_input("📅 Date de la mesure", value=date.today())

# Entrée des données
poids = col1.number_input("Poids (kg)", min_value=0.0, step=0.1, format="%.2f")
taille = col2.number_input("Tour de taille (cm)", min_value=0.0, step=0.1, format="%.1f")
poitrine = col3.number_input("Tour de poitrine (cm)", min_value=0.0, step=0.1, format="%.1f")

if st.sidebar.button("💾 Ajouter / Mettre à jour"):
    insert_data(selected_date, poids, taille, poitrine)
    st.success(f"Mesure du {selected_date} enregistrée.")
    st.experimental_rerun()

# Chargement des données
df = load_data()

# Affichage
st.subheader("📈 Évolution du poids")
fig1 = px.line(df, x='date', y='poids', markers=True, title="Poids (kg)")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("📈 Évolution du tour de taille")
fig2 = px.line(df, x='date', y='taille', markers=True, title="Tour de taille (cm)")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("📈 Évolution du tour de poitrine")
fig3 = px.line(df, x='date', y='poitrine', markers=True, title="Tour de poitrine (cm)")
st.plotly_chart(fig3, use_container_width=True)

# Aperçu des données
st.subheader("📋 Données enregistrées")
st.dataframe(df.sort_values(by="date", ascending=False), use_container_width=True)

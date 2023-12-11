import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Datasets
dfE = pd.read_excel("Collection_Experts.xlsx")
dfI = pd.read_excel("Collection_Interventions.xlsx")
dfN = pd.read_excel("Collection_Newsletters.xlsx")
dfR = pd.read_excel("Collection_Recommandations.xlsx")
dfS = pd.read_excel("Collection_Recherches.xlsx")
dfU = pd.read_excel("Collection_Utilisateurs.xlsx")
dfV = pd.read_excel("Collection_Villes.xlsx")

st.set_page_config(page_title="Le département Commerce", page_icon="2️⃣")

st.title("Le département Commerce")

titres_onglets = ["**Nb. de missions**", "**Taux journalier et taux horaire**"]
onglets = st.tabs(titres_onglets)

with onglets[0]:
    st.header("Nombre de missions")

    nombre_total_missions = dfI['Id_Interventions'].nunique()

    st.markdown(f"**Nombre total unique de missions : {nombre_total_missions}**")

with onglets[1]:
    def calculer_stats(colonne):
        min_val = dfE[colonne].min()
        max_val = dfE[colonne].max()
        moyenne = dfE[colonne].mean()  # Calculer la moyenne de toutes les valeurs de la colonne
        return min_val, max_val, moyenne


    min_max_moyenne_tarif_journalier_minimum = calculer_stats('Tarif_Journalier_Minimum')
    min_max_moyenne_tarif_journalier_maximum = calculer_stats('Tarif_Journalier_Maximum')
    min_max_moyenne_tarif_heure_minimum = calculer_stats('Tarif_Heure_Minimum')
    min_max_moyenne_tarif_heure_maximum = calculer_stats('Tarif_Heure_Maximum')

    st.header("Colonne tarif journalier minimum")
    st.markdown(f"""
        Minimum : **{min_max_moyenne_tarif_journalier_minimum[0]} €**\n 
        Maximum : **{min_max_moyenne_tarif_journalier_minimum[1]} €**\n
        Moyenne : **{min_max_moyenne_tarif_journalier_minimum[2]} €**
    """)

    st.header("Colonne tarif journalier maximum")
    st.markdown(f"""
        Minimum : **{min_max_moyenne_tarif_journalier_maximum[0]} €**\n
        Maximum : **{min_max_moyenne_tarif_journalier_maximum[1]} €**\n
        Moyenne : **{min_max_moyenne_tarif_journalier_maximum[2]} €**
    """)

    st.header("Colonne tarif horaire minimum")
    st.markdown(f"""
        Minimum : **{min_max_moyenne_tarif_heure_minimum[0]} €**\n
        Maximum : **{min_max_moyenne_tarif_heure_minimum[1]} €**\n
        Moyenne : **{min_max_moyenne_tarif_heure_minimum[2]} €**
    """)

    st.header("Colonne tarif horaire maximum")
    st.markdown(f"""
        Minimum : **{min_max_moyenne_tarif_heure_maximum[0]} €**\n
        Maximum : **{min_max_moyenne_tarif_heure_maximum[1]} €**\n
        Moyenne : **{min_max_moyenne_tarif_heure_maximum[2]} €**
    """)

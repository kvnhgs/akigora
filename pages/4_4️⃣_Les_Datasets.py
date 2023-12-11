import pandas as pd
import streamlit as st

# Datasets
dfE = pd.read_excel("Collection_Experts.xlsx")
dfI = pd.read_excel("Collection_Interventions.xlsx")
dfN = pd.read_excel("Collection_Newsletters.xlsx")
dfR = pd.read_excel("Collection_Recommandations.xlsx")
dfS = pd.read_excel("Collection_Recherches.xlsx")
dfU = pd.read_excel("Collection_Utilisateurs.xlsx")
dfV = pd.read_excel("Collection_Villes.xlsx")

st.set_page_config(page_title="Les Datasets", page_icon="5️⃣")

st.title("Les Datasets")

st.write("\n")
st.write("\n")
st.write("**Le Dataset Experts :**")
st.dataframe(dfE)

st.write("\n")
st.write("\n")
st.write("**Le Dataset Interventions :**")
st.dataframe(dfI)

st.write("\n")
st.write("\n")
st.write("**Le Dataset Newsletters :**")
st.dataframe(dfN)

st.write("\n")
st.write("\n")
st.write("**Le Dataset Recherches :**")
st.dataframe(dfR)

st.write("\n")
st.write("\n")
st.write("**Le Dataset Recommandations :**")
st.dataframe(dfR)

st.write("\n")
st.write("\n")
st.write("**Le Dataset Utilisateurs :**")
st.dataframe(dfU)
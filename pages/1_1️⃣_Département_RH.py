# Packages
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from streamlit_echarts import st_echarts
from pyecharts import options as opts
from pyecharts.charts import Pie

# Datasets
dfE = pd.read_excel("Collection_Experts.xlsx")
dfI = pd.read_excel("Collection_Interventions.xlsx")
dfN = pd.read_excel("Collection_Newsletters.xlsx")
dfR = pd.read_excel("Collection_Recommandations.xlsx")
dfS = pd.read_excel("Collection_Recherches.xlsx")
dfU = pd.read_excel("Collection_Utilisateurs.xlsx")
dfV = pd.read_excel("Collection_Villes.xlsx")

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set(style="whitegrid")

st.set_page_config(page_title="Le département RH", page_icon="1️⃣")

st.title("Le département RH")

titres_onglets = ["**Nb. experts inscrits / mois**", "**Nb. experts visibles**", "**% de profil complétés**",
                  "**% d'experts par activité**", "**Nb. d'experts / ville**", "**Nb. experts / région**", "**% LinkedIn**"]
onglets = st.tabs(titres_onglets)

with onglets[0]:
    st.header("Nombre d'experts inscrits sur la plateforme en fonction du mois")

    dfE['Date'] = pd.to_datetime(dfE['Date'], format='%d/%m/%Y')
    dfE['Mois'] = dfE['Date'].dt.to_period("M")
    df_experts_par_mois = dfE.groupby('Mois')['Id_Experts'].count().reset_index()

    plt.figure(figsize=(10, 8))

    all_months_option = "Tous les mois"
    months_list = [all_months_option] + df_experts_par_mois['Mois'].astype(str).tolist()
    selected_months = st.multiselect('**Sélectionner les mois**', months_list, default=[all_months_option])
    if all_months_option in selected_months:
        filtered_df = df_experts_par_mois
    else:
        filtered_df = df_experts_par_mois[df_experts_par_mois['Mois'].astype(str).isin(selected_months)]

    if len(selected_months) == 1:
        phrase = f"**{filtered_df['Id_Experts'].sum()} experts se sont inscrits au mois de {selected_months[0]}**"
    elif all_months_option in selected_months:
        phrase = f"**{filtered_df['Id_Experts'].sum()} experts se sont inscrits au total**"
    else:
        phrase = f"**{filtered_df['Id_Experts'].sum()} experts se sont inscrits aux mois de {', '.join(selected_months)}**"
    st.markdown(f"**{phrase}**")

    sns.barplot(x=filtered_df['Mois'], y=filtered_df['Id_Experts'],
                color="red", edgecolor="black", linewidth=3, width=0.5)
    plt.xlabel('Mois', size=20)
    plt.ylabel('Nombre d\'experts', size=20)
    plt.xticks(rotation=45)
    st.pyplot()

with onglets[1]:
    st.header("Nombre d'experts visibles sur la plateforme")

    visibility_counts = dfE['Visibilité'].value_counts()
    total_users = len(dfE)
    percentage_visible = (visibility_counts[True] / total_users) * 100
    percentage_not_visible = (visibility_counts[False] / total_users) * 100

    st.markdown(f"**{percentage_visible:.1f}% des utilisateurs sont visibles sur la plateforme.**")

    fig = px.pie(
        names=['Visible', 'Non visible'],
        values=[percentage_visible, percentage_not_visible],
        labels={'percentage_visible': 'Visible', 'percentage_not_visible': 'Non visible'},
    )
    fig.update_traces(
        marker=dict(colors=['black', 'red'], line=dict(color='black', width=3)),
        textinfo='label+percent',
    )
    fig.update_layout(
        font=dict(size=20),
        showlegend=False,
    )

    st.plotly_chart(fig)

with onglets[2]:
    st.header("Nombre d'experts avec le pourcentage des profils complétés")

    grouped_data = dfE.groupby("Pourcentage_Profil_Complété")["Id_Experts"].nunique().reset_index()
    grouped_data.columns = ["Pourcentage", "Count_Experts"]
    average_percentage_all_data = dfE["Pourcentage_Profil_Complété"].mean()
    pourcentage_options = grouped_data["Pourcentage"].unique().tolist()

    # Intégrer "Toutes les données" au multiselect et le sélectionner par défaut
    selected_percentages = st.multiselect("**Sélectionner les pourcentages**",
                                          ["Toutes les données"] + pourcentage_options,
                                          default=["Toutes les données"])

    if "Toutes les données" in selected_percentages:
        filtered_data = grouped_data
        selected_percentages_str = "Toutes les données"
    else:
        filtered_data = grouped_data[grouped_data["Pourcentage"].isin(selected_percentages)]
        selected_percentages_str = ", ".join(map(str, selected_percentages))

    total_experts = filtered_data["Count_Experts"].sum()

    if "Toutes les données" in selected_percentages:
        st.markdown(
            f"**{total_experts} experts ont rempli leur profil à {average_percentage_all_data:.2f}% en moyenne**")
    else:
        st.markdown(f"**{total_experts} experts ont rempli leur profil à {selected_percentages_str}%**")

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(x="Pourcentage", y="Count_Experts", data=filtered_data, ax=ax,
                color="red", edgecolor="black", linewidth=2, width=0.5)
    ax.set_xlabel("Pourcentage de profils complétés", size=20)
    ax.set_ylabel("Nombre d'experts", size=20)
    st.pyplot(fig)

with onglets[3]:
    st.header("Pourcentage d'experts par domaine d'activité")

    domaines_options = ["Tous les domaines d'activités"] + list(dfE["Domaine_D'activité"].unique())

    selected_domaines = st.multiselect("**Choisissez les domaines d'activité**", domaines_options,
                                       default=["Tous les domaines d'activités"])

    if "Tous les domaines d'activités" not in selected_domaines:
        filtered_df = dfE[dfE["Domaine_D'activité"].isin(selected_domaines)]
    else:
        filtered_df = dfE

    domaine_counts = filtered_df["Domaine_D'activité"].value_counts()
    domaine_counts = domaine_counts.sort_values(ascending=True)
    filtered_df = filtered_df.set_index("Domaine_D'activité").loc[domaine_counts.index].reset_index()

    for domaine in selected_domaines:
        if domaine != "Tous les domaines d'activités":
            experts_count = filtered_df[filtered_df["Domaine_D'activité"] == domaine]['Id_Experts'].nunique()
            st.markdown(f"**Il y a {experts_count} experts dans le domaine d'activité {domaine}**.")

    plt.figure(figsize=(14, 11))
    sns.countplot(data=filtered_df, x="Domaine_D'activité",
                  color="red", edgecolor="black", linewidth=2, width=0.5)
    plt.xlabel("Domaine d'activité", size=30)
    plt.ylabel("Nombre d'experts", size=30)
    plt.xticks(rotation=45, ha='right')
    st.pyplot(plt)

with onglets[4]:
    st.header("Nombre d'experts par ville (Top 10 et les autres)")

    experts_par_ville = dfE.groupby("Location")["Id_Experts"].nunique().reset_index()
    experts_par_ville = experts_par_ville.sort_values(by="Id_Experts", ascending=False)
    top_10_villes = experts_par_ville.head(10)
    reste = pd.DataFrame({"Location": ["Autres"], "Id_Experts": [experts_par_ville.iloc[10:, 1].sum()]})
    grouped_data = pd.concat([top_10_villes, reste])
    selected_villes = st.multiselect("**Choisissez les villes**", grouped_data["Location"])

    for ville in selected_villes:
        if ville == "Autres":
            experts_count = grouped_data[grouped_data["Location"] == "Autres"]['Id_Experts'].values[0]
            total_experts = grouped_data["Id_Experts"].sum()
            percentage = (experts_count / total_experts) * 100
            st.markdown(
                f"**Il y a {experts_count} experts dans les autres villes, ce qui représente {percentage:.2f}% des experts.**")
        else:
            experts_count = grouped_data[grouped_data["Location"] == ville]['Id_Experts'].values[0]
            total_experts = grouped_data["Id_Experts"].sum()
            percentage = (experts_count / total_experts) * 100
            st.markdown(
                f"**Il y a {experts_count} experts à {ville}, ce qui représente {percentage:.2f}% des experts.**")

    fig, ax = plt.subplots(figsize=(10, 8))
    grouped_data = grouped_data.sort_values(by="Id_Experts", ascending=True)
    ax.barh(grouped_data["Location"], grouped_data["Id_Experts"],
            color="red", edgecolor="black", linewidth=2, height=0.5)
    ax.set_xlabel("Nombre d'experts", size=20)
    ax.set_ylabel("Ville", size=20)
    st.pyplot(fig)

with onglets[5]:
    st.header("Nombre d'experts par région")

    experts_par_region = dfV.groupby("Région")["Ville"].count().reset_index()
    experts_par_region.columns = ["Région", "Nombre_Villes"]
    experts_par_region = experts_par_region.sort_values(by="Nombre_Villes", ascending=False)
    top_10_regions = experts_par_region.head(10)
    reste_regions = pd.DataFrame({"Région": ["Autres"], "Nombre_Villes": [experts_par_region.iloc[10:, 1].sum()]})
    grouped_data_regions = pd.concat([top_10_regions, reste_regions])

    regions_list = grouped_data_regions["Région"].tolist()
    regions_list.insert(0, "Toutes les régions")
    selected_regions = st.multiselect("**Choisissez les régions**", regions_list)

    if "Toutes les régions" in selected_regions:
        selected_regions = grouped_data_regions["Région"].tolist()  # Sélectionner toutes les régions par défaut

    for region in selected_regions:
        if region == "Autres":
            experts_count = grouped_data_regions[grouped_data_regions["Région"] == "Autres"]['Nombre_Villes'].values[0]
            total_villes = grouped_data_regions["Nombre_Villes"].sum()
            percentage = (experts_count / total_villes) * 100
            st.markdown(
                f"**Il y a {experts_count} villes dans les autres régions, ce qui représente {percentage:.2f}% des villes.**")
        else:
            experts_count = grouped_data_regions[grouped_data_regions["Région"] == region]['Nombre_Villes'].values[0]
            total_villes = grouped_data_regions["Nombre_Villes"].sum()
            percentage = (experts_count / total_villes) * 100
            st.markdown(
                f"**Il y a {experts_count} villes dans la région {region}, ce qui représente {percentage:.2f}% des villes.**")

    fig, ax = plt.subplots(figsize=(10, 8))
    grouped_data_regions = grouped_data_regions.sort_values(by="Nombre_Villes", ascending=True)
    ax.barh(grouped_data_regions["Région"], grouped_data_regions["Nombre_Villes"],
            color="red", edgecolor="black", linewidth=2, height=0.5)
    ax.set_xlabel("Nombre de Villes", size=25)
    ax.set_ylabel("Région", size=25)
    st.pyplot(fig)

with onglets[6]:
    st.header("Pourcentage d'importation de profil LinkedIn")

    import_counts = dfE['Import_LinkedIn'].value_counts()
    total_users = len(dfE)
    percentage_linked_in = (import_counts[True] / total_users) * 100
    percentage_not_linked_in = (import_counts[False] / total_users) * 100

    st.markdown(f"**{percentage_linked_in:.1f}% des utilisateurs ont effectué une importation LinkedIn.**")

    fig = px.pie(
        names=['LinkedIn', 'Non LinkedIn'],
        values=[percentage_linked_in, percentage_not_linked_in],
        labels={'percentage_linked_in': 'LinkedIn', 'percentage_not_linked_in': 'Non LinkedIn'},
    )
    fig.update_traces(
        marker=dict(colors=['black', 'red'], line=dict(color='black', width=3)),
        textinfo='label+percent',
    )
    fig.update_layout(
        font=dict(size=20),
        showlegend=False,
    )

    st.plotly_chart(fig)

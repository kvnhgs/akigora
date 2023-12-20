from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
from streamlit_extras.metric_cards import style_metric_cards


# Datasets
def load_data(file_name):
    return pd.read_excel(file_name)


dfE = load_data("Collection_Experts.xlsx")
dfI = load_data("Collection_Interventions.xlsx")
dfN = load_data("Collection_Newsletters.xlsx")
dfR = load_data("Collection_Recommandations.xlsx")
dfS = load_data("Collection_Recherches.xlsx")
dfU = load_data("Collection_Utilisateurs.xlsx")
dfV = load_data("Collection_Villes.xlsx")
dfC = load_data("Collection_Clients.xlsx")
dfCT = load_data("Collection_Consultations.xlsx")

# Config menu
st.set_page_config(
    page_title="AKIGORA BY KVN HGS",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set(style="whitegrid")
style_metric_cards(background_color="#FFFFFF", border_left_color="#DE1F1F", box_shadow=True)

selected = option_menu(
    menu_title="DASHBOARD AKIGORA BETA",
    options=["Projet", "RH", "Commercial", "Marketing", "Datasets"],
    icons=["laptop", "people-fill", "currency-euro", "building-check", "database-lock", "check-circle-fill"],
    menu_icon="laptop",
    default_index=0,
    orientation="horizontal"
)

# Fonctions graphiques


def create_bar_chart(data, x, y, rotation=45):
    plt.figure(figsize=(10, 8))
    sns.barplot(data=data, x=x, y=y, color="red", edgecolor="black", linewidth=3)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=rotation)
    st.pyplot()


def create_pie_chart(names, values, colors=None, line_color='black', line_width=3):
    fig = px.pie(names=names, values=values)
    fig.update_traces(marker=dict(colors=colors if colors else ['black', 'red'],
                                  line=dict(color=line_color, width=line_width)), textinfo='label+percent')
    fig.update_layout(font=dict(size=20), showlegend=True)
    st.plotly_chart(fig)


def create_countplot(data, x, xlabel, ylabel, rotation=45, color="red", figsize=(14, 11)):
    plt.figure(figsize=figsize)
    sns.countplot(data=data, x=x, color=color, edgecolor="black", linewidth=2, width=0.5)
    plt.xlabel(xlabel, size=20)
    plt.ylabel(ylabel, size=20)
    plt.xticks(rotation=rotation, ha='right')
    st.pyplot()


def create_barh_chart(data, x, y, xlabel, ylabel, figsize=(10, 8), color="red", linewidth=2):
    fig, ax = plt.subplots(figsize=figsize)
    data = data.sort_values(by=x, ascending=True)
    ax.barh(data[y], data[x], color=color, edgecolor="black", linewidth=linewidth)
    ax.set_xlabel(xlabel, size=20)
    ax.set_ylabel(ylabel, size=20)
    st.pyplot(fig)

if selected == "Projet":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:

        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/kvn-hgs-le-logo.png)](https://www.kvn-hgs.com/)")
        st.subheader("Analyse de données par Kévin HEUGAS")
        st.subheader("Data Analyst & Développeur en Intelligence Artificielle")
        st.subheader("Recherche alternance")
        st.write("J’ai le plaisir de vous annoncer que j’ai commencé mon diplôme de Data Analyst et Développeur en "
                 "Intelligence Artificielle à Simplon Nouvelle Aquitaine (École IA Microsoft By Simplon) à Bayonne.")
        st.write("Je suis à la recherche d’une alternance à partir du 8 janvier 2024 jusqu’au 9 mai 2025. Cette alternance "
                 "me permettra de créer une IA ou bien de mettre à profit mes compétences en data analyse et gestion de "
                 "projet digitaux. Le but principal étant de participer au développement et à la pérennité de votre "
                 "entreprise. Les outils technologiques devenant un axe d’évolution et stratégique incontournable.")

        add_vertical_space(1)
        links_row = row(2, vertical_align="center")
        links_row.link_button(
            "📲 Dossier de candidature et CV",
            "https://www.kvn-hgs.com/recherche-alternance/",
            use_container_width=True,
        )
        links_row.link_button(
            "📲 Contact KVN HGS",
            "https://www.kvn-hgs.com/contact/",
            use_container_width=True,
        )

        links_row = row(2, vertical_align="center")
        links_row.link_button(
            "🌐 GIT",
            "https://github.com/kvnhgs/",
            use_container_width=True,
        )
        links_row.link_button(
            "🌐 LINKEDIN",
            "https://www.linkedin.com/in/kevinheugas/",
            use_container_width=True,
        )


    with col3:
        st.empty()

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    col6, col7, col8 = st.columns([0.3, 0.4, 0.3])

    with col6:
        st.empty()

    with col7:
        st.subheader("École Microsoft IA by SIMPLON")
        st.write("Ce projet s'inscrit dans le cadre de la formation Data Analyst et Développeur en Intelligence "
                 "Artificielle à l'École IA Microsft by SIMPLON à Bayonne")
        st.write("Depuis 5 ans, Simplon opère à Bayonne afin de proposer des parcours allant de 6 semaines à 19 mois. "
                 "Notre objectif : vous permettre de booster votre employabilité et intégrer une entreprise du "
                 "territoire. Nous proposons majoritairement des formations en alternance accessibles à toutes et tous "
                 "sans prérequis de diplôme, mais également des parcours dédiés à des talents souhaitant se lancer dans "
                 "l'entreprenariat et ayant besoin de compétences techniques ! Vous souhaitez vous former ou vous "
                 "reconvertir dans les métiers du numérique ?")
        st.link_button("Contact SIMPLON", "https://nouvelleaquitaine.simplon.co/simplon-euskadi.html")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/simplon-simplon.png)]"
                    "(https://nouvelleaquitaine.simplon.co/simplon-euskadi.html)")

        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.subheader("Le contexte du projet")
        st.write("Le projet de Data Visualization vise à permettre à un groupe d'étudiants de créer un dashboard "
                 "einteractif pour visualiser divers indicateurs. Ces indicateurs sont disponibles aujourd’hui grâce "
                 "aux données que nous exploitons en interne. Nous manquons aujourd’hui d’un outil pour nous permettre "
                 "d’observer l’évolution de nos données dans le temps. Ces données sont de types variables, il peut "
                 "s’agir de données sur les inscriptions, de données financières, de données sur l’utilisation de la "
                 "plateforme etc.")
        st.write("Le projet consiste à concevoir et développer un dashboard interactif qui offre une visualisation "
                 "claire et efficace des indicateurs de données sélectionnés et communiqués aux étudiants.")
        st.link_button("Contact AKIGORA", "https://akigora.com/")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/akigora-akigora.png)](https://akigora.com/)")

    with col8:
        st.empty()

if selected == "RH":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département RH")

        titres_onglets = ["**Nb. experts inscrits / mois**", "**Nb. experts visibles**", "**% de profil complétés**",
                          "**Nb. d'experts par activité**", "**Nb. d'experts / ville**", "**Nb. d'experts / région**",
                          "**% d'entretiens**", "**% LinkedIn**"]
        onglets = st.tabs(titres_onglets)

        with onglets[0]:
            st.header("Nombre d'experts inscrits sur la plateforme en fonction du mois")

            dfE['Date'] = pd.to_datetime(dfE['Date'], format='%d/%m/%Y')
            dfE['Mois'] = dfE['Date'].dt.to_period("M")
            df_experts_par_mois = dfE.groupby('Mois')['Id_Experts'].count().reset_index()
            df_experts_par_mois['Mois_Str'] = df_experts_par_mois['Mois'].dt.strftime('%B %Y')
            months_list = df_experts_par_mois['Mois_Str'].tolist()

            min_index, max_index = st.select_slider('**Sélectionner la plage de mois**',
                                                    options=range(len(months_list)),
                                                    value=(0, len(months_list) - 1),
                                                    format_func=lambda x: months_list[x])

            filtered_df = df_experts_par_mois.iloc[min_index:max_index + 1]
            start_month = months_list[min_index]
            end_month = months_list[max_index]
            phrase = f"**{filtered_df['Id_Experts'].sum()} experts** se sont inscrits entre **{start_month}** et **{end_month}**."
            st.markdown(f"{phrase}")

            create_bar_chart(filtered_df, 'Mois', 'Id_Experts')

        with onglets[1]:
            st.header("Nombre d'experts visibles sur la plateforme")

            visibility_counts = dfE['Visibilité'].value_counts()
            total_users = len(dfE)
            percentage_visible = (visibility_counts[True] / total_users) * 100
            percentage_not_visible = (visibility_counts[False] / total_users) * 100

            st.markdown(f"**{percentage_visible:.1f}% des utilisateurs** sont visibles sur la plateforme.")

            create_pie_chart(
                names=['Visible', 'Non visible'],
                values=[percentage_visible, percentage_not_visible],
            )

        with onglets[2]:
            st.header("Nombre d'experts avec le pourcentage des profils complétés")

            dfE['Date'] = pd.to_datetime(dfE['Date'], format='%d/%m/%Y')
            dfE['Mois'] = dfE['Date'].dt.to_period("M")

            grouped_data = dfE.groupby("Pourcentage_Profil_Complété")["Id_Experts"].nunique().reset_index()
            grouped_data.columns = ["Pourcentage", "Nombre experts"]

            min_percentage = grouped_data["Pourcentage"].min()
            max_percentage = grouped_data["Pourcentage"].max()

            selected_range = st.slider('**Sélectionner la plage de pourcentages**',
                                       min_value=min_percentage,
                                       max_value=max_percentage,
                                       value=(min_percentage, max_percentage))

            filtered_data = grouped_data[(grouped_data["Pourcentage"] >= selected_range[0]) &
                                         (grouped_data["Pourcentage"] <= selected_range[1])]

            total_experts = filtered_data["Nombre experts"].sum()
            average_percentage = filtered_data["Pourcentage"].mean()

            st.markdown(
                f"**{total_experts} experts** ont rempli leur profil à **{average_percentage:.2f}%** en moyenne dans la plage sélectionnée.")

            create_bar_chart(filtered_data, 'Pourcentage', 'Nombre experts')

        with onglets[3]:
            st.header("Nombre d'experts par domaine d'activité")

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

            create_countplot(filtered_df, "Domaine_D'activité", "Répartition des Experts par Domaine d'Activité",
                             "Domaine d'activité", 45)

        with onglets[4]:
            st.header("Nombre d'experts par ville (Top 10 et les autres)")

            experts_par_ville = dfE.groupby("Ville")["Id_Experts"].nunique().reset_index()
            experts_par_ville = experts_par_ville.sort_values(by="Id_Experts", ascending=False)
            top_10_villes = experts_par_ville.head(10)
            reste = pd.DataFrame({"Ville": ["Autres"], "Id_Experts": [experts_par_ville.iloc[10:, 1].sum()]})
            grouped_data = pd.concat([top_10_villes, reste])

            min_experts = grouped_data["Id_Experts"].min()
            max_experts = grouped_data["Id_Experts"].max()

            selected_experts_range = st.slider('**Sélectionner la plage du nombre d’experts**',
                                               min_value=min_experts,
                                               max_value=max_experts,
                                               value=(min_experts, max_experts))

            filtered_data = grouped_data[(grouped_data["Id_Experts"] >= selected_experts_range[0]) &
                                         (grouped_data["Id_Experts"] <= selected_experts_range[1])]

            for index, row in filtered_data.iterrows():
                st.markdown(f"Il y a **{row['Id_Experts']} experts** dans la ville de **{row['Ville']}**.")

            create_barh_chart(filtered_data, 'Id_Experts', 'Ville', 'Nombre d\'experts', 'Ville')

        with onglets[5]:
            st.header("Nombre d'experts par région")

            combined_data = pd.merge(dfE, dfV, on="Ville", how="left")

            experts_par_region = combined_data.groupby("Région")["Id_Experts"].nunique().reset_index()
            experts_par_region.columns = ["Région", "Nombre_Experts"]
            experts_par_region = experts_par_region.sort_values(by="Nombre_Experts", ascending=False)

            if len(experts_par_region) > 10:
                top_10_regions = experts_par_region.head(10)
                reste_regions = pd.DataFrame(
                    {"Région": ["Autres"], "Nombre_Experts": [experts_par_region.iloc[10:, 1].sum()]})
                grouped_data_regions = pd.concat([top_10_regions, reste_regions])
            else:
                grouped_data_regions = experts_par_region

            min_experts = grouped_data_regions["Nombre_Experts"].min()
            max_experts = grouped_data_regions["Nombre_Experts"].max()

            selected_experts_range = st.slider('**Sélectionner la plage du nombre d’experts par région**',
                                               min_value=min_experts,
                                               max_value=max_experts,
                                               value=(min_experts, max_experts))

            filtered_data_regions = grouped_data_regions[
                (grouped_data_regions["Nombre_Experts"] >= selected_experts_range[0]) &
                (grouped_data_regions["Nombre_Experts"] <= selected_experts_range[1])]

            total_experts = filtered_data_regions['Nombre_Experts'].sum()
            st.markdown(f"Il y a **{total_experts} experts** dans les régions sélectionnées.")

            for index, row in filtered_data_regions.iterrows():
                st.markdown(f"Il y a **{row['Nombre_Experts']} experts** dans la région **{row['Région']}**.")

            fig, ax = plt.subplots(figsize=(10, 8))
            filtered_data_regions = filtered_data_regions.sort_values(by="Nombre_Experts", ascending=True)
            ax.barh(filtered_data_regions["Région"], filtered_data_regions["Nombre_Experts"],
                    color="red", edgecolor="black", linewidth=2, height=0.5)
            ax.set_xlabel("Nombre d'experts", size=20)
            ax.set_ylabel("Région", size=20)
            st.pyplot(fig)

        with onglets[6]:
            st.header("Pourcentage d'entretiens passés")

            entretien_counts = dfE['Done'].value_counts()
            total_entretiens = len(dfE)
            percentage_passed = (entretien_counts[True] / total_entretiens) * 100
            percentage_not_passed = (entretien_counts[False] / total_entretiens) * 100

            st.markdown(f"**{percentage_passed:.1f}% des utilisateurs** ont passé un entretien.")

            create_pie_chart(
                names=['Entretien Passé', 'Entretien Non Passé'],
                values=[percentage_passed, percentage_not_passed],
            )

        with onglets[7]:
            st.header("Pourcentage d'importation de profil LinkedIn")

            import_counts = dfE['Import_LinkedIn'].value_counts()
            total_users = len(dfE)
            percentage_linked_in = (import_counts[True] / total_users) * 100
            percentage_not_linked_in = (import_counts[False] / total_users) * 100

            st.markdown(f"**{percentage_linked_in:.1f}% des utilisateurs** ont effectué une importation LinkedIn.")

            create_pie_chart(
                names=['LinkedIn', 'Non LinkedIn'],
                values=[percentage_linked_in, percentage_not_linked_in],
            )

    with col3:
        st.empty()

if selected == "Commercial":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département Commercial")

        titres_onglets = ["**Nb. de missions**", "**Tarif journalier et tarif horaire**", "**Nb. d'écoles et d'entreprises**"]
        onglets = st.tabs(titres_onglets)

        with onglets[0]:
            st.header("Nombre de missions")

            nombre_total_missions = dfI['Id_Interventions'].nunique()
            total_heures = round(dfI['Nombre_Heures'].sum())
            moyenne_heures = round(dfI['Nombre_Heures'].mean())

            st.metric(label="Nombre total unique de missions", value=f"{nombre_total_missions}")
            st.metric(label="Somme totale des heures", value=f"{total_heures} heures")
            st.metric(label="Durée moyenne des missions", value=f"{moyenne_heures} heures")

        with onglets[1]:
            def calculer_stats(colonne):
                min_val = round(dfE[colonne].min())
                max_val = round(dfE[colonne].max())
                moyenne = round(dfE[colonne].mean())
                return min_val, max_val, moyenne


            min_max_moyenne_tarif_journalier_minimum = calculer_stats('Tarif_Journalier_Minimum')
            min_max_moyenne_tarif_journalier_maximum = calculer_stats('Tarif_Journalier_Maximum')
            min_max_moyenne_tarif_heure_minimum = calculer_stats('Tarif_Heure_Minimum')
            min_max_moyenne_tarif_heure_maximum = calculer_stats('Tarif_Heure_Maximum')

            st.header("Tarif journalier minimum")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Minimum", value=f"{min_max_moyenne_tarif_journalier_minimum[0]} €")
            with col2:
                st.metric(label="Maximum", value=f"{min_max_moyenne_tarif_journalier_minimum[1]} €")
            with col3:
                st.metric(label="Moyenne", value=f"{min_max_moyenne_tarif_journalier_minimum[2]} €")

            st.header("Tarif journalier maximum")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Minimum", value=f"{min_max_moyenne_tarif_journalier_maximum[0]} €")
            with col2:
                st.metric(label="Maximum", value=f"{min_max_moyenne_tarif_journalier_maximum[1]} €")
            with col3:
                st.metric(label="Moyenne", value=f"{min_max_moyenne_tarif_journalier_maximum[2]} €")

            st.header("Tarif heure minimum")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Minimum", value=f"{min_max_moyenne_tarif_heure_minimum[0]} €")
            with col2:
                st.metric(label="Maximum", value=f"{min_max_moyenne_tarif_heure_minimum[1]} €")
            with col3:
                st.metric(label="Moyenne", value=f"{min_max_moyenne_tarif_heure_minimum[2]} €")

            st.header("Tarif heure maximum")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(label="Minimum", value=f"{min_max_moyenne_tarif_heure_maximum[0]} €")
            with col2:
                st.metric(label="Maximum", value=f"{min_max_moyenne_tarif_heure_maximum[1]} €")
            with col3:
                st.metric(label="Moyenne", value=f"{min_max_moyenne_tarif_heure_maximum[2]} €")

        with onglets[2]:
            st.header("Nombre d'écoles et d'entreprises clientes")

            nombre_ecoles = len(dfC[dfC['Entreprise_Ecole'] == 'school'])
            nombre_entreprises = len(dfC[dfC['Entreprise_Ecole'] == 'company'])
            total = nombre_ecoles + nombre_entreprises
            pourcentage_ecoles = (nombre_ecoles / total) * 100
            pourcentage_entreprises = (nombre_entreprises / total) * 100
            labels = ['Écoles', 'Entreprises']
            values = [pourcentage_ecoles, pourcentage_entreprises]

            st.markdown(
                f"Il y a **{nombre_ecoles} écoles ({pourcentage_ecoles:.2f}%)** et **{nombre_entreprises} entreprises "
                f"({pourcentage_entreprises:.2f}%)**.")

            create_pie_chart(
                names=['Écoles', 'Entreprises'],
                values=[pourcentage_ecoles, pourcentage_entreprises],
            )

    with col3:
        st.empty()

if selected == "Marketing":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département Marketing")

        titres_onglets = ["**Nb. de recherches**", "**Nb. consultations**"]
        onglets = st.tabs(titres_onglets)

        with onglets[0]:
            st.header("Nombre de recherches")

            dfS['Date_Recherche'] = pd.to_datetime(dfS['Date_Recherche'], format='%d/%m/%Y')

            nombre_recherches = dfS['Id_Recherches'].nunique()
            st.markdown(f"Le nombre total de recherches est : **{nombre_recherches}**")

            dfS_grouped = dfS.groupby(dfS['Date_Recherche'].dt.date)['Id_Recherches'].nunique().reset_index()
            dfS_grouped.columns = ['Date', 'Nombre_Recherches']

            min_date = dfS_grouped['Date'].min()
            max_date = dfS_grouped['Date'].max()

            selected_date_range = st.slider('**Sélectionner la plage de dates**',
                                            min_value=min_date,
                                            max_value=max_date,
                                            value=(min_date, max_date),
                                            format="DD/MM/YYYY")

            filtered_data = dfS_grouped[(dfS_grouped['Date'] >= selected_date_range[0]) &
                                       (dfS_grouped['Date'] <= selected_date_range[1])]

            nombre_recherches_filtrees = filtered_data['Nombre_Recherches'].sum()
            st.markdown(
               f"Il y a **{nombre_recherches_filtrees} recherches** entre le **{selected_date_range[0].strftime('%d/%m/%Y')}**"
               f" et le **{selected_date_range[1].strftime('%d/%m/%Y')}**.")

            fig, ax = plt.subplots(figsize=(10, 8))
            sns.lineplot(x='Date', y='Nombre_Recherches', data=filtered_data, ax=ax, marker='o', color='red',
                        markersize=10, linewidth=1)
            ax.set_xlabel("Date", size=20)
            ax.set_ylabel("Nombre de Recherches", size=20)
            plt.xticks(rotation=45)
            st.pyplot(fig)

        with onglets[1]:
            st.header("Nombre de consultations (Top 10)")

            nombre_total_consultations = dfCT['Id_Consultations'].nunique()
            st.markdown(f"Nombre total de consultations : **{nombre_total_consultations}**.")

            consultations_par_expert = dfCT.groupby('Id_Experts')['Id_Consultations'].nunique().reset_index()
            consultations_par_expert.columns = ['Id_Experts', 'Nombre_Consultations']
            consultations_par_expert = consultations_par_expert.sort_values(by='Nombre_Consultations', ascending=False)

            top_10_experts = consultations_par_expert.head(10)

            create_bar_chart(top_10_experts, 'Nombre_Consultations', 'Id_Experts')

            markdown_text = "Liste de tous les experts et leurs nombres de consultations :\n"
            for index, row in consultations_par_expert.iterrows():
                markdown_text += f"- Expert ID: **{row['Id_Experts']}** a **{row['Nombre_Consultations']}** consultations.\n"

            st.markdown(markdown_text)

    with col3:
        st.empty()

if selected == "Datasets":
    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Les Datasets")

    with col3:
        st.empty()

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
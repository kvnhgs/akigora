from streamlit_option_menu import option_menu
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Datasets
dfE = pd.read_excel("Collection_Experts.xlsx")
dfI = pd.read_excel("Collection_Interventions.xlsx")
dfN = pd.read_excel("Collection_Newsletters.xlsx")
dfR = pd.read_excel("Collection_Recommandations.xlsx")
dfS = pd.read_excel("Collection_Recherches.xlsx")
dfU = pd.read_excel("Collection_Utilisateurs.xlsx")
dfV = pd.read_excel("Collection_Villes.xlsx")
dfC = pd.read_excel("Collection_Clients.xlsx")

#Config menu
st.set_page_config(
    page_title="AKIGORA BY KVN HGS",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set(style="whitegrid")

selected = option_menu(
    menu_title="DASHBOARD AKIGORA",
    options=["Projet", "RH", "Commercial", "Marketing", "Datasets"],
    icons=["laptop", "people-fill", "currency-euro", "building-check", "database-lock", "check-circle-fill"],
    menu_icon="laptop",
    default_index=0,
    orientation="horizontal"
)

if selected == "Projet":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:

        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/kvn-hgs-le-logo.png)](https://www.kvn-hgs.com/)")
        st.subheader("Analyse de données par Kévin HEUGAS")
        st.subheader("Data Analyst & Développeur en Intelligence Artificielle")
        st.link_button("📲 Contactez KVN HGS", "https://www.kvn-hgs.com/contact/")
        st.link_button("🌐 LINKEDIN", "https://www.linkedin.com/in/kevinheugas/")


    with col3:
        st.empty()

    st.write("\n")
    st.write("\n")
    col6, col7, col8, col9 = st.columns([0.2, 0.3, 0.3, 0.2])

    with col6:
        st.empty()

    with col7:
        st.subheader("École Microsoft IA by SIMPLON")
        st.write("Ce projet s'inscrit dans le cadre de la formation Data Analyst et Développeur en Intelligence Artificielle à l'École IA Microsft by SIMPLON à Bayonne")
        st.write("Depuis 5 ans, Simplon opère à Bayonne afin de proposer des parcours allant de 6 semaines à 19 mois. Notre objectif : vous permettre de booster votre employabilité et intégrer une entreprise du territoire. Nous proposons majoritairement des formations en alternance accessibles à toutes et tous sans prérequis de diplôme, mais également des parcours dédiés à des talents souhaitant se lancer dans l'entreprenariat et ayant besoin de compétences techniques ! Vous souhaitez vous former ou vous reconvertir dans les métiers du numérique ?")
        st.link_button("Contactez SIMPLON", "https://nouvelleaquitaine.simplon.co/simplon-euskadi.html")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/simplon-simplon.png)](https://nouvelleaquitaine.simplon.co/simplon-euskadi.html)")

    with col8:
        st.subheader("LE CONTEXTE ET LE PROJET")
        st.write("Le projet de Data Visualization vise à permettre à un groupe d'étudiants de créer un dashboard interactif pour visualiser divers indicateurs. Ces indicateurs sont disponibles aujourd’hui grâce aux données que nous exploitons en interne. Nous manquons aujourd’hui d’un outil pour nous permettre d’observer l’évolution de nos données dans le temps. Ces données sont de types variables, il peut s’agir de données sur les inscriptions, de données financières, de données sur l’utilisation de la plateforme etc.")
        st.write("Le projet consiste à concevoir et développer un dashboard interactif qui offre une visualisation claire et efficace des indicateurs de données sélectionnés et communiqués aux étudiants.")
        st.link_button("Contactez AKIGORA", "https://akigora.com/")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/akigora-akigora.png)](https://akigora.com/)")

    with col9:
        st.empty()

if selected == "RH":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département RH")

        titres_onglets = ["**Nb. experts inscrits / mois**", "**Nb. experts visibles**", "**% de profil complétés**",
                          "**% d'experts par activité**", "**Nb. d'experts / ville**", "**Nb. d'experts / région**",
                          "**% d'entretiens**", "**% LinkedIn**", "**Nb. d'écoles et d'entreprises**"]
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

            plt.figure(figsize=(10, 8))
            sns.barplot(x=filtered_df['Mois_Str'], y=filtered_df['Id_Experts'],
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

            st.markdown(f"**{percentage_visible:.1f}% des utilisateurs** sont visibles sur la plateforme.")

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

            dfE['Date'] = pd.to_datetime(dfE['Date'], format='%d/%m/%Y')
            dfE['Mois'] = dfE['Date'].dt.to_period("M")
            df_experts_par_mois = dfE.groupby('Mois')['Id_Experts'].count().reset_index()

            grouped_data = dfE.groupby("Pourcentage_Profil_Complété")["Id_Experts"].nunique().reset_index()
            grouped_data.columns = ["Pourcentage", "Count_Experts"]

            min_percentage = grouped_data["Pourcentage"].min()
            max_percentage = grouped_data["Pourcentage"].max()

            selected_range = st.slider('**Sélectionner la plage de pourcentages**',
                                       min_value=min_percentage,
                                       max_value=max_percentage,
                                       value=(min_percentage, max_percentage))

            filtered_data = grouped_data[(grouped_data["Pourcentage"] >= selected_range[0]) &
                                         (grouped_data["Pourcentage"] <= selected_range[1])]

            total_experts = filtered_data["Count_Experts"].sum()
            average_percentage = filtered_data["Pourcentage"].mean()

            st.markdown(
                f"**{total_experts} experts** ont rempli leur profil à **{average_percentage:.2f}%** en moyenne dans la plage sélectionnée.")

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
                    st.markdown(f"Il y a **{experts_count} experts** dans le domaine d'activité **{domaine}**.")

            plt.figure(figsize=(14, 11))
            sns.countplot(data=filtered_df, x="Domaine_D'activité",
                          color="red", edgecolor="black", linewidth=2, width=0.5)
            plt.xlabel("Domaine d'activité", size=30)
            plt.ylabel("Nombre d'experts", size=30)
            plt.xticks(rotation=45, ha='right')
            st.pyplot(plt)

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

            fig, ax = plt.subplots(figsize=(10, 8))
            filtered_data = filtered_data.sort_values(by="Id_Experts", ascending=True)
            ax.barh(filtered_data["Ville"], filtered_data["Id_Experts"],
                    color="red", edgecolor="black", linewidth=2, height=0.5)
            ax.set_xlabel("Nombre d'experts", size=20)
            ax.set_ylabel("Ville", size=20)
            st.pyplot(fig)

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

            import streamlit as st
            import plotly.express as px
            import pandas as pd

            # Supposons que dfE est déjà chargé
            # dfE = pd.read_csv('chemin_vers_dfE.csv')

            # Calcul des pourcentages d'entretiens passés et non passés
            entretien_counts = dfE['Done'].value_counts()
            total_entretiens = len(dfE)
            percentage_passed = (entretien_counts[True] / total_entretiens) * 100
            percentage_not_passed = (entretien_counts[False] / total_entretiens) * 100

            # Affichage du pourcentage avec Markdown
            st.markdown(f"**{percentage_passed:.1f}% des utilisateurs** ont passé un entretien.")

            # Création du graphique en camembert
            fig = px.pie(
                names=['Entretien Passé', 'Entretien Non Passé'],
                values=[percentage_passed, percentage_not_passed],
                labels={'percentage_passed': 'Entretien Passé', 'percentage_not_passed': 'Entretien Non Passé'},
            )
            fig.update_traces(
                marker=dict(colors=['black', 'red'], line=dict(color='black', width=3)),
                textinfo='label+percent',
            )
            fig.update_layout(
                font=dict(size=20),
                showlegend=False,
            )

            # Affichage du graphique
            st.plotly_chart(fig)

        with onglets[7]:
            st.header("Pourcentage d'importation de profil LinkedIn")

            import_counts = dfE['Import_LinkedIn'].value_counts()
            total_users = len(dfE)
            percentage_linked_in = (import_counts[True] / total_users) * 100
            percentage_not_linked_in = (import_counts[False] / total_users) * 100

            st.markdown(f"**{percentage_linked_in:.1f}% des utilisateurs** ont effectué une importation LinkedIn.")

            fig = px.pie(
                names=['LinkedIn', 'Non LinkedIn'],
                values=[percentage_linked_in, percentage_not_linked_in],
                labels={'percentage_linked_in': 'LinkedIn', 'percentage_not_linked_in': 'Non LinkedIn'},
            )
            fig.update_traces(
                marker=dict(colors=['red', 'black'], line=dict(color='black', width=3)),
                textinfo='label+percent',
            )
            fig.update_layout(
                font=dict(size=20),
                showlegend=False,
            )

            st.plotly_chart(fig)

        with onglets[8]:
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

            fig = px.pie(
                names=labels,
                values=values,
                labels={'labels': 'Type'}
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

    with col3:
        st.empty()

if selected == "Commercial":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département Commercial")

        titres_onglets = ["**Nb. de missions**", "**Tarif journalier et tarif horaire**"]
        onglets = st.tabs(titres_onglets)

        with onglets[0]:
            st.header("Nombre de missions")

            nombre_total_missions = dfI['Id_Interventions'].nunique()
            st.markdown(f"Nombre total unique de missions : **{nombre_total_missions}**.")

            total_heures = dfI['Nombre_Heures'].sum()
            total_heures_rounded = round(total_heures)
            st.markdown(f"La somme totale des heures est : **{total_heures_rounded} heures**.")

            moyenne_heures = dfI['Nombre_Heures'].mean()
            moyenne_heures_rounded = round(moyenne_heures)
            st.markdown(f"La durée moyenne des missions est : **{moyenne_heures_rounded} heures**.")

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

            st.header("Colonne TJ minimum")
            st.markdown(f"""
                Minimum : **{min_max_moyenne_tarif_journalier_minimum[0]} €**\n 
                Maximum : **{min_max_moyenne_tarif_journalier_minimum[1]} €**\n
                Moyenne : **{min_max_moyenne_tarif_journalier_minimum[2]} €**
            """)

            st.header("Colonne TJ maximum")
            st.markdown(f"""
                Minimum : **{min_max_moyenne_tarif_journalier_maximum[0]} €**\n
                Maximum : **{min_max_moyenne_tarif_journalier_maximum[1]} €**\n
                Moyenne : **{min_max_moyenne_tarif_journalier_maximum[2]} €**
            """)

            st.header("Colonne TH minimum")
            st.markdown(f"""
                Minimum : **{min_max_moyenne_tarif_heure_minimum[0]} €**\n
                Maximum : **{min_max_moyenne_tarif_heure_minimum[1]} €**\n
                Moyenne : **{min_max_moyenne_tarif_heure_minimum[2]} €**
            """)

            st.header("Colonne TH maximum")
            st.markdown(f"""
                Minimum : **{min_max_moyenne_tarif_heure_maximum[0]} €**\n
                Maximum : **{min_max_moyenne_tarif_heure_maximum[1]} €**\n
                Moyenne : **{min_max_moyenne_tarif_heure_maximum[2]} €**
            """)

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

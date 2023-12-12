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
    menu_title="Stage AKIGORA",
    options=["Projet", "RH", "Commercial", "Marketing", "Datasets", "Remerciements"],
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

        st.write("\n")
        st.write("\n")
        st.subheader("École Microsoft IA by SIMPLON")
        st.write("Ce projet s'inscrit dans le cadre de la formation Data Analyst et Développeur en Intelligence Artificielle à l'École IA Microsft by SIMPLON à Bayonne")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/2_Logo_SIMPLON.png)](https://nouvelleaquitaine.simplon.co/simplon-euskadi.html)")

        st.write("\n")
        st.write("\n")

        st.subheader("LE CONTEXTE ET LE PROJET")
        st.write("Le projet de Data Visualization vise à permettre à un groupe d'étudiants de créer un dashboard interactif pour visualiser divers indicateurs. Ces indicateurs sont disponibles aujourd’hui grâce aux données que nous exploitons en interne. Nous manquons aujourd’hui d’un outil pour nous permettre d’observer l’évolution de nos données dans le temps. Ces données sont de types variables, il peut s’agir de données sur les inscriptions, de données financières, de données sur l’utilisation de la plateforme etc.")
        st.write("Le projet consiste à concevoir et développer un dashboard interactif qui offre une visualisation claire et efficace des indicateurs de données sélectionnés et communiqués aux étudiants.")
        st.write("\n")
        st.markdown("[![Foo](https://www.kvn-hgs.com/wp-content/uploads/2023/12/logo_akigora.png)](https://akigora.com/)")

    with col3:
        st.empty()

if selected == "RH":

    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])

    with col1:
        st.empty()

    with col2:
        st.title("Le département RH")

        titres_onglets = ["**Nb. experts inscrits / mois**", "**Nb. experts visibles**", "**% de profil complétés**",
                          "**% d'experts par activité**", "**Nb. d'experts / ville**", "**Nb. experts / région**",
                          "**% d'entretiens**", "**% LinkedIn**", "**Nb. d'écoles et d'entreprises**"]
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
                phrase = f"**{filtered_df['Id_Experts'].sum()} experts** se sont inscrits au mois de **{selected_months[0]}**."
            elif all_months_option in selected_months:
                phrase = f"**{filtered_df['Id_Experts'].sum()} experts** se sont inscrits au total."
            else:
                phrase = f"**{filtered_df['Id_Experts'].sum()} experts** se sont inscrits aux mois de **{', '.join(selected_months)}**."
            st.markdown(f"{phrase}")

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
                    f"**{total_experts} experts** ont rempli leur profil à **{average_percentage_all_data:.2f}%** en moyenne.")
            else:
                st.markdown(f"**{total_experts} experts** ont rempli leur profil à **{selected_percentages_str}%**")

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
                        f"Il y a **{experts_count} experts** dans les autres villes, ce qui représente **{percentage:.2f}%** des experts.")
                else:
                    experts_count = grouped_data[grouped_data["Location"] == ville]['Id_Experts'].values[0]
                    total_experts = grouped_data["Id_Experts"].sum()
                    percentage = (experts_count / total_experts) * 100
                    st.markdown(
                        f"Il y a **{experts_count} experts à {ville}**, ce qui représente **{percentage:.2f}%** des experts.")

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
            reste_regions = pd.DataFrame(
                {"Région": ["Autres"], "Nombre_Villes": [experts_par_region.iloc[10:, 1].sum()]})
            grouped_data_regions = pd.concat([top_10_regions, reste_regions])

            regions_list = grouped_data_regions["Région"].tolist()
            regions_list.insert(0, "Toutes les régions")
            selected_regions = st.multiselect("**Choisissez les régions**", regions_list)

            if "Toutes les régions" in selected_regions:
                selected_regions = grouped_data_regions["Région"].tolist()  # Sélectionner toutes les régions par défaut

            for region in selected_regions:
                if region == "Autres":
                    experts_count = \
                        grouped_data_regions[grouped_data_regions["Région"] == "Autres"]['Nombre_Villes'].values[0]
                    total_villes = grouped_data_regions["Nombre_Villes"].sum()
                    percentage = (experts_count / total_villes) * 100
                    st.markdown(
                        f"Il y a **{experts_count} villes** dans les autres régions, ce qui représente **{percentage:.2f}%** des villes.")
                else:
                    experts_count = \
                        grouped_data_regions[grouped_data_regions["Région"] == region]['Nombre_Villes'].values[0]
                    total_villes = grouped_data_regions["Nombre_Villes"].sum()
                    percentage = (experts_count / total_villes) * 100
                    st.markdown(
                        f"Il y a **{experts_count} villes** dans la région **{region}**, ce qui représente **{percentage:.2f}%** des villes.")

            fig, ax = plt.subplots(figsize=(10, 8))
            grouped_data_regions = grouped_data_regions.sort_values(by="Nombre_Villes", ascending=True)
            ax.barh(grouped_data_regions["Région"], grouped_data_regions["Nombre_Villes"],
                    color="red", edgecolor="black", linewidth=2, height=0.5)
            ax.set_xlabel("Nombre de Villes", size=25)
            ax.set_ylabel("Région", size=25)
            st.pyplot(fig)

        with onglets[6]:
            st.header("Pourcentage d'entretiens passés")

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
                min_val = dfE[colonne].min()
                max_val = dfE[colonne].max()
                moyenne = dfE[colonne].mean()  # Calculer la moyenne de toutes les valeurs de la colonne
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

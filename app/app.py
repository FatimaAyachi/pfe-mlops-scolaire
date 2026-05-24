# app.py

import streamlit as st
import requests

from styles import load_css
from utils import (
    create_student_cards,
    generate_recommendations,
    create_sidebar,
    check_missing_fields,
    convert_form_data,
    EDUCATION_LEVELS,
    STUDY_LEVELS,
    TRAVEL_LEVELS,
    LEVEL_5,
    HEALTH_MAP,
    FAMREL_MAP
)

# =========================================================
# CONFIGURATION PAGE
# =========================================================

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# CHARGEMENT DES STYLES
# =========================================================

load_css()

# =========================================================
# API URL
# =========================================================

api_url = "https://tima456tz-student-api.hf.space/predict"

# =========================================================
# SESSION STATE
# =========================================================

if "show_form" not in st.session_state:
    st.session_state.show_form = False

# =========================================================
# CARD INTRODUCTION
# =========================================================

st.markdown("""
<div class="welcome-card">
<h2>🎓 Student Performance Prediction</h2>
<p>
        Cette plateforme utilise l'intelligence artificielle
        pour analyser les facteurs de réussite scolaire
        des étudiants.
</p>
<p>Remplissez le formulaire pour obtenir une prédiction et des recommandations personnalisées.</p>

</div>
""", unsafe_allow_html=True)

if st.button(" Commencer l'analyse"):
    st.session_state.show_form = True

# =========================================================
# AFFICHAGE FORMULAIRE
# =========================================================

if st.session_state.show_form:

    # =========================================================
    # HEADER
    # =========================================================

    st.markdown(
        '<div class="main-title">🎓 Academic Performance Predictor</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    # =========================================================
    # SECTION INFORMATIONS GENERALES
    # =========================================================

    st.markdown(
        '<div class="section-title">📌 Informations Generales</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "📅 Age",
            min_value=15,
            max_value=22,
            value=None,
            placeholder="Entrer l'âge"
        )

    with col2:
        sex = st.selectbox(
            "👤 Genre",
            options=["", "Femme", "Homme"]
        )

    # =========================================================
    # SECTION EDUCATION
    # =========================================================

    st.markdown(
        '<div class="section-title">📚 Education & Etudes</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        Medu = st.selectbox(
            "👩‍🎓 Education de la mere",
            options=list(EDUCATION_LEVELS.keys())
        )

        studytime = st.selectbox(
            "⏱️ Temps d'etude",
            options=list(STUDY_LEVELS.keys())
        )

        absences = st.number_input(
            "🏃 Nombre d'absences",
            min_value=0,
            max_value=100,
            value=None
        )

    with col2:

        Fedu = st.selectbox(
            "👨‍🎓 Education du pere",
            options=list(EDUCATION_LEVELS.keys())
        )

        failures = st.number_input(
            "❌ Nombre d'echecs",
            min_value=0,
            max_value=10,
            value=None
        )

        higher = st.selectbox(
            "🎯 Etudes superieures",
            options=["", "Oui", "Non"]
        )

    # =========================================================
    # SECTION VIE PERSONNELLE
    # =========================================================

    st.markdown(
        '<div class="section-title">🏠 Vie Personnelle</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        traveltime = st.selectbox(
            "🚗 Temps trajet",
            options=list(TRAVEL_LEVELS.keys())
        )

        Walc = st.selectbox(
            "🍷 Consommation alcool weekend",
            options=list(LEVEL_5.keys())
        )

        freetime = st.selectbox(
            "🎮 Temps libre",
            options=list(LEVEL_5.keys())
        )

        internet = st.selectbox(
            "🌐 Internet maison",
            options=["", "Oui", "Non"]
        )

    with col2:

        goout = st.selectbox(
            "🎉 Sorties avec amis",
            options=list(LEVEL_5.keys())
        )

        health = st.selectbox(
            "💪 Etat de sante",
            options=[
                "",
                "Tres mauvais",
                "Mauvais",
                "Moyen",
                "Bon",
                "Excellent"
            ]
        )

        famrel = st.selectbox(
            "❤️ Relations familiales",
            options=[
                "",
                "Tres mauvaise",
                "Mauvaise",
                "Moyenne",
                "Bonne",
                "Excellente"
            ]
        )

    # =========================================================
    # BOUTON
    # =========================================================

    predict_btn = st.button(" Envoyer Prediction")

    st.markdown("</div>", unsafe_allow_html=True)

    # =========================================================
    # TRAITEMENT PREDICTION
    # =========================================================

    if predict_btn:

        fields = {
            "Age": age,
            "Genre": sex,
            "Education Mere": Medu,
            "Education Pere": Fedu,
            "Temps Etude": studytime,
            "Echecs": failures,
            "Absences": absences,
            "Etudes Superieures": higher,
            "Temps Trajet": traveltime,
            "Sorties": goout,
            "Alcool": Walc,
            "Sante": health,
            "Temps Libre": freetime,
            "Relations Familiales": famrel,
            "Internet": internet
        }

        missing_fields = check_missing_fields(fields)

        if len(missing_fields) > 0:

            st.error("⚠️ Veuillez remplir tous les champs.")

            st.warning(
                "Champs manquants :\n\n- " +
                "\n- ".join(missing_fields)
            )

        else:

            # =========================================================
            # CONVERSION DONNEES
            # =========================================================

            data = convert_form_data(
                age,
                sex,
                Medu,
                Fedu,
                studytime,
                failures,
                absences,
                higher,
                traveltime,
                goout,
                Walc,
                health,
                freetime,
                famrel,
                internet
            )

            with st.spinner("Analyse des donnees..."):

                try:

                    response = requests.post(api_url, json=data)

                    if response.status_code == 200:

                        result = response.json()["The result is "]

                        st.balloons()

                        # =========================================================
                        # RESULTATS
                        # =========================================================

                        st.markdown("""
                        <div class="big-result-card">

                        <div class="result-text">
                                📈 Rapport d'Evaluation Academique
                        </div>

                        <div class="result-sub">
                                Prediction automatique basee sur les habitudes
                                et performances scolaires

                        <br><br>

                        ✅ Verifiez bien que les informations saisies
                                dans la section
                        <strong>📂 Profil Académique</strong>
                                sont correctes.

                        <br><br>

                        💡 Consultez egalement la sidebar pour voir
                                les recommandations et conseils personnalises.
                        </div>
                        """, unsafe_allow_html=True)

                        if result == 1:

                            st.markdown(
                                '<div class="result-success">✅ REUSSITE SCOLAIRE</div>',
                                unsafe_allow_html=True
                            )

                        else:

                            st.markdown(
                                '<div class="result-fail">❌ RISQUE D\'ECHEC SCOLAIRE</div>',
                                unsafe_allow_html=True
                            )

                        # =========================================================
                        # PROFIL ACADEMIQUE
                        # =========================================================

                        st.markdown(
                            '<div class="divider"></div>',
                            unsafe_allow_html=True
                        )

                        st.markdown("## 📂 Profil Académique")

                        create_student_cards(
                            age,
                            sex,
                            studytime,
                            absences,
                            failures,
                            Medu,
                            Fedu,
                            higher,
                            goout,
                            Walc,
                            health,
                            freetime,
                            famrel,
                            traveltime,
                            internet
                        )

                        st.markdown("</div>", unsafe_allow_html=True)

                        # =========================================================
                        # RECOMMANDATIONS
                        # =========================================================

                        weak_points = []

                        walc_value = LEVEL_5[Walc]
                        goout_value = LEVEL_5[goout]
                        freetime_value = LEVEL_5[freetime]
                        health_value = HEALTH_MAP[health]
                        famrel_value = FAMREL_MAP[famrel]
                        study_value = STUDY_LEVELS[studytime]
                        travel_value = TRAVEL_LEVELS[traveltime]

                        if walc_value >= 4:
                            weak_points.append(
                                "consommation d'alcool élevée"
                            )

                        if absences > 20:
                            weak_points.append(
                                "absences fréquentes"
                            )

                        if failures >= 3:
                            weak_points.append(
                                "antécédents d'échecs"
                            )

                        if study_value <= 2:
                            weak_points.append(
                                "temps d'étude insuffisant"
                            )

                        if goout_value >= 4:
                            weak_points.append(
                                "sorties trop fréquentes"
                            )

                        if health_value <= 2:
                            weak_points.append(
                                "santé fragile"
                            )

                        if famrel_value <= 2:
                            weak_points.append(
                                "relations familiales difficiles"
                            )

                        recommendations = generate_recommendations(
                            walc_value,
                            absences,
                            failures,
                            study_value,
                            goout_value,
                            freetime_value,
                            health_value,
                            famrel_value,
                            higher,
                            internet,
                            travel_value,
                            result
                        )

                        create_sidebar(
                            recommendations,
                            weak_points
                        )

                    else:

                        st.error(
                            f"Erreur API : {response.status_code}"
                        )

                except Exception as e:

                    st.error(
                        f"Impossible de connecter l'API : {e}"
                    )
import streamlit as st
import requests

from styles import load_css
from utils import (
    create_student_cards,
    generate_recommendations,
    create_sidebar,
    check_missing_fields,
    convert_form_data,
    edUcaTiON_LeVeLS,
    STUdY_LeVeLS,
    TRaVeL_LeVeLS,
    LeVeL_5,
    HeaLTH_MaP,
    faMReL_MaP
)

st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

load_css()

api_url = "https://tima456tz-student-api.hf.space/predict"

if "show_form" not in st.session_state:
    st.session_state.show_form = False

st.markdown("""
<div class="welcome-card">
<h2>🎓 Student Performance Prediction </h2>
<p>
        cette plateforme utilise l'intelligence artificielle  pour analyser les facteurs de réussite scolaires des étudiants 

</p>
<p> Remplissez le formulaire  pour obtenir une prédiction et des recommandations personnalisées 
</p>

</div>
""", unsafe_allow_html=True)

if st.button(" commencer l'analyse"):
    st.session_state.show_form = True

if st.session_state.show_form:

    st.markdown(
        '<div class="main-title">🎓 academic Performance Predictor</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">📌 informations Generales</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(
            "📅 age",
            min_value=15,
            max_value=22,
            value=None,
            placeholder="entre l'age"
        )

    with col2:
        sex = st.selectbox(
            "👤 Genre",
            options=["", "femme", "Homme"]
        )
        
    st.markdown(
        '<div class="section-title">📚 education & etudes</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        Medu = st.selectbox(
            "👩‍🎓 Éducation de la mère",
            options=list(edUcaTiON_LeVeLS.keys())
        )

        studytime = st.selectbox(
            "⏱️ emps d'études",
            options=list(STUdY_LeVeLS.keys())
        )

        absences = st.number_input(
            "🏃 Nombre d'absences",
            min_value=0,
            max_value=100,
            value=None
        )

    with col2:

        fedu = st.selectbox(
            "👨‍🎓 ducation du  père",
            options=list(edUcaTiON_LeVeLS.keys())
        )

        failures = st.number_input(
            "❌ Nombre d'échec ",
            min_value=0,
            max_value=10,
            value=None
        )

        higher = st.selectbox(
            "🎯 Études supérieures",
            options=["", "Oui", "Non"]
        )

    st.markdown(
        '<div class="section-title">🏠Vie personnelle</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        traveltime = st.selectbox(
            "🚗 emps trajet",
            options=list(TRaVeL_LeVeLS.keys())
        )

        Walc = st.selectbox(
            "🍷 consommation alcool weekend",
            options=list(LeVeL_5.keys())
        )

        freetime = st.selectbox(
            "🎮 Temps libre",
            options=list(LeVeL_5.keys())
        )

        internet = st.selectbox(
            "🌐 internet maison",
            options=["", "Oui", "Non"]
        )

    with col2:

        goout = st.selectbox(
            "🎉 Sorties avec amis",
            options=list(LeVeL_5.keys())
        )

        health = st.selectbox(
            "💪 etat de sante",
            options=[
                "",
                "Tres mauvais",
                "Mauvais",
                "Moyen",
                "bon",
                "excellent"
            ]
        )

        famrel = st.selectbox(
            "❤️ Relation familiale",
            options=[
                "",
                "Tres mauvaise",
                "Mauvaise",
                "Moyenne",
                "bonne",
                "excellente"
            ]
        )

    predict_btn = st.button(" envoyer Prediction")

    st.markdown("</div>", unsafe_allow_html=True)

    if predict_btn:

        fields = {
            "age": age,
            "Genre": sex,
            "education Mere": Medu,
            "education Pere": fedu,
            "Temps etude": studytime,
            "echecs": failures,
            "absences": absences,
            "etudes Superieures": higher,
            "Temps Trajet": traveltime,
            "Sorties": goout,
            "alcool": Walc,
            "Sante": health,
            "Temps Libre": freetime,
            "Relations familiales": famrel,
            "internet": internet
        }

        missing_fields = check_missing_fields(fields)
        if len(missing_fields) > 0:

            st.error("⚠️ Veuillez remplire tous les champs")

            st.warning(
                "champs manquants :\n\n- " +
                "\n- ".join(missing_fields)
            )

        else:
            data = convert_form_data(
                age,
                sex,
                Medu,
                fedu,
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

            with st.spinner("analyse des donnees....."):

                try:

                    response = requests.post(api_url, json=data)

                    if response.status_code == 200:

                        result = response.json()["The result is "]

                        st.balloons()
                        st.markdown("""
                        <div class="big-result-card">

                        <div class="result-text">
                                📈 Rapport d'evaluation academique
                        </div>

                        <div class="result-sub">
                                Prediction automatique basee sur les habitudes
                                et performances scolaires

                        <br><br>

                        ✅ Verifiez bien que les informations saisies
                                dans la section
                        <strong>📂 Profil académique</strong>
                                sont correctes.

                        <br><br>

                        💡 consultez egalement la sidebar pour voir
                                les recommandations et conseils personnalises.
                        </div>
                        """, unsafe_allow_html=True)

                        if result == 1:

                            st.markdown(
                                '<div class="result-success">✅ ReUSSiTe ScolaiRe</div>',
                                unsafe_allow_html=True
                            )

                        else:

                            st.markdown(
                                '<div class="result-fail">❌ RiSQUe d\'ecHec ScolaiRe</div>',
                                unsafe_allow_html=True
                            )

                        st.markdown(
                            '<div class="divider"></div>',
                            unsafe_allow_html=True
                        )

                        st.markdown("## 📂 Profil académique")

                        create_student_cards(
                            age,
                            sex,
                            studytime,
                            absences,
                            failures,
                            Medu,
                            fedu,
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

                        weak_points = []

                        walc_value = LeVeL_5[Walc]
                        goout_value = LeVeL_5[goout]
                        freetime_value = LeVeL_5[freetime]
                        health_value = HeaLTH_MaP[health]
                        famrel_value = faMReL_MaP[famrel]
                        study_value = STUdY_LeVeLS[studytime]
                        travel_value = TRaVeL_LeVeLS[traveltime]

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
                            f"erreur aPi : {response.status_code}"
                        )

                except Exception as e:

                    st.error(
                        f"impossible de connecter l'aPi : {e}"
                    )
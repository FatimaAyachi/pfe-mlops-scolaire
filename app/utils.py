# utils.py
import streamlit as st

# Constantes globales
EDUCATION_LEVELS = {"": None, "Aucun": 0, "Primaire": 1, "College": 2, "Lycee": 3, "Universite": 4}
STUDY_LEVELS = {"": None, "< 2 heures": 1, "2 a 5 heures": 2, "5 a 10 heures": 3, "> 10 heures": 4}
TRAVEL_LEVELS = {"": None, "< 15 min": 1, "15 a 30 min": 2, "30 min a 1h": 3, "> 1h": 4}
LEVEL_5 = {"": None, "Tres faible": 1, "Faible": 2, "Moyenne": 3, "Elevee": 4, "Tres elevee": 5}
HEALTH_MAP = {"Tres mauvais": 1, "Mauvais": 2, "Moyen": 3, "Bon": 4, "Excellent": 5}
FAMREL_MAP = {"Tres mauvaise": 1, "Mauvaise": 2, "Moyenne": 3, "Bonne": 4, "Excellente": 5}

def create_student_cards(age, sex, studytime, absences, failures, Medu, Fedu, higher, goout, Walc, health, freetime, famrel, traveltime, internet):
    """Crée les cartes d'informations étudiant"""
    cartes_html = f"""
    <div class="student-info-grid">
        <div class="student-card"><div class="student-card-icon">👤</div><div class="student-card-title">AGE</div><div class="student-card-value">{age} ans</div></div>
        <div class="student-card"><div class="student-card-icon">🚻</div><div class="student-card-title">GENRE</div><div class="student-card-value">{sex}</div></div>
        <div class="student-card"><div class="student-card-icon">📚</div><div class="student-card-title">TEMPS D'ETUDE</div><div class="student-card-value">{studytime}</div></div>
        <div class="student-card"><div class="student-card-icon">❌</div><div class="student-card-title">ABSENCES</div><div class="student-card-value">{absences}</div></div>
        <div class="student-card"><div class="student-card-icon">⚠️</div><div class="student-card-title">ECHECS</div><div class="student-card-value">{failures}</div></div>
        <div class="student-card"><div class="student-card-icon">👩‍🎓</div><div class="student-card-title">EDUCATION MERE</div><div class="student-card-value">{Medu}</div></div>
        <div class="student-card"><div class="student-card-icon">👨‍🎓</div><div class="student-card-title">EDUCATION PERE</div><div class="student-card-value">{Fedu}</div></div>
        <div class="student-card"><div class="student-card-icon">🎯</div><div class="student-card-title">ETUDES SUPERIEURES</div><div class="student-card-value">{higher}</div></div>
        <div class="student-card"><div class="student-card-icon">🎉</div><div class="student-card-title">SORTIES</div><div class="student-card-value">{goout}</div></div>
        <div class="student-card"><div class="student-card-icon">🍷</div><div class="student-card-title">ALCOOL WEEKEND</div><div class="student-card-value">{Walc}</div></div>
        <div class="student-card"><div class="student-card-icon">💪</div><div class="student-card-title">SANTE</div><div class="student-card-value">{health}</div></div>
        <div class="student-card"><div class="student-card-icon">🎮</div><div class="student-card-title">TEMPS LIBRE</div><div class="student-card-value">{freetime}</div></div>
        <div class="student-card"><div class="student-card-icon">❤️</div><div class="student-card-title">RELATIONS FAMILIALES</div><div class="student-card-value">{famrel}</div></div>
        <div class="student-card"><div class="student-card-icon">🚗</div><div class="student-card-title">TEMPS TRAJET</div><div class="student-card-value">{traveltime}</div></div>
        <div class="student-card"><div class="student-card-icon">🌐</div><div class="student-card-title">INTERNET</div><div class="student-card-value">{internet}</div></div>
    </div>
    """
    st.markdown(cartes_html, unsafe_allow_html=True)

def generate_recommendations(Walc_value, absences, failures, study_value, goout_value, freetime_value, health_value, famrel_value, higher, internet, travel_value, success_score):
    """Génère des recommandations personnalisées"""
    recommendations = []
    
    if Walc_value >= 4:
        recommendations.append({"title": "🍷 Réduire l'alcool", "advice": "L'alcool affecte votre concentration et vos performances.", "action": "Objectif : Max 2 consommations/semaine", "priority": "high"})
    elif Walc_value == 3:
        recommendations.append({"title": "🍷 Modérer l'alcool", "advice": "Évitez l'alcool avant les examens.", "action": "Conseil : Restez vigilant", "priority": "medium"})
    
    if absences > 20:
        recommendations.append({"title": "🏃 Réduire les absences", "advice": "Votre présence en cours est essentielle.", "action": "Objectif : Réduire de 50%", "priority": "high"})
    elif absences > 10:
        recommendations.append({"title": "🏃 Améliorer l'assiduité", "advice": "Identifiez les raisons de vos absences.", "action": "Parlez à un conseiller", "priority": "medium"})
    
    if failures >= 3:
        recommendations.append({"title": "📚 Soutien académique", "advice": "Vous avez besoin d'aide pour réussir.", "action": "Demandez du tutorat", "priority": "high"})
    elif failures >= 1:
        recommendations.append({"title": "📚 Prévention", "advice": "Analysez vos échecs passés.", "action": "Identifiez vos difficultés", "priority": "medium"})
    
    if study_value <= 2:
        recommendations.append({"title": "⏱️ Augmenter l'étude", "advice": "Plus d'étude = meilleures notes.", "action": "Visez 10-15h/semaine", "priority": "high"})
    
    if goout_value >= 4:
        recommendations.append({"title": "🎉 Équilibrer vie sociale", "advice": "Trop de sorties nuit aux études.", "action": "Limitez aux week-ends", "priority": "medium"})
    
    if health_value <= 2:
        recommendations.append({"title": "💪 Santé d'abord", "advice": "Votre santé affecte vos études.", "action": "Consultez un médecin", "priority": "high"})
    
    if famrel_value <= 2:
        recommendations.append({"title": "❤️ Relations familiales", "advice": "Un bon environnement familial aide à réussir.", "action": "Parlez-en à un conseiller", "priority": "medium"})
    
    if internet == "Non":
        recommendations.append({"title": "🌐 Accès internet", "advice": "Internet est essentiel pour les études.", "action": "Utilisez la bibliothèque", "priority": "medium"})
    
    if travel_value >= 3:
        recommendations.append({"title": "🚗 Optimiser le trajet", "advice": "Utilisez votre temps de transport.", "action": "Écoutez des podcasts éducatifs", "priority": "low"})
    
    if success_score < 50:
        recommendations.append({"title": "⚠️ Risque élevé", "advice": "Agissez rapidement pour améliorer votre situation.", "action": "Consultez un conseiller pédagogique", "priority": "critical"})
    
    return recommendations

def create_sidebar(recommendations, weak_points):
    """Crée le sidebar avec les conseils personnalisés"""
    with st.sidebar:
        st.markdown('<div class="sidebar-title">💡 Conseils Personnalisés</div>', unsafe_allow_html=True)
        
        if weak_points:
            st.markdown("### 🔍 Points à améliorer")
            for point in weak_points[:5]:
                st.markdown(f"- ⚠️ {point}")
            st.markdown("---")
        
        if recommendations:
            st.markdown("### 📝 Recommandations")
            priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
            recommendations.sort(key=lambda x: priority_order.get(x.get("priority", "low"), 4))
            
            for rec in recommendations[:6]:
                badge_class = "warning-badge" if rec.get("priority") in ["high", "critical"] else "info-badge"
                badge_text = "⚠️ URGENT" if rec.get("priority") == "critical" else "🔴 PRIORITAIRE" if rec.get("priority") == "high" else "ℹ️ CONSEIL"
                
                st.markdown(f"""
                <div class="advice-card">
                    <div class="{badge_class}">{badge_text}</div>
                    <div class="advice-title">{rec['title']}</div>
                    <div class="advice-text">{rec['advice']}</div>
                    <div class="advice-text" style="color: #fbbf24; margin-top: 10px;"><strong>➜ {rec['action']}</strong></div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("### ✨ Conseils Généraux")
            st.info("📚 **Astuce 1**: Établissez un planning d'étude régulier")
            st.info("💪 **Astuce 2**: Prenez soin de votre santé (sommeil, alimentation)")
            st.info("🎯 **Astuce 3**: Fixez-vous des objectifs réalisables")
            st.info("🤝 **Astuce 4**: Participez aux groupes d'étude")
            st.info("📱 **Astuce 5**: Utilisez des applications de gestion du temps")
        
        st.markdown("---")
        st.markdown("### 📞 Ressources d'aide")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎓 Aide scolaire", key="help_academic", use_container_width=True):
                st.success("📞 Contactez le service de tutorat: 01 23 45 67 89")
        with col2:
            if st.button("💬 Soutien psy", key="help_mental", use_container_width=True):
                st.success("💚 Ligne d'écoute étudiante: 0 800 123 456")
        
        if st.button("📅 Plan d'action", key="action_plan", use_container_width=True):
            st.balloons()
            st.success("✅ Plan généré! Objectifs hebdomadaires:")
            st.markdown("""
            - 📚 Semaine 1: +2h d'étude par jour
            - 🎯 Semaine 2: Réduire les sorties
            - 💪 Semaine 3: Adopter une routine saine
            - 📊 Semaine 4: Évaluer les progrès
            """)

def check_missing_fields(fields):
    """Vérifie les champs manquants"""
    missing_fields = []
    for key, value in fields.items():
        if value == "" or value is None:
            missing_fields.append(key)
    return missing_fields

def convert_form_data(age, sex, Medu, Fedu, studytime, failures, absences, higher, traveltime, goout, Walc, health, freetime, famrel, internet):
    """Convertit les données du formulaire pour l'API"""
    sex_value = 0 if sex == "Femme" else 1
    higher_value = 1 if higher == "Oui" else 0
    internet_value = 1 if internet == "Oui" else 0
    
    return {
        "age": age, "sex": sex_value, "Medu": EDUCATION_LEVELS[Medu], "Fedu": EDUCATION_LEVELS[Fedu],
        "studytime": STUDY_LEVELS[studytime], "failures": failures, "absences": absences,
        "goout": LEVEL_5[goout], "Walc": LEVEL_5[Walc], "health": HEALTH_MAP[health],
        "higher": higher_value, "internet": internet_value, "traveltime": TRAVEL_LEVELS[traveltime],
        "freetime": LEVEL_5[freetime], "famrel": FAMREL_MAP[famrel]
    }
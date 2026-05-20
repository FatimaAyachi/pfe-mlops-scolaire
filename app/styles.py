# styles.py
import streamlit as st

def load_css():
    """Charge les styles CSS personnalisés"""
    st.markdown("""
    <style>
    html, body, [class*="css"] { font-family: 'Segoe UI', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0b1220 0%, #111827 50%, #0f172a 100%); }
    .main-title { text-align: center; font-size: 42px; font-weight: bold; color: white; margin-bottom: 10px; }
    .subtitle { text-align: center; color: #f0f0f0; margin-bottom: 30px; }
    .form-container { background: rgba(255, 255, 255, 0.97); padding: 30px; border-radius: 20px; box-shadow: 0px 5px 25px rgba(0,0,0,0.15); }
    .section-title { color: #667eea; font-size: 24px; font-weight: bold; margin-top: 25px; margin-bottom: 15px; border-bottom: 3px solid #667eea; padding-bottom: 8px; }
    .stTextInput label, .stNumberInput label, .stSelectbox label { font-size: 16px !important; font-weight: 600 !important; color: #e2e8f0 !important; }
    .stButton>button { width: 100%; background: linear-gradient(to right, #667eea, #764ba2); color: white; border: none; border-radius: 12px; padding: 14px; font-size: 18px; font-weight: bold; transition: transform 0.2s; }
    .stButton>button:hover { transform: scale(1.02); }
    .result-title { text-align: center; font-size: 38px; font-weight: bold; margin-bottom: 10px; }
    .score-card { background: linear-gradient(135deg, #1e293b, #0f172a); border-radius: 20px; padding: 25px; text-align: center; border: 1px solid rgba(255,255,255,0.1); transition: transform 0.3s; }
    .score-card:hover { transform: translateY(-5px); }
    .score-card-icon { font-size: 48px; margin-bottom: 15px; }
    .score-card-title { font-size: 16px; color: #a0aec0; margin-bottom: 10px; text-transform: uppercase; }
    .score-card-value { font-size: 48px; font-weight: bold; color: white; }
    .student-info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px; margin-top: 20px; }
    .student-card { background: rgba(255,255,255,0.08); border-radius: 15px; padding: 15px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.2); transition: transform 0.3s; }
    .student-card:hover { transform: translateY(-5px); background: rgba(255,255,255,0.15); }
    .student-card-title { font-size: 14px; color: #a0aec0; margin-bottom: 5px; text-transform: uppercase; }
    .student-card-value { font-size: 20px; font-weight: bold; color: white; }
    .student-card-icon { font-size: 24px; margin-bottom: 10px; }
    .divider { height: 2px; background: linear-gradient(to right, #667eea, #764ba2); margin: 20px 0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%); }
    .sidebar-title { font-size: 24px; font-weight: bold; color: white; text-align: center; margin-bottom: 20px; padding-bottom: 10px; border-bottom: 2px solid #667eea; }
    .advice-card { background: rgba(255,255,255,0.1); border-radius: 15px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #f59e0b; }
    .advice-title { font-size: 18px; font-weight: bold; color: #fbbf24; margin-bottom: 10px; }
    .advice-text { font-size: 14px; color: #e2e8f0; line-height: 1.6; }
    .warning-badge { background: #ef4444; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; display: inline-block; margin-bottom: 10px; }
    .info-badge { background: #3b82f6; color: white; padding: 5px 10px; border-radius: 20px; font-size: 12px; display: inline-block; margin-bottom: 10px; }
    .result-success {background: linear-gradient(135deg, #16a34a, #22c55e);padding: 25px;border-radius: 20px;text-align: center;margin-top: 25px;box-shadow: 0px 5px 20px rgba(34,197,94,0.3);}
    .result-fail {background: linear-gradient(135deg, #dc2626, #ef4444);padding: 25px;border-radius: 20px;text-align: center;margin-top: 25px;box-shadow: 0px 5px 20px rgba(239,68,68,0.3);}
    .result-description {color: #f8fafc;font-size: 18px;margin-top: 10px;}
    .big-result-card {
    background: linear-gradient(135deg, #111827, #1e293b);border-radius: 25px;padding: 40px;margin-top: 30px;color: white;box-shadow: 0px 10px 35px rgba(0,0,0,0.35);border: 1px solid rgba(255,255,255,0.08);text-align: center;}
    .result-text {font-size: 38px;font-weight: 700;color: #f8fafc;margin-bottom: 10px;}
    .result-sub {font-size: 18px;color: #cbd5e1;margin-bottom: 25px;letter-spacing: 0.5px;}
    .welcome-card{background: linear-gradient(135deg, #111827 0%, #334155 100%);padding: 55px;border-radius: 28px;margin: 50px auto;text-align: center;max-width: 950px;border: 1px solid rgba(99,102,241,0.15);box-shadow: 0px 10px 35px rgba(0,0,0,0.18);backdrop-filter: blur(12px);}
    .welcome-card h2{color: #e0e7ff;font-size: 46px;font-weight: 800;margin-bottom: 28px;letter-spacing: 0.5px;}
    .welcome-card p{color: #cbd5e1;font-size: 22px;font-weight: 500;line-height: 2;margin-bottom: 20px;padding: 0 20px;}
    </style>
    """, unsafe_allow_html=True)
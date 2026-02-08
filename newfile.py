import streamlit as st
import pandas as pd
import plotly.express as px

# --- Core Psychology Logic ---
def analyze_risk(fear, fantasy, need, reinforcement):
    weights = {'fear': 1.5, 'fantasy': 1.0, 'need': 1.2, 'reinforcement': 2.0}
    total_score = (fear * weights['fear'] + fantasy * weights['fantasy'] + 
                   need * weights['need'] + reinforcement * weights['reinforcement'])
    normalized_score = min(1.0, total_score / 30) # Scale of 0 to 1
    return normalized_score

# --- UI Layout ---
st.set_page_config(page_title="Mind-State Analyzer", layout="wide")

st.title("🛡️ Mind-State Security Dashboard")
st.markdown("### Analyzing Psychological Attachment Patterns")

with st.sidebar:
    st.header("🔍 Input Parameters")
    st.info("ပြုမူမှုပြင်းအားများကို ၀ မှ ၁၀ အတွင်း သတ်မှတ်ပေးပါ။")
    fear = st.slider("Fear Induction (ကြောက်ရွံ့မှု)", 0, 10, 5)
    fantasy = st.slider("Fantasy Creation (စိတ်ကူးယဉ်မှု)", 0, 10, 5)
    need = st.slider("Need Exploitation (လိုအပ်ချက်အသုံးချခြင်း)", 0, 10, 5)
    reinforce = st.slider("Intermittent Reinforcement (အခါအားလျော်စွာ ချစ်ပြခြင်း)", 0, 10, 5)

# --- Calculation ---
risk_score = analyze_risk(fear, fantasy, need, reinforce)

# --- Visuals ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Pattern Analysis")
    df = pd.DataFrame(dict(
        r=[fear, fantasy, need, reinforce],
        theta=['Fear','Fantasy','Need','Reinforcement']))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    fig.update_traces(fill='toself', line_color='#FF4B4B')
    st.plotly_chart(fig)

with col2:
    st.subheader("⚠️ Risk Assessment")
    st.metric(label="Total Risk Score", value=f"{risk_score:.2%}")
    
    if risk_score > 0.75:
        st.error("DANGER: TRAUMA BOND DETECTED")
        st.markdown("**အကြံပြုချက်:** ပတ်ဝန်းကျင်နဲ့ အမြန်ဆုံး အဆက်အသွယ်လုပ်ပြီး အကူအညီတောင်းပါ။")
    elif risk_score > 0.45:
        st.warning("WARNING: TOXIC PATTERN EMERGING")
    else:
        st.success("SAFE: HEALTHY BOUNDARIES")

st.divider()
st.caption("Developed by AI Mentor & Syntax Snake for Psychological Awareness.")

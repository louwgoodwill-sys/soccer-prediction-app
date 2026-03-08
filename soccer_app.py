import streamlit as st
import pandas as pd
import pickle
import json
import os

st.set_page_config(page_title="Soccer Predictor")
st.title("Soccer Match Predictor")

# Load files
model_path = "model/soccer_model_final.pkl"
encoder_path = "model/team_encoder_final.pkl"
stats_path = "model/team_stats_dict.json"

if not os.path.exists(model_path):
    st.error("Model file not found!")
    st.stop()

with open(model_path, "rb") as f:
    model = pickle.load(f)
with open(encoder_path, "rb") as f:
    encoder = pickle.load(f)
with open(stats_path, "r") as f:
    team_stats = json.load(f)

teams = sorted(team_stats.keys())

home = st.selectbox("Home Team", teams)
away = st.selectbox("Away Team", teams)

if st.button("Predict"):
    if home == away:
        st.error("Select different teams")
    else:
        home_enc = encoder.transform([home])[0]
        away_enc = encoder.transform([away])[0]
        
        home_s = team_stats[home]
        away_s = team_stats[away]
        
        data = pd.DataFrame({
            "home_team_encoded": [home_enc],
            "away_team_encoded": [away_enc],
            "home_avg_scored": [home_s["scored"]],
            "home_avg_conceded": [home_s["conceded"]],
            "away_avg_scored": [away_s["scored"]],
            "away_avg_conceded": [away_s["conceded"]]
        })
        
        probs = model.predict_proba(data)[0]
        
        st.write(f"**{home} Win:** {probs[2]*100:.1f}%")
        st.write(f"**Draw:** {probs[0]*100:.1f}%")
        st.write(f"**{away} Win:** {probs[1]*100:.1f}%")

# soccer-prediction-app
ML model predicting football match outcomes
# ⚽ Soccer Match Predictor

A machine learning web app that predicts international football match outcomes with interactive win/draw probabilities.

## 🚀 Live Demo

**[Try the app here!](https://your-app-name.streamlit.app)** *(You'll add this URL after deploying on Streamlit)*

![App Scr<img width="1920" height="1080" alt="Screenshot 2026-03-08 164124" src="https://github.com/user-attachments/assets/6eb49f32-356d-4817-aea3-68713e7f1993" />
eenshot](ima<img width="1920" height="1080" alt="Screenshot 2026-03-08 164049" src="https://github.com/user-attachments/assets/b2977bd7-1f5d-499f-a513-07382fe7149d" />
<img width="1920" height="1080" alt="Screenshot 2026-03-08 164103" src="https://github.com/user-attachments/assets/f9a92fbf-fc25-4eb6-b46d-768d128a769a" />
<img width="1920" height="1080" alt="Screenshot 2026-03-08 164114" src="https://github.com/user-attachments/assets/c32235c1-9d24-4d65-8a29-53223e433bf1" />
<img width="1920" height="1080" alt="Screenshot 2026-03-08 154134" src="https://github.com/user-attachments/assets/706036b9-75e3-4760-a789-0e90f2cd6f32" />
ges/<img width="1920" height="1080" alt="Screenshot 2026-03-08 164114" src="https://github.com/user-attachments/assets/0892a8df-7e8d-457c-b72b-5cc63bef72df" />
app-preview.png)

## 📊 Features

- **Interactive Predictions**: Select any two teams and get instant win/draw probabilities
- **Team Statistics**: View average goals scored and conceded for each team
- **Machine Learning**: Random Forest model trained on historical match data (1872-2023)
- **User-Friendly Interface**: Clean, intuitive design built with Streamlit

![Prediction Demo](images/prediction-screenshot.png)

## 🛠️ Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web app framework
- **Scikit-learn** - Machine learning (Random Forest Classifier)
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Pickle/JSON** - Model serialization and data storage

## 📈 Model Performance

- **Accuracy**: ~52% (sports prediction is naturally challenging due to many variables)
- **Features Used**:
  - Team identity (encoded)
  - Average goals scored (home & away)
  - Average goals conceded (home & away)
- **Training Data**: International football matches from 1872-2023
- **Total Teams**: 200+ international teams

## 🏃 How to Run Locally

1. **Clone this repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/soccer-prediction-app.git
   cd soccer-prediction-app

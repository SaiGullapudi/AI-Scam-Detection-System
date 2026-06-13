import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# UI
st.set_page_config(
    page_title="AI Scam Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Scam Detection System")

st.markdown("""
### Intelligent SMS Scam Analyzer

This application uses **Natural Language Processing (NLP)** and
**Machine Learning** to detect scam messages.

Enter an SMS below and click **Predict**.
""")
st.info(
    "Example: Congratulations! You won ₹50,000. Claim your reward now."
)

message = st.text_area(
    "SMS Message",
    height=150,
    placeholder="Type or paste an SMS message here..."
)

# Prediction
if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter an SMS message.")
    else:
        transformed_message = vectorizer.transform([message])
        prediction = model.predict(transformed_message)
        probability = model.predict_proba(transformed_message)
        if prediction[0] == 1:
            confidence = probability[0][1] * 100
            st.error("🚨 Scam Message Detected")
            st.metric(
                label="Scam Confidence",
                value=f"{confidence:.2f}%"
            )
            st.progress(int(confidence))
        else:
            confidence = probability[0][0] * 100
            st.success("✅ Legitimate Message")
            st.metric(
                label="Legitimate Confidence",
                value=f"{confidence:.2f}%"
            )
            st.progress(int(confidence))
        
    
    
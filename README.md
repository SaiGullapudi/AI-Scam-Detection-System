# 🛡️ AI Scam Detection System

## Overview

AI Scam Detection System is a machine learning application that classifies SMS messages as **Scam** or **Legitimate** using Natural Language Processing (NLP) techniques and the Multinomial Naive Bayes algorithm.

The application is built with Streamlit and provides real-time predictions along with confidence scores.

## Features

* Detects Scam and Legitimate SMS messages
* Real-time prediction using Streamlit
* Confidence score display
* User-friendly web interface
* NLP-based text processing

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* TF-IDF Vectorizer
* Multinomial Naive Bayes

## Machine Learning Workflow

SMS Message

↓

TF-IDF Vectorization

↓

Multinomial Naive Bayes Model

↓

Prediction (Scam / Legitimate)

↓

Confidence Score

## Model Performance

* Accuracy: **95.55%**
* Algorithm: **Multinomial Naive Bayes**

## Project Structure

AI-Scam-Detection-System/

├── app.py

├── model.pkl

├── vectorizer.pkl

├── spam.csv

├── requirements.txt

└── README.md
1. Clone the repository
2. Install dependencies

pip install -r requirements.txt

3. Run the application

streamlit run app.py

## Author
Sai Gullapudi

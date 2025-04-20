# Career Predition APP
🎓 Career Guidance System
An intelligent, machine learning-powered web application that recommends personalized career paths and educational directions based on students' academic performance, interests, skills, and communication abilities.

📌 Overview
The Career Guidance System is designed to help students make informed, data-driven decisions about their future careers. Using models like Random Forest, SVM, and Decision Tree, it predicts suitable career roles, suggests relevant tools/programming languages, and even recommends higher education paths (e.g., MSc, MBA, MCA).

The system addresses the common issue of societal pressure and limited awareness of emerging career options by offering smart, interest-based alternatives.

🚀 Features
🔍 Predicts top 3 career roles with confidence scores

🎯 Recommends educational programs and skill paths

📈 Integrates job market trends and demand insights

🌐 Web-based user-friendly interface

🧠 ML-based engine (Random Forest, SVM, Decision Tree)

🗃️ Admin dashboard for feedback and analytics

📊 Resume correction and report download support

🧰 Tech Stack
💻 Backend
Python 3.x

Flask

Scikit-learn, Joblib, Pandas, NumPy

🌐 Frontend
HTML, CSS, JavaScript, Bootstrap

📊 ML Models
Random Forest (Career Role Prediction)

SVM (Education Suggestion)

Decision Tree (Tool Recommendation)

📦 Database
SQLite / MySQL

📈 Visualization
Matplotlib, Seaborn

📊 Dataset Details
~5000 student profiles

Features include GPA, communication skills, programming interests, language proficiency, etc.

Labels: Career roles, market demand, suggested tools

🧪 Model Performance

Model	Task	Accuracy
Random Forest	Career Role Prediction	94.7%
SVM	Education Path Suggestion	92.6%
Decision Tree	Tool Recommendation	90.1%
📋 Functional Requirements
User registration & login

Input form for student data

ML-based prediction engine

Visualization of predictions and confidence scores

Admin analytics dashboard

Run the application:
python app.py
Access via: http://localhost:5000

📅 Future Enhancements
Real-time job market API integration

Mobile app version (Android/iOS)

NLP-based resume analysis

Multilingual support

Federated learning for privacy-preserving customization

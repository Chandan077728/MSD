import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from imblearn.over_sampling import SMOTE
import joblib
import os

def evaluate_model(y_true, y_pred, model_name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall = recall_score(y_true, y_pred, average='macro', zero_division=0)  # Sensitivity
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
    cm = confusion_matrix(y_true, y_pred)

    tn = cm.sum(axis=1) - np.diag(cm)
    fp = cm.sum(axis=0) - np.diag(cm)
    specificity = tn / (tn + fp + 1e-10)  # Avoid divide-by-zero

    print(f"\n📘 Model: {model_name}")
    print(f"✅ Accuracy       : {acc*100:.2f}%")
    print(f"🎯 Precision      : {prec*100:.2f}%")
    print(f"🧠 Sensitivity    : {recall*100:.2f}%")
    print(f"📊 Specificity    : {np.mean(specificity)*100:.2f}%")
    print(f"🏅 F1 Score       : {f1*100:.2f}%")
    return acc, prec, recall, f1, np.mean(specificity)

def preprocess_and_train():
    df = pd.read_csv(r'C:\Users\HP\Career Guidance APP\career_dataset_.csv')
    df.columns = df.columns.str.strip()  # Clean any extra spaces

    # ✅ Use correct target column
    X = df.drop(columns=['career'])
    y = df['career']

    # Encode categorical input features if any
    encoders = {}
    for col in X.select_dtypes(include='object').columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        encoders[col] = le

    # Encode target labels
    label_enc = LabelEncoder()
    y = label_enc.fit_transform(y)

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Handle imbalance
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

    # Define models
    models = {
        "rf_model": RandomForestClassifier(n_estimators=300, max_depth=15, random_state=42),
        "svm_model": SVC(kernel='rbf', C=3, gamma='scale', probability=True, random_state=42),
        "dt_model": DecisionTreeClassifier(max_depth=10, criterion='entropy', random_state=42)
    }

    os.makedirs("models", exist_ok=True)

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        evaluate_model(y_test, y_pred, name)
        joblib.dump(model, f"models/{name}.pkl")

    joblib.dump(encoders, "models/encoders.pkl")
    joblib.dump(label_enc, "models/label_encoder.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

    print("\n✅ All models trained and saved successfully!")

if __name__ == "__main__":
    preprocess_and_train()

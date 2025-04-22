# 📉 Telco Customer Churn Prediction

A machine learning web application that predicts the likelihood of a telecom customer churning based on their usage patterns and demographics. Built with **Streamlit**, **Scikit-learn**, and **Pandas** for an interactive and user-friendly experience.

---

## 🚀 Features

- Predicts whether a customer is likely to churn.
- No file uploads required — enter customer details via the UI.
- Real-time prediction using a trained machine learning model.
- Clean, responsive dashboard using Streamlit.
- Modular code structure for scalability and maintenance.

---

## 🏗️ Project Structure

Telcom_performence/ ├── app/ │ ├── streamlit_app.py # Main Streamlit UI ├── scripts/ │ ├── utils.py # Load model and utilities │ ├── preprocessing.py # Input preprocessing │ ├── predict.py # Churn prediction logic │ ├── train_model.py # Model training script ├── models/ │ └── churn_model.pkl # Saved machine learning model ├── data/ │ └── telco_customer_churn.csv # Sample dataset (optional) ├── README.md # You're here!

yaml
Copy
Edit

---

## 🧠 Model Information

- **Algorithm**: Logistic Regression / Random Forest (customizable)
- **Target**: `Churn` (Yes/No)
- **Input Features**:
  - Gender, Senior Citizen, Partner, Dependents
  - Tenure, Monthly Charges, Total Charges
  - Internet & Phone Services
  - Contract Type, Payment Method, and more

---

## 🛠️ How to Run the App

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/telco-customer-churn.git
cd telco-customer-churn
2. Install Dependencies
Make sure you're using Python 3.12+.

bash
Copy
Edit
pip install -r requirements.txt
Or manually install:

bash
Copy
Edit
pip install streamlit pandas scikit-learn joblib
3. Train the Model (optional)
bash
Copy
Edit
python scripts/train_model.py
This saves the trained model to models/churn_model.pkl.

4. Run the App
bash
Copy
Edit
streamlit run app/streamlit_app.py
Visit http://localhost:8501 in your browser.


📎 Notes
If the model isn't found (churn_model.pkl), run the training script.

You can extend this with a database for storing predictions and analytics.

Works entirely offline.
![Screenshot (1336)](https://github.com/user-attachments/assets/de361342-3c4f-4d12-ba49-c9ee5f6affa3)
🧑‍💻 Author
Shad Ali
Final Year Student | ML & Data Science Enthusiast
LinkedIn | GitHub

📜 License
This project is open-source under the MIT License. Feel free to use, modify, and share.

yaml
Copy
Edit

---

Let me know if you'd like me to generate a `requirements.txt` or add badges (e.g., Streamlit app bad![Screenshot (1336)](https://github.com/user-attachments/assets/de361342-3c4f-4d12-ba49-c9ee5f6affa3)

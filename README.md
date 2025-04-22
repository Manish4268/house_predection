# 🏠 House Price Prediction

A machine learning project to predict house prices based on various features such as area, location, number of bedrooms, and more. This project includes data preprocessing, model training, evaluation, and a web-based interface for real-time predictions.

---

## 📊 Problem Statement

The goal is to predict housing prices using historical data. The model is trained on labeled datasets and can be used to assist users or real estate agents in estimating property values for new listings.

---

## ✨ Features

- 🧹 Data Cleaning and Preprocessing
- 📈 Model Training (Linear Regression, Decision Trees, etc.)
- 🔍 Evaluation with metrics (R² Score, MAE, RMSE)
- 🌐 Web App UI using Streamlit (or Flask, depending on version)
- 📤 Input form for real-time house price prediction

---

## 🧠 Technologies Used

- **Python**
- **Pandas**, **NumPy** – Data preprocessing
- **Scikit-learn** – Model training & evaluation
- **Matplotlib**, **Seaborn** – Data visualization
- **Streamlit** – Web interface for prediction

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/Manish4268/house_predection.git
   cd house_predection
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:
   ```bash
   streamlit run app.py
   ```

---

## 🧪 Model Workflow

1. Load dataset
2. Clean & encode features (e.g., one-hot encoding)
3. Train machine learning model
4. Save the model using `joblib`
5. Predict prices based on user input via web form

---

## 📁 Project Structure

```
/data                  # Dataset files
/models                # Trained model files
/app.py                # Streamlit or Flask app
/utils.py              # Helper functions
/EDA.ipynb             # Exploratory data analysis notebook
/requirements.txt      # Python dependencies
```

---

## 📌 Future Improvements

- Add more advanced models (e.g., XGBoost, Random Forest)
- Use location-specific pricing trends
- Add map-based feature for interactive predictions
- Deploy using Docker or cloud services

---

## 👨‍💻 Author

**Manish Shankar Jadhav**  
📧 [mn649712@dal.ca](mailto:mn649712@dal.ca)

---

## 🪪 License

This project is open-source under the [MIT License](LICENSE).

# 🏠 House Price Prediction Web App

A complete end-to-end data science project that predicts house prices using real estate listings scraped from [Zameen.com](https://www.zameen.com). Built as a project using Python, Machine Learning, Flask, and a simple HTML frontend.


## 📌 Features

- 🔍 **Scraped Dataset**: Extracts real-time property data (city, location, price, area, type, etc.) from Zameen.com.
- 🧹 **Data Cleaning & Preprocessing**: 
  - Handled missing values.
  - One-hot encoding for categorical features.
  - Feature scaling.
- 🤖 **Machine Learning Models**:
  - Trained and compared multiple regressors:  
    `LinearRegression`, `RandomForest`, `XGBoost`, `CatBoost`, `LGBM`, etc.
  - Selected the best model based on R² score and accuracy.
- 📊 **Visualization**:
  - Actual vs Predicted Prices.
  - Model Accuracy Comparison Bar Plot.
- 🌐 **Flask API + Frontend**:
  - User inputs house details via a simple web form.
  - Flask returns predicted price from the trained model.

---

## 🛠️ Tech Stack

| Area              | Tools/Libraries                            |
|-------------------|--------------------------------------------|
| Language          | Python                                     |
| Data Handling     | Pandas, NumPy                              |
| Modeling          | Scikit-learn, XGBoost, CatBoost, LightGBM  |
| Backend           | Flask                                      |
| Frontend          | HTML, CSS                                  |
| Visualization     | Matplotlib, Seaborn                        |
| Model Export      | Pickle                                     |

---

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/house-price-predictor.git
```
### 2. Train the Model
run simple_price_model.ipynb file and train the model

### 3. Run Frontend
```python app.py```
Run this command in terminal.

### 4. Optional Run to generate logo
```python .\static\generate_logo.py```

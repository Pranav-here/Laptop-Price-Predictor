# 💻 Laptop Price Predictor

This project predicts the **price of a laptop** based on its configuration using a **machine learning regression model**. It includes a **Streamlit web interface** for user input and instant price prediction.

🌐 **Live Demo**: *[]*

---

## 📂 Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit app for predicting laptop prices |
| `pipe.pkl` | Trained ML pipeline (Linear Regression or similar) |
| `df.pkl` | Preprocessed dataframe used for model input options |
| `Laptop Price Prediction.ipynb` | Notebook for data cleaning, feature engineering, and model training |
| `requirements.txt` | Required Python packages |
| `.gitignore`, `procfile` | Deployment configs (for platforms like Heroku) |
| `README.md` | This documentation |

---

## 🧠 Features Used

- Brand (`Company`)
- Type of laptop (`TypeName`)
- RAM (in GB)
- Weight
- Touchscreen (binary)
- IPS Panel (binary)
- Screen Size (in inches)
- Screen Resolution (used to calculate PPI)
- CPU brand
- HDD and SSD storage
- GPU brand
- Operating System

Derived Feature:
- **PPI (Pixels Per Inch)** – calculated from resolution and screen size

---

## 🚀 How to Use

```bash
git clone https://github.com/Pranav-here/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Author

**Pranav Kuchibhotla**  
🔗 [GitHub](https://github.com/Pranav-here) 
---

⚠️ This model is for educational purposes and works best on laptops similar to those in the dataset.

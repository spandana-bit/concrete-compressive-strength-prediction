#  Concrete Compressive Strength Prediction Using Machine Learning

##  Project Overview

This project is a **Machine Learning-based Concrete Compressive Strength Prediction System** developed using Python and Streamlit.

The system predicts the **compressive strength of concrete in MPa** based on its composition and curing age.

The project uses Machine Learning **regression algorithms** to learn the relationship between concrete ingredients, age, and compressive strength.

A Streamlit web application is developed where users can enter concrete composition values and obtain a predicted compressive strength. The application loads a trained Machine Learning model and scaler using Joblib.

---

##  Objectives

The main objectives of this project are:

* To predict concrete compressive strength using Machine Learning.
* To treat concrete strength prediction as a regression problem.
* To use concrete composition and curing age as input features.
* To compare different regression algorithms.
* To evaluate models using MAE, MSE, RMSE, and R².
* To save the trained model for future predictions.
* To develop an interactive Streamlit web application.
* To provide concrete strength predictions in MPa.

---

##  Machine Learning Problem

### Type of Problem

**Supervised Machine Learning – Regression**

The target variable is a continuous numerical value:

```text
Concrete Compressive Strength (MPa)
```

The model predicts the strength rather than assigning the concrete to a category.

---

##  Input Features

The application uses **8 input features**:

| No. | Feature            | Unit  |
| --: | ------------------ | ----- |
|   1 | Cement             | kg/m³ |
|   2 | Blast Furnace Slag | kg/m³ |
|   3 | Fly Ash            | kg/m³ |
|   4 | Water              | kg/m³ |
|   5 | Superplasticizer   | kg/m³ |
|   6 | Coarse Aggregate   | kg/m³ |
|   7 | Fine Aggregate     | kg/m³ |
|   8 | Age                | Days  |

These are the same input fields used in the Streamlit application.

---

##  Target Variable

The target of the Machine Learning model is:

```text
Concrete Compressive Strength
```

The predicted result is displayed in:

```text
MPa
```

---

##  Regression Algorithms

The project compares multiple Machine Learning regression algorithms, including:

* Linear Regression
* Polynomial Regression
* Decision Tree Regression
* Random Forest Regression
* Support Vector Regression (SVR)
* Gradient Boosting Regression

The models are evaluated using standard regression metrics.

---

##  Evaluation Metrics

The project evaluates the regression models using:

### MAE – Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

### MSE – Mean Squared Error

Measures the average squared prediction error and gives greater importance to larger errors.

### RMSE – Root Mean Squared Error

The square root of MSE. It measures prediction error in the same unit as the target.

### R² – R-squared

Measures how well the model explains the variation in the target variable.

---

##  Model Selection

The regression models are compared using the evaluation metrics.

The model with the best evaluation performance is saved as:

```text
best_concrete_strength_model.pkl
```

This saved model is used by the Streamlit application for making new predictions.

---

##  Data Preprocessing

A scaler is used for the Machine Learning workflow and saved as:

```text
concrete_scaler.pkl
```

The Streamlit application loads the saved scaler together with the trained model.

For model types that require scaling, the application transforms the input data before prediction.

---

##  Streamlit Application

The project includes an interactive Streamlit application.

The user enters:

```text
Cement
Blast Furnace Slag
Fly Ash
Water
Superplasticizer
Coarse Aggregate
Fine Aggregate
Age
```

Then the user clicks:

```text
 Predict Concrete Strength
```

The application predicts and displays the estimated compressive strength in MPa.

---

##  Project Workflow

```text
Concrete Dataset
       ↓
Data Preprocessing
       ↓
Exploratory Data Analysis
       ↓
Feature Selection
       ↓
Train-Test Split
       ↓
Train Regression Models
       ↓
Model Evaluation
       ↓
Compare MAE, MSE, RMSE & R²
       ↓
Select Best Model
       ↓
Save Model and Scaler
       ↓
Streamlit Application
       ↓
User Enters Concrete Data
       ↓
Prediction
       ↓
Concrete Strength in MPa
```

---

##  Project Structure

```text
concrete-compressive-strength-prediction/
│
├── app.py
├── concrete.ipynb
├── best_concrete_strength_model.pkl
├── concrete_scaler.pkl
├── concrete_prediction_results.xlsx
├── requirements.txt
└── README.md
```

### File Description

| File                               | Description                                     |
| ---------------------------------- | ----------------------------------------------- |
| `app.py`                           | Streamlit web application                       |
| `concrete.ipynb`                   | Machine Learning training and analysis notebook |
| `best_concrete_strength_model.pkl` | Saved trained regression model                  |
| `concrete_scaler.pkl`              | Saved feature scaler                            |
| `concrete_prediction_results.xlsx` | Prediction results                              |
| `requirements.txt`                 | Required Python libraries                       |
| `README.md`                        | Project documentation                           |

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Jupyter Notebook
* Streamlit
* Matplotlib
* Seaborn
* Excel

---

##  Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/concrete-compressive-strength-prediction.git
```

### 2. Open the Project Folder

```bash
cd concrete-compressive-strength-prediction
```

### 3. Create a Python Environment

```bash
conda create -n concrete python=3.10 -y
```

Activate the environment:

```bash
conda activate concrete
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Run the Application

Run:

```bash
streamlit run app.py
```

The Streamlit application will open in your web browser.

---

##  Example Prediction
Example input:

```text
Cement              = 350 kg/m³
Blast Furnace Slag  = 100 kg/m³
Fly Ash             = 50 kg/m³
Water               = 180 kg/m³
Superplasticizer    = 10 kg/m³
Coarse Aggregate    = 1000 kg/m³
Fine Aggregate      = 700 kg/m³
Age                 = 28 days
```

After clicking:

```text
 Predict Concrete Strength
```

the application displays:

```text
Predicted Concrete Strength
XX.XX MPa
```

The actual value depends on the trained model and input values.

---

##  Deployment

The Streamlit application can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Upload the project to GitHub.
2. Connect the GitHub repository to Streamlit Community Cloud.
3. Select the `main` branch.
4. Select `app.py` as the main file.
5. Deploy the application.

Make sure these files are included in the repository:

```text
app.py
best_concrete_strength_model.pkl
concrete_scaler.pkl
requirements.txt
```

The application requires the trained model and scaler when it starts.

---

##  Application Output

The application provides:

* Predicted compressive strength
* Prediction value in MPa
* Entered concrete composition
* Input data preview
* Project information

The application displays the entered input data through the **View Input Data** section.

---

## Author

**Spandana**

B.Tech – Computer Science and Engineering

---

##  License

This project is developed for **educational and academic purposes**.

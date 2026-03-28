# 📋 Project Statement

## Student Performance Predictor using Machine Learning

---

## 1. 🎯 Project Title

**Student Performance Predictor — Pass / Fail Classification using Machine Learning**

---

## 2. 📌 Problem Statement

In educational institutions, identifying students who are at risk of failing
is a critical challenge. Traditional methods of evaluating student performance
rely on periodic exams and manual observation, which are often too late to
take corrective action.

This project aims to build a **Machine Learning-based classification system**
that can predict whether a student will **Pass or Fail** based on key academic
and lifestyle factors — enabling early intervention and personalized support.

---

## 3. 🎓 Objective

- To develop a supervised Machine Learning model that predicts student academic performance.
- To identify the most influential factors affecting student outcomes.
- To provide a tool that educators and institutions can use for **early risk detection**.
- To compare multiple classification algorithms and select the best-performing model.

---

## 4. 📊 Dataset Description

The dataset consists of **40 student records** with the following features:

| Feature          | Description                            | Range       |
|------------------|----------------------------------------|-------------|
| `hours_study`    | Number of hours a student studies/day  | 1 – 10      |
| `attendance`     | Percentage of classes attended         | 40 – 100 %  |
| `sleep_hours`    | Number of hours of sleep per day       | 4 – 10      |
| `previous_score` | Score obtained in the previous exam    | 40 – 100    |
| `performance`    | Target variable — 0 = Fail, 1 = Pass   | Binary      |

**Class Distribution:**
- Pass (1) : 25 students
- Fail (0) : 15 students

---

## 5. 🛠️ Methodology

### Step 1 — Data Collection
A structured CSV dataset is used as input containing student academic
and lifestyle attributes.

### Step 2 — Data Preprocessing
- Load dataset using Pandas
- Split into features (X) and target (y)
- Apply **StandardScaler** for feature normalization
- Split into training (80%) and testing (20%) sets

### Step 3 — Model Training
Four classification algorithms are trained and evaluated:

| Algorithm           | Type                   |
|---------------------|------------------------|
| Random Forest       | Ensemble (Bagging)     |
| Gradient Boosting   | Ensemble (Boosting)    |
| Logistic Regression | Linear Classifier      |
| SVM (RBF Kernel)    | Kernel-based Classifier|

### Step 4 — Model Evaluation
Each model is evaluated using:
- **Test Accuracy** — performance on unseen data
- **5-Fold Cross Validation** — generalization check
- **Classification Report** — Precision, Recall, F1-Score
- **Confusion Matrix** — True/False Positives & Negatives
- **ROC-AUC Score** — discrimination ability

### Step 5 — Best Model Selection
The model with the highest test accuracy is automatically selected
as the final predictor.

### Step 6 — Prediction
The trained model predicts Pass/Fail for:
- Individual student input (interactive mode)
- Batch of students from CSV file

---

## 6. 🔍 Key Findings

| Finding                        | Detail                                      |
|-------------------------------|---------------------------------------------|
| Best Model                    | Random Forest (100% Test Accuracy)          |
| Most Important Feature        | Attendance (42% importance)                 |
| Second Most Important         | Previous Score (26% importance)             |
| ROC-AUC Score                 | 1.0 (perfect separation)                    |
| Cross-Validation Accuracy     | 95% (Random Forest)                         |

**Feature Importance Ranking:**
1. `attendance`      → 42.02%
2. `previous_score`  → 26.43%
3. `hours_study`     → 17.51%
4. `sleep_hours`     → 14.04%

---

## 7. 💻 Tools & Technologies

| Category         | Technology              |
|------------------|-------------------------|
| Language         | Python 3.8+             |
| Data Handling    | Pandas, NumPy           |
| Machine Learning | Scikit-learn            |
| Algorithms       | Random Forest, Gradient Boosting, Logistic Regression, SVM |
| IDE              | VS Code / Jupyter / PyCharm |
| Version Control  | Git / GitHub            |

---

## 8. 📂 Project Files

| File                        | Description                                  |
|-----------------------------|----------------------------------------------|
| `student_predictor_v2.py`   | Main Python script — training & prediction   |
| `student_data.csv`          | Input dataset (40 student records)           |
| `requirements.txt`          | Python package dependencies                  |
| `README.md`                 | Project setup and usage guide                |
| `statement.md`              | This project statement document              |

---

## 9. ▶️ How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the predictor
python student_predictor_v2.py
```

---

## 10. 📈 Expected Output

```
MODEL COMPARISON
─────────────────────────────────────────────────
Random Forest        Test: 100.0%  CV: 95.0%  ◄ BEST
Gradient Boosting    Test:  75.0%  CV: 95.0%
Logistic Regression  Test: 100.0%  CV: 97.5%
SVM (RBF Kernel)     Test: 100.0%  CV: 97.5%

Feature Importance:
attendance         █████████████████████  0.4202
previous_score     █████████████          0.2643
hours_study        ████████               0.1751
sleep_hours        ███████                0.1404
```

---

## 11. 🚀 Future Scope

- Expand dataset with more student records for better generalization
- Add additional features: parental education, internet access, extracurriculars
- Build a **Streamlit web application** for non-technical users
- Deploy as a **REST API** using Flask or FastAPI
- Integrate **SHAP (SHapley Additive exPlanations)** for model explainability
- Use **deep learning** (Neural Networks) for larger datasets
- Enable **real-time predictions** from a student management system

---

## 12. ✅ Conclusion

This project successfully demonstrates the use of Machine Learning to predict
student academic performance. The **Random Forest classifier** achieved
**100% accuracy** on the test set with a **ROC-AUC score of 1.0**, proving
the strong predictability of the selected features.

The analysis reveals that **attendance is the most critical factor** in
determining student success, followed by previous academic scores.
This system can serve as an effective **early warning tool** for educators
to identify at-risk students and provide timely support.

---

*Project developed for academic and educational purposes.*

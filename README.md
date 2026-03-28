#  Student Performance Predictor (Pass / Fail)

A Machine Learning project that predicts whether a student will **Pass or Fail**
based on Study Hours, Attendance, Sleep Hours, and Previous Score.

---

##  Project Structure

```
student-performance-predictor/
│
├── student_predictor_v2.py    # Main ML model & predictor
├── student_data.csv           # Your dataset (40 students)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

##  Dataset Description (`student_data.csv`)

| Column           | Type    | Range     | Description                        |
|------------------|---------|-----------|------------------------------------|
| `hours_study`    | Integer | 1 – 10    | Daily study hours                  |
| `attendance`     | Integer | 40 – 100  | Class attendance percentage        |
| `sleep_hours`    | Integer | 4 – 10    | Daily sleep hours                  |
| `previous_score` | Integer | 40 – 100  | Previous exam score                |
| `performance`    | Integer | 0 or 1    | **0 = Fail** / **1 = Pass**        |

### Class Distribution

| Label | Value | Count |
|-------|-------|-------|
| Pass  |   1   |  25   |
| Fail  |   0   |  15   |

---

##  Installation

```bash
pip install -r requirements.txt
```

**Requirements:**
```
numpy>=1.24
pandas>=2.0
scikit-learn>=1.3
```

---

##  How to Run

```bash
python student_predictor_v2.py
```

The script will:
1. Load and explore `student_data.csv`
2. Train **4 ML models** and compare accuracy + cross-validation scores
3. Select the **best model** automatically
4. Show batch predictions on the full dataset
5. Display sample student predictions with probabilities
6. Launch **interactive mode** — enter student values manually

---

##  Models Used

| Model               | Test Acc | CV Acc | Notes                          |
|---------------------|----------|--------|--------------------------------|
| Random Forest       | 100%     | 95%    | Best — ensemble of trees       |
| Gradient Boosting   | 75%      | 95%    | Strong with more data          |
| Logistic Regression | 100%     | 97.5%  | Linear, fast, interpretable    |
| SVM (RBF Kernel)    | 100%     | 97.5%  | Great for small datasets       |

---

##  Feature Importance (Random Forest)

```
attendance         █████████████████████  0.4202  <- Most important
previous_score     █████████████          0.2643
hours_study        ████████               0.1751
sleep_hours        ███████                0.1404
```

**Attendance** is the strongest predictor of Pass/Fail in this dataset.

---

##  Sample Output

```
  Student 1  Pass
    Study: 8h  Attendance: 90%  Sleep: 8h  Prev Score: 78
    Pass Probability : ████████████████████  100.0%
    Fail Probability : ░░░░░░░░░░░░░░░░░░░░    0.0%

  Student 2  Fail
    Study: 2h  Attendance: 55%  Sleep: 5h  Prev Score: 42
    Pass Probability :                          0.0%
    Fail Probability : ████████████████████  100.0%
```

---

##  Predict Your Own Student

```python
from student_predictor_v2 import StudentPerformancePredictor
import pandas as pd

df        = pd.read_csv("student_data.csv")
predictor = StudentPerformancePredictor()
predictor.train(df)

result = predictor.predict_one(
    hours_study    = 6,
    attendance     = 80,
    sleep_hours    = 7,
    previous_score = 65
)
print(result)
# {'prediction': 1, 'label': 'Pass', 'pass_prob': 100.0, 'fail_prob': 0.0}
```

---

##  Future Improvements

- [ ] Add more student records for better generalization
- [ ] Hyperparameter tuning with GridSearchCV
- [ ] Streamlit web UI with input form
- [ ] Export model using joblib for deployment
- [ ] Add SHAP values for explainability

---

## 📄 License

Open-source — free to use for educational and academic purposes.

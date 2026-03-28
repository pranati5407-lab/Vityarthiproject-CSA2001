# ==========================================
# STUDENT PERFORMANCE PREDICTOR
# (NO LIBRARIES NEEDED - PURE PYTHON)
# ==========================================

import random

# ------------------------------------------
# STEP 1: Generate Dataset
# ------------------------------------------

def generate_data(num_samples):
    data = []

    for _ in range(num_samples):
        hours = random.randint(0, 10)
        attendance = random.randint(50, 100)
        sleep = random.randint(4, 10)
        previous = random.randint(40, 100)

        # Rule-based performance
        if hours >= 5 and attendance >= 75 and previous >= 60:
            performance = 1
        else:
            performance = 0

        data.append([hours, attendance, sleep, previous, performance])

    return data

# ------------------------------------------
# STEP 2: "Training" (Simple Logic Learning)
# ------------------------------------------

def train_model(data):
    # Calculate average values for high performers
    high_perf = [d for d in data if d[4] == 1]

    avg_hours = sum(d[0] for d in high_perf) / len(high_perf)
    avg_attendance = sum(d[1] for d in high_perf) / len(high_perf)
    avg_sleep = sum(d[2] for d in high_perf) / len(high_perf)
    avg_previous = sum(d[3] for d in high_perf) / len(high_perf)

    model = {
        "hours": avg_hours,
        "attendance": avg_attendance,
        "sleep": avg_sleep,
        "previous": avg_previous
    }

    return model

# ------------------------------------------
# STEP 3: Prediction Function
# ------------------------------------------

def predict(model, hours, attendance, sleep, previous):
    
    score = 0

    if hours >= model["hours"]:
        score += 1
    if attendance >= model["attendance"]:
        score += 1
    if sleep >= model["sleep"]:
        score += 1
    if previous >= model["previous"]:
        score += 1

    # Decision rule
    if score >= 3:
        return 1
    else:
        return 0

# ------------------------------------------
# STEP 4: Accuracy Check
# ------------------------------------------

def evaluate(model, data):
    correct = 0

    for d in data:
        pred = predict(model, d[0], d[1], d[2], d[3])
        if pred == d[4]:
            correct += 1

    accuracy = correct / len(data) * 100
    return accuracy

# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

print("📊 Generating student data...")
dataset = generate_data(100)

print("🧠 Training model...")
model = train_model(dataset)

print("📈 Evaluating model...")
accuracy = evaluate(model, dataset)

print(f"Model Accuracy: {accuracy:.2f}%")

# ------------------------------------------
# USER INPUT
# ------------------------------------------

print("\n🎓 Enter student details:")

try:
    hours = float(input("Study hours (0–10): "))
    attendance = float(input("Attendance % (50–100): "))
    sleep = float(input("Sleep hours (4–10): "))
    previous = float(input("Previous score (40–100): "))

    result = predict(model, hours, attendance, sleep, previous)

    print("\nResult:")
    if result == 1:
        print("🎯 High Performance Expected")
    else:
        print("⚠️ Low Performance Expected")

except:
    print("Invalid input. Please enter numbers only.")

print("\n✅ Program Finished Successfully!")

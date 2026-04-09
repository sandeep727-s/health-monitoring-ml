import numpy as np
import pandas as pd

# --------------------------------------------------------------
# SIMULATED HEALTH DATA
# --------------------------------------------------------------
data = {
    "heart_rate": [72, 85, 90, 110, 60, 95, 130],
    "temperature": [36.5, 37.0, 38.5, 39.0, 36.2, 37.8, 40.0]
}

df = pd.DataFrame(data)

print("Health Data:\n")
print(df)

# --------------------------------------------------------------
# SIMPLE ANOMALY DETECTION
# --------------------------------------------------------------
def detect_abnormal(row):
    if row["heart_rate"] > 100 or row["temperature"] > 38:
        return "ABNORMAL"
    else:
        return "NORMAL"

df["status"] = df.apply(detect_abnormal, axis=1)

# --------------------------------------------------------------
# RESULTS
# --------------------------------------------------------------
print("\nHealth Status:\n")
print(df)

# --------------------------------------------------------------
# SUMMARY
# --------------------------------------------------------------
abnormal_count = (df["status"] == "ABNORMAL").sum()

print("\nTotal Abnormal Cases:", abnormal_count)
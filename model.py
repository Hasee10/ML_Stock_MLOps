import pandas as pd
import pickle
import wandb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 🧪 Initialize Weights & Biases
wandb.init(project="ml-stock-classifier", name="run-1")

# 📥 Load dataset
df = pd.read_csv("data.csv")

# ✂️ Preprocessing (replace 'label' with your actual target column name)
X = df.drop(columns=["label"])
y = df["label"]

# 🔀 Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🎯 Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔍 Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("✅ Accuracy:", accuracy)

# 📊 Log metrics to W&B
wandb.log({"accuracy": accuracy})

# 💾 Save trained model as a .pkl file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# ✅ Finish the W&B run
wandb.finish()

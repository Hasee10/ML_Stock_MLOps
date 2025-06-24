# 🤖 ML Stock Movement Classifier with MLOps

![GitHub Workflow Status](https://github.com/Hasee10/ML_Stock_MLOps/actions/workflows/run-model.yml/badge.svg)
![DVC Versioning](https://img.shields.io/badge/DVC-enabled-blue)
![W&B Logging](https://img.shields.io/badge/W%26B-logging-green)

Welcome to **ML_Stock_MLOps**, a fully automated and production-ready MLOps project designed to classify stock movement trends using historical Amazon stock data. This repository demonstrates how to set up a robust ML pipeline with:

- ⚙️ **GitHub Actions** for CI/CD
- 📦 **DVC (Data Version Control)** for dataset + model tracking
- 📊 **Weights & Biases (W&B)** for experiment logging
- 🧠 **Scikit-Learn** for model training
- ☁️ **Google Drive** for remote storage

---

## 📁 Project Structure

```bash
ML_Stock_MLOps/
├── .dvc/                    # DVC metadata
├── .github/
│   └── workflows/
│       └── run-model.yml   # GitHub Actions workflow
├── fetch_data.py           # Dataset download script
├── model.py                # Training + logging
├── data.csv.dvc            # DVC pointer to dataset
├── dvc-sa-key.json         # (Ignored) GDrive auth key
├── model.pkl               # Saved model artifact
├── requirements.txt        # Dependencies
└── README.md               # This file
```

---

## 🚀 Features

### 🔁 1. GitHub Actions CI/CD
Every push to `main` branch automatically:
- Pulls the dataset from Google Drive
- Trains the model using `model.py`
- Logs metrics to W&B (accuracy)
- Uploads `model.pkl` as an artifact

### 📦 2. Data Versioning with DVC
- DVC tracks `data.csv` via `data.csv.dvc`
- The actual file is stored on **Google Drive**
- Enables consistent, reproducible experiments

### 📊 3. Experiment Tracking with W&B
- Accuracy and metadata are logged per run
- Visualize comparisons across different commits

---

## 🧪 Example Metrics Logged

| Run | Accuracy | Model Version | Notes              |
|-----|----------|----------------|---------------------|
| #1  | 0.812    | v1             | Initial baseline    |
| #2  | 0.835    | v2             | Tuned hyperparams   |

🔗 View logs on: [W&B Dashboard](https://wandb.ai/YOUR_USERNAME/ml_stock_mlops)

---

## 📦 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Hasee10/ML_Stock_MLOps.git
cd ML_Stock_MLOps
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup DVC Remote with GDrive
```bash
dvc remote add -d gdrive_remote gdrive://<your-folder-id>
dvc remote modify gdrive_remote gdrive_use_service_account true
dvc remote modify gdrive_remote gdrive_service_account_json_file_path dvc-sa-key.json
```

### 4. Pull the Dataset
```bash
dvc pull
```

### 5. Train the Model Locally
```bash
python model.py
```

---

## 🔄 Workflow Automation

### GitHub Actions
The workflow in `.github/workflows/run-model.yml`:
- Runs on every push to `main`
- Pulls data using DVC
- Trains the model
- Logs to W&B
- Uploads `model.pkl`

No manual intervention needed after setup! ✅

---

## 📤 Deployment Ideas (Next Steps)

| Step               | Tools You Can Use           |
|--------------------|------------------------------|
| Live Inference     | Streamlit / Flask            |
| Model Registry     | MLflow / W&B Artifacts       |
| Auto Retraining    | Cron + GitHub Actions        |
| Data Drift Monitor | Evidently / Grafana          |

Let me know if you’d like to implement these — happy to guide you!

---

## 💡 Why This Project Stands Out

✔️ **Real-world data** from Amazon stock history  
✔️ **End-to-end pipeline** from data to deployment  
✔️ **Resume-ready**, **client-attracting** project  
✔️ Showcases **production-level MLOps principles**

---

## 👨‍💻 Author

**Muhammad Haseeb Arshad**  
📧 haseeb.arshad@example.com  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)  

---

## ⭐ Star This Repo If You Like It!

Your support keeps the projects coming 🚀

---

> _Built with ❤️ using Python, GitHub Actions, DVC, and W&B._


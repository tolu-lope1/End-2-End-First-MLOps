# End-2-End-First-MLOps

## Overview

This project demonstrates an end-to-end MLOps workflow for diabetes prediction using a Random Forest Classifier. It covers data ingestion, partitioning, model training, testing, and serving predictions via a FastAPI REST API.

## Directory Structure

```
End-2-End-First-MLOps/
├── app.py                # FastAPI app for serving predictions
├── config.py             # Configuration variables
├── main.py               # Main pipeline script (ingest, split, train, test)
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── model_data/           # Contains train.csv and test.csv
├── model_output/         # Stores trained model and scaler
├── src/                  # Source code for pipeline steps
│   ├── data_ingestion.py
│   ├── data_partition.py
│   ├── train.py
│   └── test.py
└── ...
```

## Setup Instructions

1. **Clone the repository and navigate to the project directory:**
	 ```bash
	 git clone <repo-url>
	 cd End-2-End-First-MLOps
	 ```

2. **(Recommended) Create a virtual environment:**
	 ```bash
	 python3 -m venv .venv
	 source .venv/bin/activate
	 ```

3. **Install dependencies:**
	 ```bash
	 pip install -r requirements.txt
	 ```

## Running the Pipeline

To run the full pipeline (data ingestion, partitioning, training, and testing):

```bash
python main.py
```

This will:
- Download the diabetes dataset
- Split it into train/test CSVs
- Train a Random Forest model
- Save the model and scaler
- Test the model on the test set

## Running the API Server

To serve predictions via REST API using FastAPI:

```bash
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000/`.

### Example API Usage

- **Health check:**
	- `GET /` returns a status message.
- **Single prediction:**
	- `POST /single-predict` with JSON body containing feature values.
- **Batch prediction:**
	- `POST /multi-predict` with a list of JSON objects.

## DIY: Customization & Extension

- **Change dataset:** Edit `dataset_url` in `config.py`.
- **Modify features or model:** Update `features` in `config.py` or change the model in `src/train.py`.
- **Add new endpoints:** Extend `app.py` with new FastAPI routes.
- **Experiment:** Try different ML algorithms or preprocessing steps in the `src/` modules.

## Notes

- Output files (`train.csv`, `test.csv`, model artifacts) are auto-generated in `model_data/` and `model_output/`.
- `.gitignore` excludes CSVs and system files.

---
For any issues or contributions, please open an issue or PR.

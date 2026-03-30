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

kubectl port-forward svc/diabetes-model-service 1111:80 --address=0.0.0.0
docker build -t diabetes-model-demo .
docker ps
docker run -p 8000:8000 diabetes-model-demo    
docker images
docker login
docker tag 7068e87f77fe tolulopeodetola1/diabetes-model-demo:latest
docker push tolulopeodetola1/diabetes-model-demo:latest

---

## Notes & Troubleshooting

- Output files (`train.csv`, `test.csv`, model artifacts) are auto-generated in `model_data/` and `model_output/`.
- `.gitignore` excludes CSVs and system files.
- If you encounter issues with dependencies, try upgrading pip: `pip install --upgrade pip`.
- Make sure your Python version is 3.7 or higher.

---

## 🐳 Docker: Containerize the App

Build and run the application in a Docker container for portability and deployment:

```bash
# Build the Docker image
docker build -t diabetes-model-demo .

# List Docker images
docker images

# Run the container, exposing port 8000
docker run -p 8000:8000 diabetes-model-demo

# (Optional) Check running containers
docker ps
```

### Push Docker Image to Docker Hub

```bash
# Log in to Docker Hub
docker login

# Tag your image (replace <image_id> with your actual image ID)
docker tag <image_id> tolulopeodetola1/diabetes-model-demo:latest

# Push to Docker Hub
docker push tolulopeodetola1/diabetes-model-demo:latest
```

---

## ☸️ Kubernetes: Deploy on a Cluster

You can deploy the app to a local or cloud Kubernetes cluster using [kind](https://kind.sigs.k8s.io/) or any K8s provider.

```bash
# Create a local cluster (with kind)
kind create cluster --name=demo-mlops

# Check cluster nodes
kubectl get nodes

# Apply deployment (ensure deploy.yml is configured)
kubectl apply -f deploy.yml

# Watch pod status
kubectl get pods -w

# Get services
kubectl get svc

# Forward service port to localhost (replace service name if needed)
kubectl port-forward svc/diabetes-model-service 1111:80 --address=0.0.0.0

# Now access the API at http://localhost:1111
```

---

## 📺 Reference & Learning

- [YouTube: End-to-End MLOps Demo](https://www.youtube.com/watch?v=hw17NDhjVHo)
- Official docs: [FastAPI](https://fastapi.tiangolo.com/), [Docker](https://docs.docker.com/), [Kubernetes](https://kubernetes.io/docs/)

---

## 🤝 Contributing & Support

For any issues or contributions, please open an issue or PR.
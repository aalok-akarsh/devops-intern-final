MLflow Tracking (Dummy Experiment)

This adds a small local MLflow tracking run to show experiment logging.

Prereqs:
- Python 3.x
- Optional: virtualenv

Steps:
  cd /mnt/c/Users/alokp/devops-intern-final-project

  python3 -m venv .venv-mlflow
  source .venv-mlflow/bin/activate
  pip install mlflow

  # Run the dummy experiment
  python3 mlflow/run_experiment.py

  # View the run in the MLflow UI
  mlflow ui --backend-store-uri ./mlruns

Then open:
  http://127.0.0.1:5000

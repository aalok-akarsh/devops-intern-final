import mlflow
import time


def main() -> None:
    mlflow.set_experiment("devops-intern-final")
    with mlflow.start_run(run_name="dummy-run"):
        mlflow.log_param("model", "demo")
        mlflow.log_param("owner", "alok")
        mlflow.log_metric("accuracy", 0.42)
        mlflow.log_metric("loss", 0.58)
        mlflow.log_metric("timestamp", int(time.time()))


if __name__ == "__main__":
    main()

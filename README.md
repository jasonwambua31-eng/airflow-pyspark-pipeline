# Scalable Big Data ETL Pipeline (Airflow & PySpark)

An automated, containerized data engineering pipeline built to process large datasets using **Apache Airflow** for orchestration and **Apache PySpark** for distributed data transformation.

# The tech stack 
* **Orchestration:** Apache Airflow (DAGs, Scheduler, Workers)
* **Processing Engine:** Apache PySpark (SparkSession, DataFrames)
* **Containerization:** Docker & Docker Compose (Custom Image with Java & PySpark)
* **Message Broker / Metadata DB:** Redis & PostgreSQL
* **Language:** Python

# HOW works
1. **Custom Docker Image:** Instead of relying on startup scripts, a custom `Dockerfile` bakes Java 17 and PySpark directly into the Airflow image for production-ready reliability.
2. **Extract Task:** Downloads raw data and stages it in the local environment.
3. **Transform Task (PySpark):** Initializes a SparkSession to perform heavy, distributed aggregations (GroupBy, Averages) that would crash standard Pandas.
4. **Load Task:** Saves the cleaned, aggregated data into highly optimized **Parquet** format.

# How to run locally 
*(Requires Docker Desktop with at least 4GB+ of RAM allocated)*

1. Clone this repository.
2. Ensure you have a `.env` file with your Airflow credentials.
3. Build the custom image and start the containers:
   ```bash
   docker compose up -d --build
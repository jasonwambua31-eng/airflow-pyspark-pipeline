#CREATING MY OWN IMAGE SINDE THE SCHEDULAR AND WEBSERVER ARE UN HEALTHY WHEN I TRY TO RUN THE CONTAINER WITH THE OFFICIAL IMAGE. I THINK IT IS BECAUSE OF THE PIP INSTALLATION OF PYSPARK. SO I AM CREATING MY OWN IMAGE WITH PYSPARK INSTALLED.
FROM apache/airflow:2.8.1
USER root

#install java
RUN apt-get update && \
    apt-get install -y openjdk-17-jre-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER airflow
RUN pip install --no-cache-dir pyspark
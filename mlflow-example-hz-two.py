# Databricks notebook source
# hello
%pip install mlflow

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import mlflow

with mlflow.start_run() as run:
  mlflow.log_param("name", "world")
  mlflow.log_metric("accuracy", 0.95)

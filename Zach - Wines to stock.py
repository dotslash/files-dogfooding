# Databricks notebook source
import utils
# from utils import data_without_spaces

data = utils.data_without_spaces()

# COMMAND ----------

# Wines with free_sulfur_dioxide less than 15 can be labelled as no added sulfur

no_added_sulfur = (data["free_sulfur_dioxide"] <= 15).astype(int)
data["no_added_sulfur"] = no_added_sulfur

# COMMAND ----------

# Wines with residual_sugar less than 2 is considered brut

is_brut = (data["residual_sugar"] <= 2).astype(int)
data["brut"] = is_brut

def data_without_spaces():
  import pandas as pd

  # Load wine data
  data = pd.read_csv("winequality-red.csv", sep=";")

  # Remove spaces from column names
  data.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)
  
  return data

def foo():
  return "ok"
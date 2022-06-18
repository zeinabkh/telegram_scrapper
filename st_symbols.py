import pandas as pd
import numpy as np
# read symbols
symbols_list = pd.read_excel("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\processed_data\\symbols_list.xlsx")
deterministic_symbols = symbols_list.loc[symbols_list['label']==0, 'نماد'].to_numpy()
data = pd.read_excel("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\processed_data\\labeled_data2.xlsx")
data_positive = data.loc[data['labels'] == 1,"texts"].to_numpy()
data_negative = data.loc[data['labels'] == -1,"texts"].to_numpy()

symbols_st_pos = {s: 0 for s in deterministic_symbols}
symbols_st_neg = {s: 0 for s in deterministic_symbols}
for t in data_negative:
  try:
   for s in deterministic_symbols:
      if t.find(s) != -1:
          symbols_st_neg[s] += 1
  except AttributeError:
      continue

for t in data_positive:
  try:
    for s in deterministic_symbols:
        if t.find(s) != -1:
            symbols_st_pos[s] += 1
  except AttributeError:
      continue


print("negative",sorted(symbols_st_neg.items(), key=lambda item: item[1],reverse=True))
print("positive",sorted(symbols_st_pos.items(), key=lambda item: item[1],reverse=True))


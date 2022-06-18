import os
import pandas as pd
import urllib3
symbol_list = pd.read_csv("symbol.csv")
# symbol_list.head()

link = "https://tse.ir/en/Archive/Trade/Cash/SymbolTrade/SymbolTrade_IRO1BMLT0001_2021.xls"
http = urllib3.PoolManager()
print()
for symbol in symbol_list['ename']:
  for year in [2022]:
    # print(link)
    try:
      link = "https://tse.ir/en/Archive/Trade/Cash/SymbolTrade/SymbolTrade_IRO1"+symbol[:-1]+"0001_"+str(year)+".xls"
      data = http.request('get', link)
      pd.read_html(data.data)[0].to_excel("G:\master_matus\payan_name1\\2_implement1\Archive_data\\"+symbol+"_"+str(year)+".xlsx")
    except ValueError:
      pass


# import pandas as pd
# import os
# from matplotlib import pyplot as plt
# import numpy as np
# import arabic_reshaper
# from bidi.algorithm import get_display
# symbol_path = os.listdir("G:\\master_matus\\payan_name1\\stocknet_dataset\\stocknet-dataset-master\\price\\raw")
# p_coef = []
# n_coef = []
# for sym in symbol_path:
#     index_data = pd.read_csv("G:\\master_matus\\payan_name1\\stocknet_dataset\\stocknet-dataset-master\\price\\raw\\"+sym)
#     # print(index_data)
#     dates_price = list(index_data['Date'].to_numpy())
#     dates_positive_message = np.zeros(len(dates_price))
#     dates_negative_message = np.zeros(len(dates_price))
#     index = sym.replace(".csv","")
#     try:
#        xls = pd.ExcelFile("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\labelsd\\"+ index + ".xlsx")
#     except FileNotFoundError:
#         continue
#     for shn in xls.sheet_names:
#         # d = date_to_seq(shn)
#         message_data = pd.read_excel(xls, sheet_name=shn)
#         try:
#          for l in  message_data['label']:
#
#                 if l == "positive":
#                     try:
#                         dates_positive_message[dates_price.index(shn)] += 1
#                     except ValueError:
#                         continue
#                 elif l =='negative':
#                     try:
#                         dates_negative_message[dates_price.index(shn)] += 1
#                     except ValueError:
#                         continue
#         except KeyError:
#              continue
#
# # print(index_data[index_data['<DTYYYYMMDD>']>20210720])
#     text = "نماد "+ index
#     reshaped_text = arabic_reshaper.reshape(text)  # correct its shape
#     bidi_text = get_display(reshaped_text)
#     prices = index_data['Close'].to_numpy()
#     n_price = (prices[300:800] - min(prices[300:800])) / (max(prices[300:800]) - min(prices[300:800]))
#     p_msg = (dates_positive_message[300:800] - min(dates_positive_message[300:800]))/(max(dates_positive_message[300:800]) - min(dates_positive_message[300:800]))
#     n_msg = (dates_negative_message[300:800] - min(dates_negative_message[300:800]))/(max(dates_negative_message[300:800]) - min(dates_negative_message[300:800]))
#     plt.plot(n_price, c="blue")
#     plt.bar([i for i in range(len(p_msg))], p_msg,edgecolor="green" , fill=False, width=0.2)
#     plt.bar([i for i in range(len(p_msg))], n_msg,edgecolor="red", fill=False, width=0.2)
#     plt.title(bidi_text+"   -:"+ str(np.corrcoef(n_msg,n_price)[0,1])+"  +"+ str(np.corrcoef(p_msg,n_price)[0,1]))
#     plt.show()
#     p_p_coefs = []
#     p_n_coefs = []
#     for i in range(0,4):
#         # print(i)
#         p_p_coefs.append(np.corrcoef(p_msg[:len(p_msg)-i], n_price[i :len(p_msg)])[0, 1])
#         p_n_coefs.append(np.corrcoef(n_msg[:len(p_msg)-i], n_price[i :len(p_msg)])[0, 1])
#     r1 = np.arange(4)
#     r2 = [x + 0.3 for x in r1]
#     plt.bar(r1, p_p_coefs, color='green', width=0.2, edgecolor='white', label='positive')
#     plt.bar(r2, p_n_coefs, color='red', width=0.2, edgecolor='white', label='negative')
#     plt.legend()
#     plt.title("pearson coefficient")
#     plt.show()
#     p_c = np.corrcoef(p_msg,n_price)[0, 1]
#     n_c = np.corrcoef(n_msg,n_price)[0, 1]
#     print("   -:"+ str(n_c)+"  +:"+ str(p_c))
#     if np.isnan(p_c) == False:
#        p_coef.append(p_c)
#     if np.isnan(n_c) == False:
#        n_coef.append(n_c)
# print("-:", sum(n_coef)/len(n_coef), "  +:",sum(p_coef)/len(p_coef))
# # print(pd.read_csv("G:\\master_matus\\payan_name1\\stocknet_dataset\\stocknet-dataset-master\\price\\raw\\AAPL.csv"))
import pandas as pd
import pytse_client as tse
# from sentiment_analyzer import  sentiment_analyzer as sn

print(tse.download(symbols="کایتا"))

# import pandas as pd
# from matplotlib import pyplot as plt
# import xlsxwriter
# import numpy as np
# import arabic_reshaper
# from bidi.algorithm import get_display
# def date_to_seq(date):
#     t = date.split("-")
#     if len(t[1]) == 1:
#         t[1] = "0" + t[1]
#     if len(t[2]) == 1:
#         t[2] = "0" + t[2]
#     return int(t[0]+t[1]+t[2])
# def delta_price(prices):
#     d_p = []
#     for i in range(1,len(prices)):
#         d_p.append(prices[i] - prices[i- 1])
#     return d_p
#
# symbls = ["خپارس", "فولاد","شستا","فملی","خگستر","کرازی","دبالک","ثشاهد","شسینا","خساپا","خودرو"]
# s_to_path = {
#     "فولاد":'follad',
#     "فملی":"fameli",
#     "خگستر" :"khagestar",
#     "خودرو":"Khodro",
#     "شستا" :"shasta",
#     "کرازی":"krazi",
#     "ثشاهد":"sshahed",
#     "دبالک":"dbalk",
#     "شسینا":"shasina",
#     "خساپا":"khasapa",
#     "خپارس":"khapars"
# }
# for sym in symbls:
#     index_data = pd.read_csv(s_to_path[sym]+".csv")
#     dates_price = list(index_data[index_data['<DTYYYYMMDD>'] > 20201129]['<DTYYYYMMDD>'].to_numpy())[::-1]
#     dates_positive_message = np.zeros(len(dates_price))
#     dates_negative_message = np.zeros(len(dates_price))
#     xls = pd.ExcelFile("Money Making Group_st.xlsx")
#     # xls = pd.ExcelFile("پردازش شده_تحلیل سهام و همفکری بورسی.xlsx")
#     index = sym
#     # print(len(xls.sheet_names))
#     for shn in xls.sheet_names:
#         d = date_to_seq(shn)
#         message_data = pd.read_excel(xls, sheet_name=shn)
#         try:
#           for s, l in zip(message_data['symbols'], message_data['label']):
#             if s.find(index) != -1:
#                 if l == 1:
#                     try:
#                         dates_positive_message[dates_price.index(d)] += 1
#                     except ValueError:
#                         continue
#                 elif l ==-1:
#                     try:
#                         dates_negative_message[dates_price.index(d)] += 1
#                     except ValueError:
#                         continue
#         except KeyError:
#             continue
#
#     # print(index_data[index_data['<DTYYYYMMDD>']>20210720])
#     text = "نماد "+ index
#     reshaped_text = arabic_reshaper.reshape(text)  # correct its shape
#     bidi_text = get_display(reshaped_text)
#     prices = index_data[index_data['<DTYYYYMMDD>']>20201129]['<CLOSE>'].to_numpy()
#     volume = index_data[index_data['<DTYYYYMMDD>']>20201129]['<VOL>'].to_numpy()
#     n_price = (prices[:35] - min(prices[:35])) / (max(prices[:35]) - min(prices[:35]))
#     n_vol = (volume[:35] - min(volume[:35])) / (max(volume[:35]) - min(volume[:35]))
#     if max(dates_negative_message[:35])!=0:
#         negative_msg = (dates_negative_message[:35] - min(dates_negative_message[:35]))/(max(dates_negative_message[:35]) - min(dates_negative_message[:35]))
#     else:
#         # print(index)
#         negative_msg = np.zeros(35)
#     if max(dates_positive_message[:35])!=0:
#         positive_msg = (dates_positive_message[:35] - min(dates_positive_message[:35]))/(max(dates_positive_message[:35]) - min(dates_positive_message[:35]))
#     else:
#         # print(index)
#         positive_msg = np.zeros(35)
#
#     # print(positive_msg)
#     # print(negative_msg)
#     # plt.plot(positive_msg, c="green",linestyle="dotted")
#     # plt.plot(negative_msg, c="red",linestyle="dotted")
#     plt.bar([i for i in range(35)], positive_msg,edgecolor="green" , fill=False, width=0.2)
#     plt.bar([i for i in range(35)], negative_msg,edgecolor="red", fill=False, width=0.2)
#     plt.plot(n_price, c="m")
#     plt.title(bidi_text)
#     plt.show()
#     p_p_coefs = []
#     p_n_coefs = []
#     for i in range(0,4):
#         print(i)
#         p_p_coefs.append(np.corrcoef(positive_msg[:35-i], n_price[i :35])[0, 1])
#         p_n_coefs.append(np.corrcoef(negative_msg[:35-i], n_price[i :35])[0, 1])
#     r1 = np.arange(4)
#     r2 = [x + 0.3 for x in r1]
#     plt.bar(r1, p_p_coefs, color='green', width=0.2, edgecolor='white', label='positive')
#     plt.bar(r2, p_n_coefs, color='red', width=0.2, edgecolor='white', label='negative')
#     d_prices = delta_price(prices[0:35])
#
#     percent_positive = []
#     for n,p in zip(negative_msg[:-1], positive_msg[:-1]):
#         if n+p == 0:
#             percent_positive.append(0)
#         else:
#             percent_positive.append(p/(n+p))
#     plt.legend()
#     plt.title("pearson coefficient")
#     plt.show()

#
import pandas as pd

# f = open("G:\\master_matus\\payan_name1\\2_implement1\\tweets\\tweets_labelled.csv",encoding="utf-8")
# d = f.read()
# messages = d.split("\n")
# for m in messages[:80]:
#     print(m)
#     print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# d = f.read().split(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
# for j,i in enumerate(d):
#     # print(len(i.strip(" ")))
#     print("=====================================================================")
#     if len(i) > 0:
#        print(j,"         ","@",i, "@")
# d = pd.read_csv("G:\\master_matus\\payan_name1\\2_implement1\\tweets\\tweets_labelled.csv",encoding="utf-8",delimiter=';')
# print(d)

import pandas as pd
import numpy as np
# 1111
# xls = pd.ExcelFile("processed_data//پردازش شده_تحلیل سهام و همفکری بورسی.xlsx")
txts = np.array([])
labels = np.array([])
symbols = np.array([])
# for shn in xls.sheet_names:
#     data = pd.read_excel(xls, sheet_name=shn)
#     # print(data.columns)
#     try:
#         labels = np.concatenate((labels, data['label'].to_numpy()))
#         txts = np.concatenate((txts, data['processed text'].to_numpy()))
#         symbols = np.concatenate((symbols, data['symbols'].to_numpy()))
#     except KeyError:
#         continue
# print(txts)
# print(labels)
# print(symbols)
# 2222
xls = pd.ExcelFile("processed_data//Money Making Group_st.xlsx")
for shn in xls.sheet_names:

    data = pd.read_excel(xls, sheet_name=shn)
    print(shn, data.columns)
    try:
        labels = np.concatenate((labels, data['new_label'].to_numpy()))
        txts = np.concatenate((txts, data['processed text'].to_numpy()))
        symbols = np.concatenate((symbols, data['symbols'].to_numpy()))
    except KeyError:
        continue
# 3333
# xls = pd.ExcelFile("processed_data//bours_rezaeii.xlsx")
# for shn in xls.sheet_names:
#     data = pd.read_excel(xls, sheet_name=shn)
#     try:
#         labels = np.concatenate((labels, data['label'].to_numpy()))
#         txts = np.concatenate((txts, data['processed text'].to_numpy()))
#         symbols = np.concatenate((symbols, data['symbols'].to_numpy()))
#     except KeyError:
#         continue
pd.DataFrame({"texts":txts, "labels":labels,"symbols":symbols}).to_excel("labeled_data_newset.xlsx")
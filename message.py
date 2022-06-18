# import pandas as pd
# import numpy as np
# import re
#
# f = open('G:\\semester7\\final-projerct-graduated\document\emoji_uicode.txt')
# stickers_code = f.read()
# list1 = stickers_code.split('\n')
# emoji_list_unicode = []
# for li in list1:
#             emoji_u = li.split("  ")[0].strip().split(" ")
#             if len(emoji_u) > 1:
#                 st = ''
#                 for emoji in emoji_u:
#                     zero = '0' * (8 - len(emoji))
#                     try:
#                         st += chr(int(zero + emoji, 16))
#                         if chr(int(zero + emoji, 16)) not in emoji_list_unicode:
#                             emoji_list_unicode.append(chr(int(zero + emoji, 16)))
#                     except ValueError:
#                         print(emoji)
#                     emoji_list_unicode.append(st)
#             else:
#                 emoji_u = emoji_u[0].split('..')
#                 try:
#                     for emoji in emoji_u:
#                         zero0 = '0' * (8 - len(emoji_u[0]))
#                         zero1 = '0' * (8 - len(emoji_u[1]))
#                         m1 = int(zero1 + emoji_u[1], 16)
#                         m0 = int(zero0 + emoji_u[0], 16)
#                         try:
#                             for i in range(m0, m1 + 1):
#                                 emoji_list_unicode.append(chr(i))
#                         except ValueError:
#                             print(m0, m1)
#                 except IndexError:
#                     zero0 = '0' * (8 - len(emoji_u[0]))
#                     m0 = (zero0 + emoji_u[0])
#                     try:
#                         emoji_list_unicode.append(chr(int(m0, 16)))
#                     except ValueError:
#                         print(emoji_u[0])
# emoji_list_unicode.append(chr(int("0000300b", 16)))
# emoji_list_unicode.append(chr(int("0000300a", 16)))
# emoji_list_unicode.append(chr(int("00002014", 16)))
# # emoji_list_unicode.append('#')
# # remove_sign = [u"\U0000300b", u"\U0000300a", u"\U00002014", "»", "«", "?", ":", "-", "_", "؟"]
# pattr = "["
# # sticker_file = open('sticker.txt')
# for em in emoji_list_unicode:
#      pattr += em
# f.close()
# pattr += "]+"
#
# data = pd.DataFrame(pd.read_excel("labels_data.xlsx"))
# print(data)
# text = np.array([])
# labels = np.array([])
# for i in range(0, 20, 2):
#     print(i)
#     text = np.concatenate((text,data.iloc[:, i].to_numpy()))
#     labels = np.concatenate((labels, data.iloc[:, i+1].to_numpy()))
# print(len([i for i in text if type(i) == str]))
# data_frame = pd.DataFrame({'Text':[i for i in text if type(i) == str],'Labels': [i for i in labels if i == -1 or i== 1]})
# data_frame.to_excel('true_data_labels.xlsx')
# # regrex_pattern = re.compile(pattern=pattr, flags=re.UNICODE)
# # data['Text'] = data['Text'].apply(lambda t:re.sub(r'( )( )+', r' ',regrex_pattern.sub(r' ', t.replace('\n', " "))))
# # print(data)






import pandas as pd
import pytse_client as tse
# from sentiment_analyzer import  sentiment_analyzer as sn

symbols_data = {}


def load_data_of_group(messages_path, users_path):
      file = pd.ExcelFile(messages_path)
      messages_data = {}
      for d in file.sheet_names:
          messages_data[d] = pd.read_excel(messages_path,sheet_name=d)
      users_info = pd.read_excel(users_path)
      users_id = {i: {'score':0, 'count':0} for i in users_info['id'].to_numpy()}
      return  messages_data, users_info,users_id

#
# def sentiment_analayzer(messages_data):
#     # region Description
#     for date_of_messages in messages_data.keys():
#            data_in_day = messages_data[date_of_messages]
#            data_in_day['sentiment'] = sn(data_in_day['processed text'])
#       # endregion


def load_market_data(symbol):
     return tse.download(symbols=symbol)
     # tse.download(symbols="وبملت", write_to_csv=True, include_jdate=True)
     # tse.download(symbols=["وبملت", "ولملت"], write_to_csv=True)
def symbol_directions_of_change(symbols_list,date):
         for s in symbols_list:
              symbols = s.replace("[",'').replace("]","").replace("'",'').split(",")
              for symbol in symbols:
                 try:
                     data = symbols_data[symbol]['data']

                 except KeyError:
                     data =  load_market_data(symbol)[symbol]

                     symbols_data[symbol]  = {'data': data}
                 print(data.index[data['date']==date].to_list())
                 try:
                    index = data.index[data['date']==date].to_list()[0]
                 except IndexError:
                     continue
                 today_price = data.loc[index, 'close']
                 yesterday_price =  data.loc[index + 1 , 'close']
                 delta_price = yesterday_price - today_price
                 if delta_price >= 0 :
                     symbols_data[symbol] ['change'] = 1
                 else:
                     symbols_data[symbol] ['change'] = -1


def users_scoring(messages_path, users_path):

     messages_data, users_info, users_id = load_data_of_group(messages_path,users_path)
     # sentiment_analayzer(messages_data)
     for date_of_messages in messages_data.keys():
              messages_info = messages_data[date_of_messages]
              symbol_directions_of_change(messages_info['symbols'].to_numpy(), date_of_messages)
              print(symbols_data)
              for id, symbols_list, sentiment in zip(messages_info['user_id'].to_numpy(),messages_info['symbols'].to_numpy(),messages_info['sentiment'].to_numpy()):
                  symbols = symbols_list.replace("[",'').replace("]","").replace("'",'').split(",")
                  score = 0
                  for s in symbols:
                     d =  symbols_data[s]['change']
                     if d == 1 and (sentiment == 0 or sentiment == 1):
                           score += 1
                     elif d == -1 and (sentiment == 2):
                          score += 1
                     else :
                         score -= 1
                  score /= len(symbols)
                  try:
                    users_id[id]['score'] = score
                    users_id[id]['count'] += 1
                  except KeyError:
                      continue
                      
     print(users_id)

if __name__ == '__main__':
    users_scoring("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\processed_data\\datav2.xlsx","G:\master_matus\\payan_name1\\2_implement1\\first_predict_model\\processed_data\\users-bours_rezaeii.xlsx")
#
# # t = pd.read_excel("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\processed_data\\bours_rezaeii.xlsx")['symbols'].to_numpy()[0]
# # print(type(t))
# print(tse.download("ملت"))

from telethon import TelegramClient
import datetime
from pytz import timezone
import xlsxwriter as xlwr
from txt_processing import *
from hazm import *
import pandas as pd
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep

normalizer_hazm = Normalizer()
normalizer = Normalizer()
api_id = 1790282
api_hash = 'ca3cd83dbafd959395e408e9575c31e0'
client = TelegramClient('anon', api_id, api_hash)


def message_process(new_message):
    post= {}
    post['post_id'] = int(str(id) + str(new_message.id))
    post['message'] = new_message.text
    post['sender_username'] = new_message.username
    # post['sender_title'] = utils.get_display_name(sender)

    try:
        if new_message.views:
            post['view'] = new_message.views
        else:
            post['view'] = -1
    except KeyError:
        post['view'] = -1
    post['process'] = 'false'
    post['date_get'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    post['date_published'] = new_message.date.astimezone(timezone('Asia/Tehran')).strftime("%Y-%m-%d %H:%M:%S")



async def main():
    t_preprocess = Preprocess()
    # Getting information about yourself
    me = await client.get_me()
    print(me.stringify())
    username = me.username
    print(username)
    print(me.phone)
    group_list = [
    {'name': "https://t.me/Vira_Bourse_Group",
           'date': datetime.datetime.now()},
    # #                {'name': "bours_rezaeii",
    # #                 'date': datetime.datetime.now()},
    #                {'name': "tse_mag",
    #                 'date': datetime.datetime.now()}
                        ]
    for group in group_list:
        message_texts = []
        message_ids = []
        message_users = []
        p_messages = []
        users_names = []
        users_id = []
        print(group['name'])
        excel_data_file = xlwr.Workbook("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\data\\" + group['name'] + ".xlsx")
        # excel_data_file = pd.ExcelWriter("G:\\master_matus\\payan_name1\\2_implement1\\first_predict_model\\"+group['name']+".xlsx")
        previous_date = (group['date'].year, group['date'].month, group['date'].day)
        date_sheet = excel_data_file.add_worksheet(str(group['date'].year)+"-" + str(group['date'].month)+"-" +str(group['date'].day))
        date_sheet.write(0, 0, 'user_id')
        date_sheet.write(0, 1,  "user_name")
        date_sheet.write(0, 2, "name")
        date_sheet.write(0, 3, "message_id")
        date_sheet.write(0, 4, "text")
        date_sheet.write(0, 5, "processed text")
        i = 1
        j = 1
        day = 0
        # all_participants = []
        # offset = 0
        # limit = 100
        # while True:
        #     participants = await client(GetParticipantsRequest(
        #                          group['name'], ChannelParticipantsSearch(''), offset, limit,
        #                           hash=0
        #       ))
        #     if not participants.users:
        #         break
        #     all_participants.extend(participants.users)
        #     offset += len(participants.users)
        # ids_list = []
        # active_status = []
        # fake_status = []
        # f_names = []
        # l_names = []
        # user_names_list = []
        # for member in all_participants:
        #     ids_list.append(member.id)
        #     active_status.append(~member.deleted)
        #     fake_status.append(member.fake)
        #     f_names.append(member.first_name)
        #     l_names.append(member.last_name)
        #     user_names_list.append(member.username)
        # pd.DataFrame({"id":ids_list,
        #               "active":active_status,
        #               "fake":fake_status,
        #                "first name":f_names,
        #                 "last name":l_names,
        #                  "username":user_names_list}).to_excel("users-"+group["name"]+".xlsx")
        async for message in client.iter_messages(group['name'], offset_date=group['date']):
            if message.text is None or message.from_id is None:
                  continue
            j += 1
            message_date = (message.date.year, message.date.month, message.date.day)
            try:
                txt = t_preprocess.remove_punctuation(t_preprocess.find_urls(t_preprocess.remove_emoji(message.text.replace("#"," #"))))
                txt = normalizer.normalize(txt)
                if len(txt)< 10:
                    continue
                if message_date == previous_date:
                    if message.media is None and message.from_id is not None:
                        try:
                           user_id = message.from_id.user_id
                        except AttributeError :
                           user_id = message.from_id.channel_id
                        try:
                            user = await client.get_entity(user_id)
                            if user.last_name is not None:
                               name = user.first_name + ' ' + user.last_name
                            else:
                               name = user.first_name
                        except Exception:
                            user = await client.get_entity(user_id)
                        date_sheet.write(i, 0, user_id)
                        date_sheet.write(i, 1, user.username)
                        date_sheet.write(i, 2, name)
                        date_sheet.write(i, 3, message.id)
                        date_sheet.write(i, 4, message.text)
                        date_sheet.write(i, 5, txt)

                        # message_texts.append(message.text)
                        # p_messages.append(txt)
                        # message_ids.append(message.id)
                        # message_users.append(user.username)
                        # users_names.append(name)
                        # users_id.append(user_id)
                        i += 1
                else:
                    # print(len(message_ids), len(message_texts), len(message_users), len(p_messages))
                    # pd.DataFrame({"id": message_ids,
                    #               'user_id':users_id,
                    #               "user_name": message_users,
                    #                'name':users_names,
                    #                "text": message_texts,
                    #               "processed text": p_messages}).to_excel(excel_data_file, sheet_name=date_sheet)
                    # print(i, ":?")
                    # message_texts = []
                    # message_ids = []
                    # message_users = []
                    # p_messages = []
                    # users_names = []
                    # users_id = []
                    txt = t_preprocess.remove_punctuation(
                        t_preprocess.find_urls(t_preprocess.remove_emoji(message.text)))
                    txt = normalizer.normalize(txt)
                    i = 1
                    previous_date = (message.date.year, message.date.month, message.date.day)
                    # date_sheet = str(message.date.year) + "-" + str(message.date.month) + "-" + str(message.date.day)
                    date_sheet = excel_data_file.add_worksheet(str(message.date.year)+"-" + str(message.date.month) + "-" + str(message.date.day))
                    date_sheet.write(0, 0, 'user_id')
                    date_sheet.write(0, 1, "user_name")
                    date_sheet.write(0, 2, "name")
                    date_sheet.write(0, 3, "message_id")
                    date_sheet.write(0, 4, "text")
                    date_sheet.write(0, 5, "processed text")
                    if True:
                        try:
                            user_id = message.from_id.user_id
                        except AttributeError :
                            user_id = message.from_id.channel_id
                        try:
                            user = await client.get_entity(user_id)
                            if user.last_name is not None:
                                name = user.first_name + ' ' + user.last_name
                            else:
                                name = user.first_name
                        except Exception:
                            user = await client.get_entity(user_id)
                        day += 1
                        # print("**")
                        # print(day,"**")
                        date_sheet.write(i, 0, user_id)
                        date_sheet.write(i, 1, user.username)
                        date_sheet.write(i, 2, name)
                        date_sheet.write(i, 3, message.id)
                        date_sheet.write(i, 4, message.text)
                        date_sheet.write(i, 5, txt)
                        # message_texts.append(message.text)
                        # p_messages.append(txt)
                        # message_ids.append(message.id)
                        # message_users.append(user.username)
                        # users_names.append(name)
                        # users_id.append(user_id)
                        i += 1
                    print(day)
                    if day > 300:
                        break
            # except TypeError:
            #     print(message.text)
            #     continue
            # except AttributeError:
            #     continue
            except IndexError:
                print("")
        excel_data_file.close()

with client:
    client.loop.run_until_complete(main())

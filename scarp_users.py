from telethon import TelegramClient
import datetime
import pandas as pd
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

api_id = 1790282
api_hash = 'ca3cd83dbafd959395e408e9575c31e0'
client = TelegramClient('anon', api_id, api_hash)
group_list = [{'name': "bours_rezaeii",
                'date': datetime.datetime.now()}]


async def main():
    for group in group_list:
        print('***')
        all_participants = []
        offset = 0
        limit = 100
        while True:
             participants = await client(GetParticipantsRequest(
                          group['name'], ChannelParticipantsSearch(''), offset, limit,
                         hash=0
                      ))
             if not participants.users:
                  break
             all_participants.extend(participants.users)
             offset += len(participants.users)
        print(offset)
        ids_list = []
        active_status = []
        fake_status = []
        f_names = []
        l_names = []
        user_names_list = []
        for member in all_participants:
                 ids_list.append(member.id)
                 active_status.append(~member.deleted)
                 fake_status.append(member.fake)
                 f_names.append(member.first_name)
                 l_names.append(member.last_name)
                 user_names_list.append(member.username)
        pd.DataFrame({"id":ids_list,
                          "active":active_status,
                          "fake":fake_status,
                          "first name":f_names,
                          "last name":l_names,
                          "username":user_names_list}).to_excel("users-"+group["name"]+".xlsx")


with client:
    client.loop.run_until_complete(main())

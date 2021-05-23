import asyncio 
from datetime import datetime, time, date
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from telethon import TelegramClient, events, sync
import pytz


# CLIENT SETTINGS
API_ID = 
API_HASH = 
client = TelegramClient('session_name', API_ID, API_HASH)

# BOT SETTINGS
ChatWarsChatId = #id получателя сообщений 
YanaId = #id отправителя сообщений

config = {"is_work": True}

@client.on(events.NewMessage(pattern='!старт', from_users=(YanaId)))
async def gaga(event):

    print('is_work', config['is_work'])
   
    if config['is_work'] == True:

        tz = pytz.timezone('Europe/Moscow')

        dtstart = tz.localize(datetime.combine(date.today(), time(16, 55)))
        t16_55 = rrule.rrule(
            rrule.DAILY,
            dtstart=dtstart,
            until=dtstart+relativedelta(months=1)
        )
        for t in t16_55:
            await client.send_message(ChatWarsChatId, '/ga_def', schedule=t)
        
        dtstart = tz.localize(datetime.combine(date.today(), time(00, 55)))
        t00_55 = rrule.rrule(
            rrule.DAILY,
            dtstart=dtstart,
            until=dtstart+relativedelta(months=1)
        )
        for t in t00_55:
            await client.send_message(ChatWarsChatId, '/ga_def', schedule=t)
        
        dtstart = tz.localize(datetime.combine(date.today(), time(8, 55)))
        t8_55 = rrule.rrule(
            rrule.DAILY,
            dtstart=dtstart,
            until=dtstart+relativedelta(months=1)
        )
        for t in t8_55:
            await client.send_message(ChatWarsChatId, '/ga_def', schedule=t)


with client.start():
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()

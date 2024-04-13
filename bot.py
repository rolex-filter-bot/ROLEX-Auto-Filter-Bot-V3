from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN = ""

RolexFilterBot = Client(
    name="ROLEX-Auto-Filter-Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )


@RolexFilterBot.on_message(filters.command("start"))


print("Bot was Started")

RolexFilterBot.run() 
